ssl._create_default_https_context = lambda: ssl.create_default_context(
    cafile=certifi.where()
)

# create search strategy using structured inputs

question = input("Do you already have a search strategy file saved?")
filename = input("Enter the file name of the search strategy: ")
file = f"{search_strategy}/pubmed/{filename}.txt"

if question == "no":
    parts = []
    string = []
    while True:
        term = input("Enter the search string: ")
        field = input("Enter the field type: ")
        string.append(f"'{term}'[{field}]")
        boolean = input("Enter the Boolean operator (e.g., OR, AND, NOT): ")
        
        if boolean == "OR":
            continue
    
        parts.append("(" + " OR ".join(string) + ")")
        string = []
    
        if boolean == "":
            break
            
        parts.append(boolean)
        
    query = " ".join(parts) # query = search strategy FROM HERE
    with open(file, "w") as f:
        f.write(query)
    
with open(file, "r") as f:
    query = f.read()

query = f"{query}"

# use NCBI's e-utitilies to pull PMIDs using e-search.

Entrez.email = "dkim246@jhmi.edu"
Entrez.api_key = 'bb1c481d8e167acd16f3616593c18b3aab08'

handle = Entrez.esearch(db= "pubmed", 
                        term = query, 
                        usehistory = "y", 
                        retmax = 2000,
                        retmode = "xml")

pmid = Entrez.read(handle)

pmid = pmid['IdList']
pmid = ",".join(pmid) # list to string
#with open(f"./data/pmid_{filename}.txt", 'w') as f:
#    f.write(pmid)
os.makedirs(f"{search}/pubmed/pmid/", exist_ok = True)
with open(f"{search}/pubmed/pmid/{filename}.txt", 'w') as f:
    f.write(pmid)
handle.close()

# ncbi e-summary
handle = Entrez.esummary(db= "pubmed", 
                         id = pmid, 
                         retmode = "xml", 
                         usehistory = "y", 
                         retmax = 2000)

xml = handle.read()
#xml_file = f"./data/{filename}.xml"
os.makedirs(f"{search}/pubmed/xml/", exist_ok = True)
xml_file = f"{search}/pubmed/xml/{filename}.xml"
with open(xml_file, "wb") as f:
    f.write(xml)   
handle.close()

import xml.etree.ElementTree as ET

tree = ET.parse(f"{xml_file}")
root = tree.getroot()

docsum = root[0]

def xml_parse(docsum):
    df = {}
    df["pmid"] = docsum.find("Id").text
    for item in docsum.findall("Item"):
        key = item.attrib.get("Name")
        if item.attrib.get("Type") == "List":
            values = [sub.text for sub in item.findall("Item") if sub.text]
            df[key] = values
        else:
            df[key] = item.text
    return df
records = [xml_parse(doc) for doc in root.findall(".//DocSum")]
df = pd.DataFrame(records)

os.makedirs(f"{search}/pubmed/", exist_ok = True)
csv_file = f"{search}/pubmed/{filename}.csv"
df.to_csv(csv_file, encoding = "utf-8")

# using e-fetch, the abstracts are pulled

handle = Entrez.efetch(
    db="pubmed",
    id=pmid,
    rettype="medline",
    retmode="text"
)

text = list(Medline.parse(handle))
data = pd.DataFrame(text)
data_csv = data.map(lambda x: ", ".join(map(str, x)) if isinstance(x, list) else x)
os.makedirs(f"{search}/pubmed/medline/", exist_ok = True)
data_csv.to_csv(f"{search}/pubmed/medline/{filename.replace("pm","md")}.csv", index=False)
globals()[f"{filename.replace("pm","md")}"] = data
handle.close()

abstracts = pd.DataFrame(text)[["PMID", "AB"]]
abstracts.rename(columns = {"PMID":"pmid", "AB":"abstract"}, inplace = True)
df = df.merge(abstracts, on = "pmid", how = "left")
df['year'] = df['PubDate'].str[:4]
csv_file = f"{search}/pubmed/{filename}.csv"
df.to_csv(csv_file, encoding = "utf-8")
num = len(df)
print(f"Number of records found: {num}")
data.info()