import ipywidgets as widgets
from IPython.display import display
import pandas as pd

def dataframe(columns):
    # create an empty dataframe for universal usage beyond current project 
    
    if columns == "":
        columns = ["id",
                   "study",
                   "subgroups",
                   "author(s)",
                   "title",
                   "abstract",
                   "year",
                   "journal",
                   "source"
                   "doi",
                   "url",
                   "title_abstract_screening"]
        df = pd.DataFrame(columns = columns)
        return df

def form():

    dataframe(columns = "")
    
    #df = pd.read_csv(url, encoding = "utf-8")
    a = widgets.IntText(value = 0, description = "ID ", min = 1, max = len(df)-1, layout = {"width": "20%"})
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
    

    
    yes = widgets.Button(value = "Yes", description = "Yes")
    maybe = widgets.Button(value = "Maybe", description = "Maybe")
    no = widgets.Button(value = "No", description = "No")
    save = widgets.Button(value = "Save", description = "Save")

    out = widgets.Output()

    buttons = [yes, maybe, no, save]
    
    w_a = display(a, out)
    w_b = display(b, out)
    w_c = display(c, out)
    w_d = display(d, out)
    w_e = display(e, out)
    w_f = display(f, out)
    w_g = display(g, out)
    w_h = display(h, out)
    w_i = display(i, out)
    w_j = display(j, out)
    w_k = display(k, out)
    
    title_abstract_screening = widgets.HBox(children = buttons)
    display(title_abstract_screening, buttons, out)
