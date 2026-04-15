<details><summary>Table of Contents</summary>
    
<a id="toc"></a>
    
- [Search strategy](#search-strategy)
- [Search](#search)
- [Deduplication](#deduplication)
- [Screening](#screening)
 
</details>

<details><summary>Kanban</summary>

```mermaid
---
config:
  kanban:
    ticketBaseUrl: 'https://mermaidchart.atlassian.net/browse/#TICKET#'
---
kanban
  [Systematic review]
      id1[Protocol]
      id2[Search strategy]
      id3[Search]
      id4[Deduplication]
      id5[Screening]
  [Data]
      id6[Database]
      id7[Form]
      id8[Collection]
      id9[Transformation]
  [Meta-analysis]
      id10[Effect size pooling]
      id11[Subgroup analysis]
      id12[Forest plots]
      id13[Regression]
  [Manuscript]
      id14[Tables and Figures]
      id15[Results]
      id16[Methods]
      id17[Introduction]
      id18[Discussion]
      id19[Abstract]
```

</details>

<details><summary>Flowchart</summary>

```mermaid
---
config:
  curve: stepBefore
---

graph LR

part1["systematic review"]
A["protocol"]
B["search strategy"]
C["search"]
D["deduplication"]
E["screening"]
E1["title and abstract<br>screening"]
E2["full-text screening"]

part2["data extraction"]
part3["meta-analysis"]

part1 --> A
A --> B
B --> C
C --> D
D --> E
E --> E1 & E2
E2 --> part2 --> part3
```

</details>