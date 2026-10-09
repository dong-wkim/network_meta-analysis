

```python
from src import search
```

**Search results of all previous network meta-analyses**

```python
with open("./data/wos_bptb.txt", "r") as f:
    query = f.read()

print(query)
```

```python
query = """("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab]) AND ("network meta-analysis"[tiab])"""
nma = search(query)
nma.head()
```

```python
nma.sort_values(by = ["year"], ascending = False)
nma.to_csv("./nma.csv", encoding = "utf-8")
```

```python
doi = nma["DOI"]
for x in doi:
    url = f"https://doi.org/{x}"
    print(url)
```

```python
nma["authors"] = nma["AuthorList"].str.join(", ")
nma["first_author"] = nma["AuthorList"].str[0].str.split().str[0]

def second_author(authors):
    if len(authors) > 1:
        return authors[1].split()[0]
    return None
    
nma["second_author"] = nma["AuthorList"].apply(second_author)
nma["number_of_authors"] = nma["AuthorList"].str.len()
nma.head()
```

```python
def study(authors, year):
    first = authors[0].split()[0]

    if len(authors) == 1:
        return f"{first}, {year}"

    elif len(authors) == 2:
        second = authors[1].split()[0]
        return f"{first} & {second}, {year}"
    else:
        return f"{first} et al., {year}"

studies = []

for authors, year in zip(nma["AuthorList"], nma["year"]):
    studies.append(study(authors, year))

nma["study"] = studies
```

```python
nma.head()
nma.sort_values(by = ["year"], ascending = False)
nma.to_csv("./nma.csv", encoding = "utf-8")
nma.to_excel("./nma.xlsx", index = False)
```

Yadav et al., 2025
Garcia-Linage et al., 2025
Calvert et al., 2025
Tang et al., 2025
Ebert et al., 2024
Vilchez-Cavazos et al., 2020
Sinding et al., 2020
Lind et al., 2020
Barié et al., 2020 
Tirupathi et al., 2019
Martin‐Alguacilet al., 2019
Martin‐Alguacilet al., 2018
Buescu et al., 2017
Lund et al., 2014 
Arida 2021
Beard 2001
Carter 1999
Feller 2003
Holm 2010
Machado 2018
Mo 2024
Mohammad 2013
Wipfler 2007
Horstmann et al., 2022
Komzák et al. 2022
Smith et al., 2020
Eriksson et al., 2000
Boonrion & Kietsiriroje, 2004


Garcia-Linage, 2025
Lucidi, 2025
Solanki, 2025
Ebert, 2024
Mo, 2024
Fallah, 2024
Popovic, 2024
Khatri, 2023
Kulinski, 2023
Horstmann, 2022
Komzak, 2022
Arida, 2021
Guglielmett, 2021
Krishna, 2021
Vilchez-Cavazos, 2020
Cristiani, 20221
Smith, 2020
Roger, 2020
Rajput, 2020
Barie, 2020
Lind, 2020
Mohtadi, 2019
Gupta, 2019
Gupta, 2020
Martin-Alguacil, 2018
Sajovic, 2018
Lu, 2017
Webster, 2016
Mohtadi, 2015
Karimi-Mobarakeh, 2015
Barenius, 2014
Lund, 2014
Papalia, 2015
Razi, 2014
Wipfler, 2011
Barenius, 2010
Moraiti, 2010
Taylor, 2009
Maletis, 2007
Zaffagnini, 2006
Harilainen, 2006
Laxdal, 2005
Ibrahim, 2005
Aglietti, 2004
Shaieb, 2002
Beard, 2001
Aune, 2001
