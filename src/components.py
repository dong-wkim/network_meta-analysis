import ipywidgets as widgets
import pandas as pd
import os
#from csv2df import csv2df

root = os.getcwd() # add this to resolve absolute paths
df = pd.read_csv("../systematic_review/search/records.csv", encoding = "utf-8")

# DONE - write out widgets (i.e., interactive forms) for each column that already exists, and 
# TODO then for columns that don't

columns = {
    'id': df['id'], 
    'study': df['study'],
    'subgroup': df['subgroup'], 
    'authors': df['authors'], 
    'first_author': df['first_author'], 
    'title': df['title'], 
    'abstract': df['abstract'], 
    'year': df['year'], 
    'language': df['language'], 
    'journal': df['journal'], 
    'source': df['source'], 
    'doi': df['doi'], 
    'doi_url': df['doi_url'], 
    'pmid': df['pmid'], 
    'pmid_url': df['pmid_url'],
    'second_author': df['second_author'], 
    'num_authors': df['num_authors']
}


a = widgets.IntText(value = 0, description = "ID ", min = 1, max = len(df)-1, layout = {"width": "100%"})
b = widgets.Textarea(value = "", description =  "study ", layout = {"width": "100%"}) # study
#c = widgets.Text(value = "", description = "subgroup(s) ", layout = {"width": "100%"})
c = widgets.Dropdown(options = subgroups, value = "BPTB", description = "subgroups")
#c = widgets.SelectMultiple(options = sorted(df['source'].dropna().astype(str).unique()), value = sorted(df['subgroup'].dropna().astype(str).unique())[0], description = "")
d = widgets.Text(value = "", description = "author(s) ", layout = {"width": "100%"}) # authors
e = widgets.Text(value = "", description = "title ", layout = {"width": "100%"}) # title
f = widgets.Textarea(value = "", description = "abstract ", layout = {"width": "100%", "height": "300px"}) # abstract
g = widgets.Text(value = "", description = "year ", layout = {"width": "100%"}) # year
h = widgets.Text(value = "",description = "journal ", layout = {"width": "100%"}) # journal
i = widgets.Dropdown(options = ['pubmed', 'embase', 'wos'], value = "pubmed", description = "source")
j = widgets.Text(value = "", description = "DOI ", layout = {"width": "100%"}) # doi
k = widgets.Text(value = "", description = "URL ", layout = {"width": "100%"}) # url


def update(change):
    study = df.loc[df["id"] == a.value, "study"] #b
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
yes = widgets.Button(value = "Yes", description = "Yes")
maybe = widgets.Button(value = "Maybe", description = "Maybe")
no = widgets.Button(value = "No", description = "No")
save = widgets.Button(value = "Save", description = "Save")

# april - may

# take a break and then create events 
# add non-existing data collection columns (back-end)
# find differences in studies from screening results and repeat all on covidence to see user interface 
# revise forms (front-end)
# deploy using sphinx, jupyter book, voila, or whatever
# do collection + analyses using R but this time in jupyter for R
# use documentation as submission manuscript 

items1 = [a, b, c, d, e, f, g, h, i, j, k]
items2 = [yes, maybe, no, save]
items3 = ['IKDC-SKF', 'Lysholm', 'Tegner', 'Pivot shift', 'Lachman', 'Instrumental laxity', 'Graft rupture']  # primary outcomes of interest
subgroups = ['BPTB', 'HT', 'QT', 'PLT', 'AT', 'TA']



#A = widgets.VBox(children = items1, layout = {"width": "100%"})
B = widgets.HBox(children = items2, layout = {"width": "100%"})
#C = widgets.Dropdown(options = items3, value = 'IKDC-SKF', description = 'outcome(s)', layout = {"width": "50%"})
#D = widgets.Dropdown(options = subgroups, value = "BPTB", description = "subgroups")
#E = widgets.FileUpload(accept='',  # Accepted file extension e.g. '.txt', '.pdf', 'image/*', 'image/*,.pdf'multiple=False  # True to accept multiple files upload else False

# x is a list of widgets (a, b, etc.) and their labels in a dict list.

def stack(x, y):
    w = widgets.Stack(list(x), selected_index=int(y))
    display(w)

grouped = [A, B, C, D]
individual = [a, b, c, d, e, f, g, h, i, j, k]

# clean and revise code by grouping interactive components by software principles, which i think are:
# views, models, compose
    


#stack(indexed, 0)
#stack(indexed, 1)
#stack(indexed, 2)
#stack(indexed, 3)

stack(individual, 0)
stack(individual, 1)
stack(individual, 2)
stack(individual, 3)
stack(individual, 4)
stack(individual, 5)
stack(individual, 6)
stack(individual, 7)
stack(individual, 8)
stack(individual, 9)
stack(individual, 10)


stack(indexed, 
out = widgets.Output(layout={'border': '1px solid black'})
out

update(None)