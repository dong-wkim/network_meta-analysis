import ipywidgets as widgets
from IPython.display import display
import pandas as pd

url = "https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search/records.csv"
df = pd.read_csv(url, encoding = "utf-8")

a = widgets.IntText(value = 0, description = "ID ", min = 1, max = len(df)-1, layout = {"width": "100%"})
b = widgets.Textarea(value = "", description = "study ", layout = {"width": "50%"}) # study
c = widgets.Dropdown(options = ['BPTB', 'HT', 'QT', 'PLT', 'AT', 'TA'], value = "BPTB", description = "subgroup", layout = {"width": "50%"})
d = widgets.Text(value = "", description = "author(s) ", layout = {"width": "100%"}) # authors
e = widgets.Text(value = "", description = "title ", layout = {"width": "100%"}) # title
f = widgets.Textarea(value = "", description = "abstract ", layout = {"width": "100%", "height": "300px"}) # abstract
g = widgets.Text(value = "", description = "year ", layout = {"width": "100%"}) # year
h = widgets.Text(value = "",description = "journal ", layout = {"width": "100%"}) # journal
j = widgets.Text(value = "", description = "DOI ", layout = {"width": "100%"}) # doi
k = widgets.Text(value = "", description = "URL ", layout = {"width": "100%"}) # url
def title_abstract_screening():

    df = pd.read_csv("../systematic_review/search/records.csv", encoding = "utf-8")
    df1 = pd.read_csv("../systematic_review/search/records.csv", encoding = "utf-8")
    df2 = pd.DataFrame(columns = ['id', 'study', 'subgroup', 'arm', 'outcome', 'ni', 'male', 'female', 'effect_size', 'xi', 'yi', 'sdi', 'sei', 'var'])
    df = pd.concat([df1, df2])
    a = widgets.IntText(value = 0, description = "ID ", min = 1, max = len(df)-1, layout = {"width": "100%"})
    b = widgets.Textarea(value = "", description = "study ", layout = {"width": "50%"}) # study
    c = widgets.Dropdown(options = ['BPTB', 'HT', 'QT', 'PLT', 'AT', 'TA'], value = "BPTB", description = "subgroup", layout = {"width": "50%"})
    d = widgets.Text(value = "", description = "author(s) ", layout = {"width": "100%"}) # authors
    e = widgets.Text(value = "", description = "title ", layout = {"width": "100%"}) # title
    f = widgets.Textarea(value = "", description = "abstract ", layout = {"width": "100%", "height": "300px"}) # abstract
    g = widgets.Text(value = "", description = "year ", layout = {"width": "100%"}) # year
    h = widgets.Text(value = "",description = "journal ", layout = {"width": "100%"}) # journal
    j = widgets.Text(value = "", description = "DOI ", layout = {"width": "100%"}) # doi
    k = widgets.Text(value = "", description = "URL ", layout = {"width": "100%"}) # url
    
    
    
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
    
    a.observe(update, names = "value")
    
    yes = widgets.Button(value = "Yes", description = "Yes")
    maybe = widgets.Button(value = "Maybe", description = "Maybe")
    no = widgets.Button(value = "No", description = "No")
    save = widgets.Button(value = "Save", description = "Save")
    
    buttons = [yes, maybe, no, save]
    outcomes = ['IKDC-SKF', 'Lysholm', 'Tegner', 'Pivot shift', 'Lachman', 'Instrumental laxity', 'Graft rupture']  # primary outcomes of interest
    
    def stack(x, y):
        w = widgets.Stack(list(x), selected_index=int(y))
        display(w)
    
    individual = [a, b, c, d, e, f, g, h, j, k]
    
    stack(individual, 0)
    stack(individual, 1)
    stack(individual, 2)
    stack(individual, 3)
    stack(individual, 4)
    stack(individual, 5)
    stack(individual, 6)
    stack(individual, 7)
    stack(individual, 8)
    
    yes = widgets.Button(value = "Yes", description = "Yes", style = {"button_color":"#A5D46A"})
    maybe = widgets.Button(description = "Maybe", style = {"button_color": "#FFFF80"})
    no = widgets.Button(description = "No", style = {"button_color": "#ffcfbf"})
    
    buttons = [yes, maybe, no]
    
    out = widgets.Output()
    
    vertical = widgets.VBox(children = buttons)
    horizontal = widgets.HBox(children = buttons, layout = {"display":"flex"})
    
    display(horizontal, out)