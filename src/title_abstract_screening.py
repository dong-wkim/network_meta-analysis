import ipywidgets as widgets
from IPython.display import display
import pandas as pd

def form():
    url = "https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search/records.csv"
    df = pd.read_csv(url, encoding = "utf-8")
    
    a, a1 =  widgets.IntText(description = "ID", layout = {"width":"20%"}),\
             widgets.IntSlider(value = 0, readout = False, min = 1, max = len(df)-1, layout = {"width":"70%"}),
    
    link = widgets.jslink((a, "value"),(a1,"value"))
    out = widgets.Output()
    
    
    # design 
    A = widgets.HBox(children = [a, a1])
    b = widgets.HTML(description = "study ", layout = {"width": "50%"}) # study
    c = widgets.HTML(description = "subgroup", layout = {"width": "50%"})
    d = widgets.HTML(value = "", description = "author(s) ", layout = {"width": "90%"}) # authors
    e = widgets.HTML(value = "", description = "title ", layout = {"width": "90%"}) # title
    f = widgets.HTML(value = "", description = "abstract ", layout = {"width": "91.5%", "height": "300px"}) # abstract
    g = widgets.HTML(value = "", description = "year ", layout = {"width": "90%"}) # year
    h = widgets.HTML(value = "", description = "journal ", layout = {"width": "90%"}) # journal
    i = widgets.HTML(description = "source", layout = {"width": "50%"})
    j = widgets.HTML(value = "", description = "DOI ", layout = {"width": "90%"}) # doi
    k = widgets.HTML(value = "", description = "URL ", layout = {"width": "90%"}) # url
    
    columns = ["study", "subgroup", "authors", "title", "abstract", "year", "journal", "source", "doi", "url"]
    wid = [b, c, d, e, f, g, h, i, j, k]
    
    mapping = dict(zip(columns, wid))
    
    def update(change):
        id = df.loc[df["id"] == a.value]
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
            c.value = str(subgroup.iloc[0])
            d.value = str(authors.iloc[0])
            e.value = str(title.iloc[0])
            f.value = str(abstract.iloc[0])
            g.value = str(year.iloc[0])
            h.value = str(journal.iloc[0])
            i.value = str(source.iloc[0])
            j.value = str(doi.iloc[0])
            k.value = str(url.iloc[0])    
    
    a.observe(update, names = "value")
    display(A, b, c, d, e, f, g, h, i, j, k)
    df = df.sort_values(by = 'id')
    df.head()    

def result():
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
    
    buttons = widgets.HBox([yes, maybe, no, save])
    display(buttons, out)
    return buttons
    
if __name__ == "__main__":
    form()
    result()

