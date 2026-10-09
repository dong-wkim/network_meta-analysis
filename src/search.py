import ssl
import certifi
import xml.etree.ElementTree as ET
import pandas as pd
from Bio import Entrez, Medline

def search(query):
    ssl._create_default_https_context = lambda: ssl.create_default_context(
        cafile=certifi.where()
    )
    
    # use NCBI's e-utitilies to pull PMIDs using e-search.
    
    Entrez.email = "dkim246@jhmi.edu"
    Entrez.api_key = 'bb1c481d8e167acd16f3616593c18b3aab08'
    
    handle = Entrez.esearch(db= "pubmed", 
                            term = query, 
                            usehistory = "y", 
                            retmax = 2000,
                            retmode = "xml")
    
    pmids = Entrez.read(handle)["IdList"]
    handle.close()
    
    if not pmids:
        return pd.DataFrame()
    
    pmid_string = ",".join(pmids)

    # ncbi e-summary
    handle = Entrez.esummary(db= "pubmed", 
                             id = pmid_string, 
                             retmode = "xml", 
                             usehistory = "y", 
                             retmax = 2000)
    
    xml = handle.read()
    handle.close()

    root = ET.fromstring(xml)    
    def xml_parse(docsum):
        record = {}
        record["pmid"] = docsum.find("Id").text
        
        for item in docsum.findall("Item"):
            key = item.attrib.get("Name")
            if item.attrib.get("Type") == "List":
                record[key] = [sub.text for sub in item.findall("Item") if sub.text]
            else:
                record[key] = item.text
        return record
        
    records = [xml_parse(doc) for doc in root.findall(".//DocSum")]
    df = pd.DataFrame(records)
    
    # using e-fetch, the abstracts are pulled
    
    handle = Entrez.efetch(
        db="pubmed",
        id=pmid_string,
        rettype="medline",
        retmode="text"
    )
    
    text = list(Medline.parse(handle))

    handle.close()
    
    abstracts = (
        pd.DataFrame(text)
          .rename(columns={"PMID": "pmid", "AB": "abstract"})
          .loc[:, ["pmid", "abstract"]]
    )
    df = df.merge(abstracts, on = "pmid", how = "left")
    df["year"] = df["PubDate"].str.extract(r"(\d{4})")
    return df
