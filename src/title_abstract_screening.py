import ipywidgets as widgets
from IPython.display import display
import pandas as pd

def title_abstract_screening():
    
    url = "https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search/records.csv"
    
    df = pd.read_csv(url, encoding = "utf-8")
    a = widgets.BoundedIntText(value = 0, description = "ID ", min = 0, max = len(df)-1, layout = {"width": "30%"})
    b = widgets.Text(value = "", description = "study ", layout = {"width": "50%"}) # study
    c = widgets.Dropdown(options = ['BPTB', 'HT', 'QT', 'PLT', 'AT', 'TA'], value = "BPTB", description = "subgroup", layout = {"width": "50%"})
    d = widgets.Text(value = "", description = "author(s) ", layout = {"width": "90%"}) # authors
    e = widgets.Text(value = "", description = "title ", layout = {"width": "90%"}) # title
    f = widgets.HTML(value = "", description = "abstract ", layout = {"width": "91.5%", "height": "300px"}) # abstract
    g = widgets.Text(value = "", description = "year ", layout = {"width": "90%"}) # year
    h = widgets.Text(value = "", description = "journal ", layout = {"width": "90%"}) # journal
    i = widgets.Dropdown(options = ["PubMed", "Embase", "Web of Science"], value = "PubMed", description = "source", layout = {"width": "50%"})
    j = widgets.Text(value = "", description = "DOI ", layout = {"width": "90%"}) # doi
    k = widgets.Text(value = "", description = "URL ", layout = {"width": "90%"}) # url
    
    def update(change):
        study = df.loc[df["id"] == a.value, "study"]
        subgroup =  df.loc[df["id"] == a.value, "subgroup"]
        authors =  df.loc[df["id"] == a.value, "authors"]
        title =  df.loc[df["id"] == a.value, "title"]
        abstract =  df.loc[df["id"] == a.value, "abstract"]
        year =  df.loc[df["id"] == a.value, "year"]
        journal =  df.loc[df["id"] == a.value, "journal"]
        source =  df.loc[df["id"] == a.value, "source"]
        doi =  df.loc[df["id"] == a.value, "doi"]
        url =  df.loc[df["id"] == a.value, "doi_url"]
    
        if a.value > 0:
           b.value = str(study.iloc[0])
           d.value = str(authors.iloc[0])
           e.value = str(title.iloc[0])
           f.value = str(abstract.iloc[0])
           g.value = str(year.iloc[0])
           h.value = str(journal.iloc[0])
           j.value = str(doi.iloc[0])
           k.value = str(url.iloc[0])
    
        else:
            b.value = ""
            d.value = ""
            e.value = ""
            f.value = ""
            g.value = ""
            h.value = ""
            j.value = ""
            k.value = ""
    
    a.observe(update, names = "value") # observe widget 'a' (i.e., ID column) for any changes, and if there is, then display all of the widgets corresponding to the value of 'a'.
    
    
    yes = widgets.Button(
        value = "Yes", 
        description = "Yes", 
        icon = "check", 
        button_style = "success", 
        layout = {
            "width":"100%"})
    
    maybe = widgets.Button(
        value = "Maybe", 
        description = "Maybe", 
        icon = "", 
        button_style = "warning")
    
    no = widgets.Button(
        value = "No", 
        description = "No", 
        icon = "times", 
        button_style = "danger")
    
    save = widgets.Button(
        value = "Save", 
        description = "Save", 
        icon = "floppy-o", 
        button_style = "info")
    
    out = widgets.Output()
    
    buttons = [yes, maybe, no, save]
        
    A = display(a, out) # id
    B = display(b, out) # study
    C = display(c, out) # subgroups
    D = display(d, out) # author(s)
    E = display(e, out) # title
    F = display(f, out) # abstract
    G = display(g, out) # year
    H = display(h, out) # journal
    I = display(i, out) # source
    J = display(j, out) # doi
    K = display(k, out) # url 

    vbox = widgets.VBox([A, B, C, D, E, F, G, H, I, J, K])
    hbox = widgets.HBox(children = buttons)
    
    display(vbox, hbox, out)
        
if __name__ == "__main__":
    title_abstract_screening()

