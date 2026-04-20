::: {#60a2cb4f-08fd-4b71-beca-29f72e57b338 .cell .markdown}
<!-- Notes:

Read this and follow the steps to organize and stuff.
https://medium.com/@caneuenschwander/how-to-turn-a-messy-jupyter-notebook-into-a-professional-python-project-f34d5ee7f88b



-->
:::

::: {#3963aa21-61c3-448e-9a26-f21b97d39bba .cell .markdown}
<style>
  .text {
    white-space: pre;
  }
</style>
<div style="font-family:Times New Roman;float:center;"><p></p></div>
<div align="center">
    <font size="5" style="font-family:Times New Roman;">What is the optimal graft choice for anterior cruciate ligament reconstruction surgery?</font><br>
    <br>
    <a href="https://dongwkim.com"><img src="logo.svg" alt="Logo" width="200" height="200"></a><br><br>
	<font size="5" style="font-family:Times New Roman;font-variant: small-caps;">Thesis</font><br><br>
    <div align="center"><font size="1"><i>In fulfillment for the award of the degree of:</i></font><br></div>
    <div align="center"><font size="3" style="font-family:Times New Roman;font-variant: small-caps;">doctor of philosophy</font></div>
</div>

`<br>`{=html} `</div>`{=html} `<br>`{=html} `<font size = "1em">`{=html}
`<sup>`{=html}1`</sup>`{=html} Department of Anatomy, Jagiellonian
University, Kraków, Poland `<br/>`{=html} `<sup>`{=html}2`</sup>`{=html}
Whiting College of Engineering, Johns Hopkins University, Baltimore, MD,
United States `<br/>`{=html} `<sup>`{=html}3`</sup>`{=html} Harvard
Dataverse, Harvard University, Cambridge, MA, United States
`</font>`{=html} `</div>`{=html}
:::

::: {#1370ab4e-67a5-4962-b418-90da4313b85b .cell .markdown}
<div>
<details>
    <summary style="font-family:Times New Roman;">Table of Contents</summary>  
    
<a id="toc"></a>

- [Systematic Review](#systematic-review)
    - [Search strategy](#search-strategy)
    - [Search](#search)
    - [Deduplication](#deduplication)
    - [Screening](#screening)
- [Data Collection](#data-collection)

</details>
<details>
    <summary style="font-family:Times New Roman;">Kanban</summary>  


```mermaid

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
<details>
    <summary style="font-family:Times New Roman;">Flowchart</summary>
  
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
<details>
    <summary style="font-family:Times New Roman;">Checklist</summary>

<table style="width:100%;">
<colgroup>
<col style="width: 21%" />
<col style="width: 6%" />
<col style="width: 59%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Section/Topic</strong></th>
<th style="text-align: center;"><strong>Item #</strong></th>
<th style="text-align: center;"><strong>Checklist Item</strong></th>
<th style="text-align: center;"><strong>Reported on Page #</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>TITLE</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Title</p>
</blockquote></td>
<td>1</td>
<td>Identify the report as a systematic review <em>incorporating a
network meta-analysis (or related form of meta-analysis).</em></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>ABSTRACT</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Structured summary</p>
</blockquote></td>
<td>2</td>
<td><p>Provide a structured summary including, as applicable:</p>
<blockquote>
<p><strong>Background:</strong> main objectives</p>
<p><strong>Methods:</strong> data sources; study eligibility criteria,
participants, and interventions; study appraisal; and <em>synthesis
methods, such as network meta-analysis.</em></p>
<p><strong>Results:</strong> number of studies and participants
identified; summary estimates with corresponding confidence/credible
intervals; <em>treatment rankings may also be discussed. Authors may
choose to summarize pairwise comparisons against a chosen treatment
included in their analyses for brevity.</em></p>
<p><strong>Discussion/Conclusions:</strong> limitations; conclusions and
implications of findings.</p>
<p><strong>Other:</strong> primary source of funding; systematic review
registration number with registry name.</p>
</blockquote></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>INTRODUCTION</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Rationale</p>
</blockquote></td>
<td>3</td>
<td>Describe the rationale for the review in the context of what is
already known<em>, including mention of why a network meta-analysis has
been conducted.</em></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Objectives</p>
</blockquote></td>
<td>4</td>
<td>Provide an explicit statement of questions being addressed, with
reference to participants, interventions, comparisons, outcomes, and
study design (PICOS).</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>METHODS</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Protocol and registration</p>
</blockquote></td>
<td>5</td>
<td>Indicate whether a review protocol exists and if and where it can be
accessed (e.g., Web address); and, if available, provide registration
information, including registration number.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Eligibility criteria</p>
</blockquote></td>
<td>6</td>
<td>Specify study characteristics (e.g., PICOS, length of follow-up) and
report characteristics (e.g., years considered, language, publication
status) used as criteria for eligibility, giving rationale. <em>Clearly
describe eligible treatments included in the treatment network, and note
whether any have been clustered or merged into the same node (with
justification).</em></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Information sources</p>
</blockquote></td>
<td>7</td>
<td>Describe all information sources (e.g., databases with dates of
coverage, contact with study authors to identify additional studies) in
the search and date last searched.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Search</p>
</blockquote></td>
<td>8</td>
<td>Present full electronic search strategy for at least one database,
including any limits used, such that it could be repeated.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Study selection</p>
</blockquote></td>
<td>9</td>
<td>State the process for selecting studies (i.e., screening,
eligibility, included in systematic review, and, if applicable, included
in the meta-analysis).</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Data collection process</p>
</blockquote></td>
<td>10</td>
<td>Describe method of data extraction from reports (e.g., piloted
forms, independently, in duplicate) and any processes for obtaining and
confirming data from investigators.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Data items</p>
</blockquote></td>
<td>11</td>
<td>List and define all variables for which data were sought (e.g.,
PICOS, funding sources) and any assumptions and simplifications
made.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p><strong>Geometry of the network</strong></p>
</blockquote></td>
<td><strong>S1</strong></td>
<td>Describe methods used to explore the geometry of the treatment
network under study and potential biases related to it. This should
include how the evidence base has been graphically summarized for
presentation, and what characteristics were compiled and used to
describe the evidence base to readers.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Risk of bias within individual studies</p>
</blockquote></td>
<td>12</td>
<td>Describe methods used for assessing risk of bias of individual
studies (including specification of whether this was done at the study
or outcome level), and how this information is to be used in any data
synthesis.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Summary measures</p>
</blockquote></td>
<td>13</td>
<td>State the principal summary measures (e.g., risk ratio, difference
in means). <em>Also describe the use of additional summary measures
assessed, such as treatment rankings and surface under the cumulative
ranking curve (SUCRA) values, as well as modified approaches used to
present summary findings from meta-analyses.</em></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Planned methods of analysis</p>
</blockquote></td>
<td>14</td>
<td><p>Describe the methods of handling data and combining results of
studies for each network meta-analysis. This should include, but not be
limited to:</p>
<ul>
<li><p><em>Handling of multi-arm trials;</em></p></li>
<li><p><em>Selection of variance structure;</em></p></li>
<li><p><em>Selection of prior distributions in Bayesian analyses;
and</em></p></li>
<li><p><em>Assessment of model fit.</em></p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p><strong>Assessment of Inconsistency</strong></p>
</blockquote></td>
<td><strong>S2</strong></td>
<td>Describe the statistical methods used to evaluate the agreement of
direct and indirect evidence in the treatment network(s) studied.
Describe efforts taken to address its presence when found.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Risk of bias across studies</p>
</blockquote></td>
<td>15</td>
<td>Specify any assessment of risk of bias that may affect the
cumulative evidence (e.g., publication bias, selective reporting within
studies).</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Additional analyses</p>
</blockquote></td>
<td>16</td>
<td><p>Describe methods of additional analyses if done, indicating which
were pre-specified. This may include, but not be limited to, the
following:</p>
<ul>
<li><p>Sensitivity or subgroup analyses;</p></li>
<li><p>Meta-regression analyses;</p></li>
<li><p><em>Alternative formulations of the treatment network;
and</em></p></li>
<li><p><em>Use of alternative prior distributions for Bayesian analyses
(if applicable).</em></p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>RESULTS†</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Study selection</p>
</blockquote></td>
<td>17</td>
<td>Give numbers of studies screened, assessed for eligibility, and
included in the review, with reasons for exclusions at each stage,
ideally with a flow diagram.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p><strong>Presentation of network structure</strong></p>
</blockquote></td>
<td><strong>S3</strong></td>
<td>Provide a network graph of the included studies to enable
visualization of the geometry of the treatment network.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p><strong>Summary of network geometry</strong></p>
</blockquote></td>
<td><strong>S4</strong></td>
<td>Provide a brief overview of characteristics of the treatment
network. This may include commentary on the abundance of trials and
randomized patients for the different interventions and pairwise
comparisons in the network, gaps of evidence in the treatment network,
and potential biases reflected by the network structure.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Study characteristics</p>
</blockquote></td>
<td>18</td>
<td>For each study, present characteristics for which data were
extracted (e.g., study size, PICOS, follow-up period) and provide the
citations.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Risk of bias within studies</p>
</blockquote></td>
<td>19</td>
<td>Present data on risk of bias of each study and, if available, any
outcome level assessment.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Results of individual studies</p>
</blockquote></td>
<td>20</td>
<td>For all outcomes considered (benefits or harms), present, for each
study: 1) simple summary data for each intervention group, and 2) effect
estimates and confidence intervals. <em>Modified approaches may be
needed to deal with information from larger networks.</em></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Synthesis of results</p>
</blockquote></td>
<td>21</td>
<td>Present results of each meta-analysis done, including
confidence/credible intervals. <em>In larger networks, authors may focus
on comparisons versus a particular comparator (e.g. placebo or standard
care), with full findings presented in an appendix. League tables and
forest plots may be considered to summarize pairwise comparisons.</em>
If additional summary measures were explored (such as treatment
rankings), these should also be presented.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p><strong>Exploration for inconsistency</strong></p>
</blockquote></td>
<td><strong>S5</strong></td>
<td>Describe results from investigations of inconsistency. This may
include such information as measures of model fit to compare consistency
and inconsistency models, <em>P</em> values from statistical tests, or
summary of inconsistency estimates from different parts of the treatment
network.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Risk of bias across studies</p>
</blockquote></td>
<td>22</td>
<td>Present results of any assessment of risk of bias across studies for
the evidence base being studied.</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Results of additional analyses</p>
</blockquote></td>
<td>23</td>
<td>Give results of additional analyses, if done (e.g., sensitivity or
subgroup analyses, meta-regression analyses<em>, alternative network
geometries studied, alternative choice of prior distributions for
Bayesian analyses,</em> and so forth).</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>DISCUSSION</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Summary of evidence</p>
</blockquote></td>
<td>24</td>
<td>Summarize the main findings, including the strength of evidence for
each main outcome; consider their relevance to key groups (e.g.,
healthcare providers, users, and policy-makers).</td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Limitations</p>
</blockquote></td>
<td>25</td>
<td>Discuss limitations at study and outcome level (e.g., risk of bias),
and at review level (e.g., incomplete retrieval of identified research,
reporting bias). <em>Comment on the validity of the assumptions, such as
transitivity and consistency. Comment on any concerns regarding network
geometry (e.g., avoidance of certain comparisons).</em></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Conclusions</p>
</blockquote></td>
<td>26</td>
<td>Provide a general interpretation of the results in the context of
other evidence, and implications for future research.</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>FUNDING</strong></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Funding</p>
</blockquote></td>
<td>27</td>
<td>Describe sources of funding for the systematic review and other
support (e.g., supply of data); role of funders for the systematic
review. This should also include information regarding whether funding
has been received from manufacturers of treatments in the network and/or
whether some of the authors are content experts with professional
conflicts of interest that could affect use of treatments in the
network.</td>
<td></td>
</tr>
</tbody>
</table>

PICOS = population, intervention, comparators, outcomes, study design.

\* Text in italics indicates wording specific to reporting of network
meta-analyses that has been added to guidance from the PRISMA statement.

† Authors may wish to plan for use of appendices to present all relevant
information in full detail for items in this section.


</details>
:::

::: {#a57fbc61-c21b-45aa-b0ff-7da6ef6ca746 .cell .markdown}
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                  pubmed                                                                                                                                                                       embase                                                                                                                                                                  web of science                                                                                
  ------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----
  patellar     [pm_bptb](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_bptb.csv)`<br>`{=html}`<sup>`{=html}(*n* = [em_bptb](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_bptb.csv)`<br>`{=html}`<sup>`{=html}(*n* = [wos_bptb](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_bptb.csv)`<br>`{=html}`<sup>`{=html}(*n* = 
                                                                                           190)`</sup>`{=html}                                                                                                                                                           73)`</sup>`{=html}                                                                                                                                                          186)`</sup>`{=html}                                                                             

  hamstring      [pm_ht](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_ht.csv)`<br>`{=html}`<sup>`{=html}(*n* =     [em_ht](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_ht.csv)`<br>`{=html}`<sup>`{=html}(*n* =      [wos_ht](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_ht.csv)`<br>`{=html}`<sup>`{=html}(*n*    
                                                                                           202)`</sup>`{=html}                                                                                                                                                           97)`</sup>`{=html}                                                                                                                                                         =253)`</sup>`{=html}                                                                             

  quadriceps     [pm_qt](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_qt.csv)`<br>`{=html}`<sup>`{=html}(*n* =     [em_qt](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_qt.csv)`<br>`{=html}`<sup>`{=html}(*n* =     [wos_qt](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_qt.csv)`<br>`{=html}`<sup>`{=html}(*n* =   
                                                                                           165)`</sup>`{=html}                                                                                                                                                          114)`</sup>`{=html}                                                                                                                                                          70)`</sup>`{=html}                                                                              

  peroneus      [pm_plt](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_plt.csv)`<br>`{=html}`<sup>`{=html}(*n* =   [em_plt](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_plt.csv)`<br>`{=html}`<sup>`{=html}(*n* =   [wos_plt](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_plt.csv)`<br>`{=html}`<sup>`{=html}(*n* =  
  longus                                                                                    2)`</sup>`{=html}                                                                                                                                                            25)`</sup>`{=html}                                                                                                                                                           4)`</sup>`{=html}                                                                              

  Achilles       [pm_at](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_at.csv)`<br>`{=html}`<sup>`{=html}(*n* =     [em_at](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_at.csv)`<br>`{=html}`<sup>`{=html}(*n* =     [wos_at](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_at.csv)`<br>`{=html}`<sup>`{=html}(*n* =   
                                                                                            7)`</sup>`{=html}                                                                                                                                                            5)`</sup>`{=html}                                                                                                                                                           10)`</sup>`{=html}                                                                              

  tibialis       [pm_ta](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_ta.csv)`<br>`{=html}`<sup>`{=html}(*n* =     [em_ta](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_ta.csv)`<br>`{=html}`<sup>`{=html}(*n* =     [wos_ta](https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_ta.csv)`<br>`{=html}`<sup>`{=html}(*n* =   
                                                                                            7)`</sup>`{=html}                                                                                                                                                            3)`</sup>`{=html}                                                                                                                                                            8)`</sup>`{=html}                                                                              
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#1d80c0a7-7085-4f66-92e9-c9888cfcf523 .cell .markdown}

------------------------------------------------------------------------

`<a id="systematic-review">`{=html}`</a>`{=html}

<h1 align="center" style="font-family:Times New Roman;font-variant:small-caps;">Systematic Review</h1>
:::

::: {#21087bf9-4181-4397-8e10-dee41e958637 .cell .markdown}
Define directory structure and store paths as global variables.
:::

::: {#1c51cdb3-ee2e-4fd9-9fb4-971278dfdeae .cell .markdown}
    ./research/
    ├── ./research/systematic_review/
    |   |   
    │   ├── ./research/systematic_review/protocol/  
    |   |   |
    │   │   ├── ./research/systematic_review/protocol/prospero  
    │   │   └── ./research/systematic_review/protocol/cochrane  
    |   |
    │   ├── ./research/systematic_review/search_strategy/  
    |   |   |
    │   │   ├── ./research/systematic_review/search_strategy/pubmed  
    │   │   ├── ./research/systematic_review/search_strategy/embase  
    │   │   └── ./research/systematic_review/search_strategy/wos  
    |   |
    │   ├── ./research/systematic_review/search/  
    |   |   |
    │   │   ├── ./research/systematic_review/search/pubmed
    │   │   ├── ./research/systematic_review/search/embase
    │   │   └── ./research/systematic_review/search/wos
    |   |
    │   ├── ./research/systematic_review/deduplication/
    |   |   |
    │   │   ├── ./research/systematic_review/deduplication/doi
    │   │   ├── ./research/systematic_review/deduplication/key
    │   │   └── ./research/systematic_review/deduplication/id
    |   |
    │   └── ./research/systematic_review/screening/
    |       |
    │       ├── ./research/systematic_review/screening/title_abstract_screening
    │       ├── ./research/systematic_review/screening/PDF
    │       └── ./research/systematic_review/screening/full-text_screening
    |
    ├── ./research/data
    ├── ./research/meta-analysis
    ├── ./research/manuscript
    ├── ./research/README.ipynb
    ├── ./research/docs
    └── ./research/src
:::

::: {#313ab029-4543-4d62-9052-0f678a537ccc .cell .markdown}
Install `PyPI` modules in `requirements.txt`.
:::

::: {#32daa4dc-d5f9-4ad8-8468-227356840bd7 .cell .code}
``` python
%pip install -q pandas mermaid-py biopython

!cd .venv; Scripts/Activate.ps1 
!pip install -r requirements.txt
```
:::

::: {#eedfe910-f3b3-487f-879b-6928801e7908 .cell .markdown}
Exclude certain files from syncing with remote github repository with
`gitignore` file.
:::

::: {#b3db5113-25fd-41c2-8517-2adc1e3d9048 .cell .code execution_count="2"}
``` python
ignore = f""".venv/
*/*.gsheet
*/*.gdoc"""

gitignore = ['.venv/', '.gsheet', '.gdoc']
ignore = "\n".join(gitignore)
with open(f"./.gitignore", "w") as f:
    f.write(ignore)
```
:::

::: {#f1cedad7-1235-4008-9dbb-5f34414c77bd .cell .markdown}
Import the necessary modules.
:::

::: {#ee98e7bc-08ac-45ca-b0fd-bacd14a99af3 .cell .code execution_count="3"}
``` python
import subprocess
import sys
import os
import pandas as pd
from Bio import Entrez, Medline
import ssl
import certifi
import re
from pathlib import Path
```
:::

::: {#f762c238-20bd-4098-a90c-ab68e29a4caf .cell .markdown}
Set absolute directory paths for important sub-project folders as
variables in the global environment for use in scripts downstream and
make them in order to start the project.
:::

::: {#2edd3fb9-c57f-4858-83d3-056e44a9caff .cell .code execution_count="4"}
``` python
root = os.getcwd()
folders = {
"systematic_review": f"{root}/systematic_review",
    "protocol": f"{root}/systematic_review/protocol",
        "prospero": f"{root}/systematic_review/protocol/prospero",
        "cochrane": f"{root}/systematic_review/protocol/cochrane",
    "search_strategy": f"{root}/systematic_review/search_strategy",
        "search_strategy_pubmed": f"{root}/systematic_review/search_strategy/pubmed/",
        "search_strategy_embase": f"{root}/systematic_review/search_strategy/embase/",
        "search_strategy_wos": f"{root}/systematic_review/search_strategy/wos/",
    "search": f"{root}/systematic_review/search",
        "search_pubmed": f"{root}/systematic_review/search/pubmed/",
        "search_embase": f"{root}/systematic_review/search/embase/",
        "search_wos": f"{root}/systematic_review/search/wos/",
    "deduplication": f"{root}/systematic_review/deduplication/",
    "screening": f"{root}/systematic_review/screening/",
        "title_abstract": f"{root}/systematic_review/screening/title_abstract_screening", 
        "pdf": f"{root}/systematic_review/screening/PDF",
        "full_text": f"{root}/systematic_review/screening/full_text_screening", 
"meta-analysis": f"{root}/meta-analysis",
"manuscript": f"{root}/manuscript",    

}

for var, f in folders.items():
    directory = Path(f)
    globals()[f"{var}"] = directory
    os.makedirs(directory, exist_ok = True)
```
:::

::: {#9be6a593-9d7d-4e2a-8575-75bba8868349 .cell .markdown}
[top](#toc) \| [next](#search)\
[search strategy](#search-strategy) \| [search](#search) \|
[deduplication](#deduplication) \| [screening](#screening)

`<a id="search-strategy">`{=html}`</a>`{=html}

<div align="center">
	<font size="5" style="font-family:Times New Roman;font-variant: small-caps;">Search Strategy</font><br>
</div>

------------------------------------------------------------------------
:::

::: {#67f2d17b-cc9a-4159-8dad-2502363d22bc .cell .markdown}
`<a Section_id="here">`{=html}`</a>`{=html}

**Search strategies** were developed for randomized controlled trials:
`pm_bptb.txt`, `pm_ht.txt`, `pm_qt.txt`, `pm_plt.txt`, `pm_at.txt` and
`pm_ta.txt` corresponding to PubMed search strategies for patellar,
hamstring, quadriceps, peroneus longus, achilles and tibialis anterior
and posterior tendones, respectively. From the protocol that was
developed, extract key terms from the eligibility criteria for inclusion
and exclusion of studies in order to develop a *search strategy*.

The search strategies were \'translated\' via regular expressions from
PubMed syntax to Embase and Web of Science syntax, store them into the
global environment, and save them as plain text files for importing and
use as queries for search.
:::

::: {#26c864f8-342a-4886-9910-9d779f459198 .cell .markdown}

------------------------------------------------------------------------
:::

::: {#f37b080a-394b-4087-8fd4-74173057ca33 .cell .code}
``` python
acl = f"""("anterior cruciate ligament"[mh] OR "anterior cruciate ligament reconstruction"[tiab])"""
rct = f"""("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab])"""
reviews = f"""("review"[pt] OR "review"[tiab] OR "systematic review"[pt] OR "systematic review"[tiab] OR "meta-analysis"[pt] OR "meta-analysis"[tiab])"""
outcomes = f"""("ikdc"[tiab] OR "lysholm"[tiab] OR "tegner"[tiab] OR (("instrumental laxity"[tiab] OR "kt-1000"[tiab] OR "kt-2000"[tiab] OR "rolimeter"[tiab]) OR "pivot shift"[tiab] OR "lachman"[tiab]) OR ("graft failure"[tiab] OR "graft rupture"[tiab]))"""

bptb = f"""("bone-patellar tendon-bone"[tiab] OR "patellar tendon"[tiab] OR "bptb"[tiab])"""
ht = f"""("hamstring tendon"[tiab] OR "semitendinosus"[tiab] OR "gracilis"[tiab])"""
qt = f"""("quadriceps"[tiab] OR "qt"[tiab])"""
plt = f"""("peroneus longus"[tiab] OR "fibularis longus"[tiab])"""
at = f"""("achilles"[tiab])"""
ta = f"""("tibialis anterior"[tiab] OR "tibialis posterior"[tiab])"""

subgroups = {"bptb": bptb, 
             "ht": ht, 
             "qt": qt, 
             "plt": plt, 
             "at": at, 
             "ta": ta}

queries = {}

# Create pm_bptb, etc.
for x, y in subgroups.items():
    globals()[f"pm_{x}"] = f"{acl} AND {rct} AND {y} NOT {reviews}"
    with open(f"{search_strategy}/pubmed/pm_{x}.txt", 'w') as f:
        f.write(f"{acl} AND {rct} AND {y}")
    #globals()[f"reviews_pm_{x}"] = f"{acl} AND {rct} AND {y}"
    with open(f"{search_strategy}/pubmed/reviews_pm_{x}.txt", 'w') as f:
        f.write(f"{acl} AND {reviews} AND {y} AND {outcomes}")

pm_queries = {
    "bptb": pm_bptb,
    "ht": pm_ht,
    "qt": pm_qt,
    "plt": pm_plt,
    "at": pm_at,
    "ta": pm_ta
}

# Create em_bptb, etc.
for x, y in pm_queries.items():
    query = re.sub(r"\[(.*?)\]",":\\1", y)
    query = re.sub(r"\:tiab",":ti,ab", query)
    query = re.sub(r"\:mh","/exp", query)
    query = re.sub(r"\:pt",":it,ti,ab", query)
    query = re.sub(r'"',"'", query)
    globals()[f"em_{x}"] = query
    with open(f"{search_strategy}/embase/em_{x}.txt", 'w') as f:
        f.write(query)

# Create wos_bptb, etc.
for x, y in pm_queries.items():
    query = re.sub(r'"(.*?)"\[(.*?)\]','\\2="\\1"', y)
    query = re.sub(r'tiab="(.*?)"','(TI=(\\1) OR AB=(\\1))', query)
    query = re.sub(r'mh="(.*?)"','(TMIC=(\\1))', query)
    query = re.sub(r'pt="(.*?)"','(TS=(\\1))', query)
    globals()[f"wos_{x}"] = query

    with open(f"{search_strategy}/wos/wos_{x}.txt", 'w') as f:
        f.write(query)
```
:::

:::: {#c87f8e5c-7b36-4ad0-8bf0-0bd897221065 .cell .code execution_count="104"}
``` python
import ipywidgets as widgets
from IPython.display import display, clear_output

entries = []

term_input = widgets.Text(
    placeholder="Search term",
    layout=widgets.Layout(width="75%")
)

field_tag = widgets.Dropdown(
    options=[
        ("MeSH term", "mh"),
        ("Title", "ti"),
        ("Title / Abstract", "tiab"),
        ("Publication Type", "pt"),
    ],
    value="mh",
    layout=widgets.Layout(width="15%")
)

boolean = widgets.Dropdown(
    options=["OR", "AND", "NOT", ""],
    value="",
    layout=widgets.Layout(width="10%")
)

filename_input = widgets.Text(
    placeholder="File name",
    layout=widgets.Layout(width="75%")
)

add_button = widgets.Button(description="Add")
delete_button = widgets.Button(description="Delete")
clear_button = widgets.Button(description="Clear")
save_button = widgets.Button(description="Save")

output = widgets.Output()


def build_query(entries):
    parts = []
    current_or_group = []

    for entry in entries:
        term = entry["term"].strip()
        field = entry["field"]
        op = entry["boolean"]

        if not term:
            continue

        current_or_group.append(f'"{term}"[{field}]')

        if op == "OR":
            continue

        parts.append("(" + " OR ".join(current_or_group) + ")")
        current_or_group = []

        if op in ("AND", "NOT"):
            parts.append(op)

    if current_or_group:
        parts.append("(" + " OR ".join(current_or_group) + ")")

    return " ".join(parts)


def refresh_output(message=""):
    with output:
        clear_output()
        if message:
            print(message)
            print()

        print("Entries:")
        if entries:
            for i, entry in enumerate(entries, start=1):
                op_label = entry["boolean"] if entry["boolean"] != "" else "END"
                print(f'{i}. "{entry["term"]}" [{entry["field"]}] -> {op_label}')
        else:
            print("[none]")

        print("\nCurrent query:")
        query = build_query(entries)
        print(query if query else "[empty]")


def add_entry(_):
    term = term_input.value.strip()
    field = field_tag.value
    op = boolean.value

    if not term:
        refresh_output("Please enter a term.")
        return

    entries.append({
        "term": term,
        "field": field,
        "boolean": op
    })

    term_input.value = ""
    refresh_output(f'Added: "{term}"[{field}] -> {op if op else "END"}')


def delete_last_entry(_):
    if not entries:
        refresh_output("Nothing to delete.")
        return

    removed = entries.pop()
    refresh_output(
        f'Removed: "{removed["term"]}"[{removed["field"]}] -> {removed["boolean"] if removed["boolean"] else "END"}'
    )


def clear_all_entries(_):
    entries.clear()
    refresh_output("Cleared all entries.")


def save_query(_):
    query = build_query(entries)
    filename = filename_input.value.strip() or "default_strategy"
    filepath = f"{filename}.txt"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(query)

    refresh_output(f"Saved query to {filepath}")


add_button.on_click(add_entry)
delete_button.on_click(delete_last_entry)
clear_button.on_click(clear_all_entries)
save_button.on_click(save_query)

entry_row = widgets.HBox(
    [term_input, field_tag, boolean],
    layout=widgets.Layout(align_items="center", gap="10px")
)

controls = widgets.VBox([
    filename_input,
    entry_row,
    widgets.HBox([add_button, delete_button, clear_button, save_button]),
    output
])
display(controls)
refresh_output("Ready.")
```

::: {.output .display_data}
``` json
{"model_id":"825bfabe1d2d437e97552bd5664fc70d","version_major":2,"version_minor":0}
```
:::
::::

::: {#12c1ca76 .cell .markdown}
<form method="POST" action="/submit">
    <label for="term" align="left" style="font-family:Times New Roman;"></label>
    <input type="text" id="term" name="term" style="width:50%"></input> 
    <select id="field_tag" name="field_tag" width="50%" style="font-family:Times New Roman;">
        <option value = "[mh]">MeSH term</option>
        <option value = "[ti]">Title</option>
        <option value = "[tiab]">Title / Abstract</option>
        <option value = "[pt]">Publication Type</option>
    </select> 
    <select id="boolean" name="boolean" width="20%" style="font-family:Times New Roman;"> 
        <option value="OR">OR</option> 
        <option value="AND">AND</option> 
        <option value="NOT">NOT</option> 
    </select> 
    <button type="submit" style="font-family:Times New Roman;">Add </button>
</div>
</form>
:::

:::: {#68c55cc5-c650-4c16-91fe-fd246c2afaa2 .cell .code execution_count="106"}
``` python
filename = input("Enter the file name of the search strategy: ")
file = f"{search_strategy}/pubmed/{filename}.txt"

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
```

::: {.output .stream .stdin}
    Enter the file name of the search strategy:  
    Enter the search string:  
    Enter the field type:  
    Enter the Boolean operator (e.g., OR, AND, NOT):  
:::
::::

::: {#d8fea9ab-4fbc-4357-b3fa-9777c1b5b977 .cell .markdown}
[previous](#search-strategy) \| [top](#toc) \| [next](#deduplication)\
[search strategy](#search-strategy) \| [search](#search) \|
[deduplication](#deduplication) \| [screening](#screening)

`<a id="search">`{=html}`</a>`{=html} `<div align="center">`{=html}
`<font size="5" style="font-family:Times New Roman;font-variant: small-caps;">`{=html}Search`</font>`{=html}`<br>`{=html}
`</div>`{=html}

------------------------------------------------------------------------
:::

::: {#2a081847-333d-47ed-bdcc-3fbdbd45b078 .cell .markdown}
A script to either create a search strategy using the terms, field tags,
and Boolean operators and save them as plain text files or load already
written and saved plain text files for import into the API search
scripts. This uses the search strategies (e.g., `pm_bptb.txt`, search
strategy in plain text written in PubMed syntax for bone-patellar
tendon-bone (BPTB) subgroup search) and pulls data from PubMed to output
PMIDs (`pmid_pm_bptb.txt`) and search results in XML (`pm_bptb.xml`) and
parses this into CSV files (`pm_bptb.csv`).
:::

::::: {#1fda7696-1363-48ba-8834-abf37cf86cb9 .cell .code execution_count="11" slideshow="{\"slide_type\":\"\"}" tags="[]"}
``` python
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
globals()[f"{filename}"] = df
csv_file = f"{search}/pubmed/{filename}.csv"
df.to_csv(csv_file, encoding = "utf-8")
num = len(df)
print(f"Number of records found: {num}")
data.info()
```

::: {.output .stream .stdin}
    Do you already have a search strategy file saved? yes
    Enter the file name of the search strategy:  pm_ta
:::

::: {.output .stream .stdout}
    Number of records found: 9
    <class 'pandas.DataFrame'>
    RangeIndex: 9 entries, 0 to 8
    Data columns (total 41 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   PMID    9 non-null      str   
     1   OWN     9 non-null      str   
     2   STAT    9 non-null      str   
     3   LR      9 non-null      str   
     4   IS      9 non-null      str   
     5   DP      9 non-null      str   
     6   TI      9 non-null      str   
     7   LID     8 non-null      str   
     8   AB      9 non-null      str   
     9   CI      7 non-null      object
     10  FAU     9 non-null      object
     11  AU      9 non-null      object
     12  AD      9 non-null      object
     13  LA      9 non-null      object
     14  GR      2 non-null      object
     15  PT      9 non-null      object
     16  DEP     8 non-null      str   
     17  PL      9 non-null      str   
     18  TA      9 non-null      str   
     19  JT      9 non-null      str   
     20  JID     9 non-null      str   
     21  SB      8 non-null      str   
     22  OTO     5 non-null      object
     23  OT      5 non-null      object
     24  COIS    4 non-null      object
     25  EDAT    9 non-null      str   
     26  MHDA    9 non-null      str   
     27  CRDT    9 non-null      object
     28  PHST    9 non-null      object
     29  AID     8 non-null      object
     30  PST     9 non-null      str   
     31  SO      9 non-null      str   
     32  DCOM    7 non-null      str   
     33  VI      8 non-null      str   
     34  PG      8 non-null      str   
     35  MH      7 non-null      object
     36  PMC     3 non-null      str   
     37  MID     1 non-null      object
     38  PMCR    3 non-null      object
     39  AUID    1 non-null      object
     40  IP      6 non-null      str   
    dtypes: object(17), str(24)
    memory usage: 3.0+ KB
:::
:::::

::: {#2874372b-6f87-482f-9b32-4b1cdf673499 .cell .markdown}
The CSV files from the three databases were now cleaned, prepared, and
transformed; this is otherwise known as \'data wrangling\' in Data
Science.

Step 1: import the csv files and read them into the global environment
for each subgroup and concat them into one dataframe per database.\
Step 2: rename the columns for each dataframe.\
Step 3: write them as csv files into the appropriate directory.
:::

::: {#820fad24-3a40-4d2d-9cc3-69f2f40a1c96 .cell .markdown}
``` mermaid
---
config:
  theme: light
  curve: step
---

flowchart TD

A1["pm_bptb"]
B1["pm_ht"]
C1["pm_qt"]
D1["pm_plt"]
E1["pm_at"]
F1["pm_ta"]

A2["em_bptb"]
B2["em_ht"]
C2["em_qt"]
D2["em_plt"]
E2["em_at"]
F2["em_ta"]

A3["wos_bptb"]
B3["wos_ht"]
C3["wos_qt"]
D3["wos_plt"]
E3["wos_at"]
F3["wos_ta"]

G["pubmed"]
H["embase"]
I["wos"]

A1 & B1 & C1 & D1 & E1 & F1 --> G
A2 & B2 & C2 & D2 & E2 & F2 --> H
A3 & B3 & C3 & D3 & E3 & F3 --> I

G & H & I --> J["records"]
```
:::

::: {#636d0011-31ef-4fb2-a8ad-fc642240ca0b .cell .code execution_count="17" scrolled="true"}
``` python
# import the exported csv files into the global environment
# convert Web of Science exports to csv

import pandas as pd

subgroups = {
    "bptb": "patellar",
    "ht": "hamstring",
    "qt": "quadriceps",
    "plt": "peroneus",
    "at": "achilles",
    "ta": "tibialis"}

# For web of science, there is no CSV export option (go figure), so TSV files were converted in CSV files.
for x, y in subgroups.items():
    df = pd.read_csv(f"{search}/wos/tsv/wos_{x}.tsv", sep = '\t', encoding = "latin-1")
    df.to_csv(f"{search}/wos/wos_{x}.csv", encoding = "utf-8", sep = ",", index = False)
    globals()[f"wos_{x}"] = df
    
import pandas as pd 
search = f"./systematic_review/search"

databases = {"pm": "pubmed", 
             "em": "embase", 
             "wos": "wos"}

subgroups = {"bptb": "patellar", 
             "ht": "hamstring", 
             "qt": "quadriceps", 
             "plt": "peroneus", 
             "at": "achilles", 
             "ta": "tibialis"}

# Step 1
for a, b in databases.items():
    dfs = []
    for x, y in subgroups.items():
        df = pd.read_csv(f"{search}/{b}/{a}_{x}.csv", encoding = "utf-8")
        df['source'] = b
        df['subgroup'] = x
        dfs.append(df)
        globals()[f"{a}_{x}"] = df
        data = pd.concat(dfs, ignore_index = True)
        data.insert(0, "id", range(1, len(data) + 1))
        data.to_csv(f"{search}/{b}/{b}.csv", encoding = "utf-8", index = False)
        globals()[f"{b}"] = data

databases = {"pm": "pubmed", 
             "em": "embase", 
             "wos": "wos"}

subgroups = {"bptb": "patellar", 
             "ht": "hamstring", 
             "qt": "quadriceps", 
             "plt": "peroneus", 
             "at": "achilles", 
             "ta": "tibialis"}

# Step 2: Rename columns
embase.rename(columns = {
	"Title" : "title",
	"Original Title" : "original_title",
	"Author Names" : "authors",
	"Author Addresses" : "author_addresses",
	"Correspondence Address" : "correspondence_address",
	"Editors" : "editors",
	"AiP/IP Entry Date" : "aip/ip_entry_date",
	"Full Record Entry Date" : "full_record_entry_date",
	"Source" : "journal_full",
	"Source title" : "journal",
	"Publication Year" : "year",
	"Volume" : "volume",
	"Issue" : "issue",
	"First Page" : "first_page",
	"Last Page" : "last_page",
	"Date of Publication" : "date",
	"Publication Type" : "study_design",
	"Conference Name" : "conference_name",
	"Conference Location" : "conference_location",
	"Conference Date" : "conference_date",
	"Conference Editors" : "conference_editors",
	"ISSN" : "issn",
	"ISBN" : "isbn",
	"Name" : "name",
	"Location" : "location",
	"Date" : "date",
	"Editors" : "editors",
	"Book Publisher" : "book_publisher",
	"Abstract" : "abstract",
	"Original Abstract" : "original_abstract",
	"Author Keywords" : "author_keywords",
	"Emtree Drug Index Terms (Major Focus)" : "emtree_drug_index_terms_(major_focus)",
	"Emtree Drug Index Terms" : "emtree_drug_index_terms",
	"Emtree Medical Index Terms (Major Focus)" : "emtree_medical_index_terms_(major_focus)",
	"Emtree Medical Index Terms" : "emtree_medical_index_terms",
	"Drug Tradenames" : "drug_tradenames",
	"Drug Manufacturer" : "drug_manufacturer",
	"Device Tradenames" : "device_tradenames",
	"Device Manufacturer" : "device_manufacturer",
	"CAS Registry Numbers" : "cas_registry_numbers",
	"Molecular Sequence Numbers" : "molecular_sequence_numbers",
	"Embase Classification" : "embase_classification",
	"Clinical Trial Numbers" : "clinical_trial_numbers",
	"Article Language" : "language",
	"Summary Language" : "summary_language",
	"Embase Accession ID" : "embase_accession_id",
	"Medline PMID" : "pmid",
	"PUI" : "pui",
	"DOI" : "doi",
	"Full Text Link" : "full_text_link",
	"Embase Link" : "embase_link",
	"Open IJRL Link" : "open_ijrl_link",
	"Copyright" : "copyright",
	"source" : "source",
	"subgroup" : "subgroup"
}, inplace = True)

pubmed.rename(columns = {
	"id" : "id",
	"pmid" : "pmid",
	"PubDate" : "date",
	"EPubDate" : "epubdate",
	"Source" : "journal_abbr",
	"AuthorList" : "authors",
	"LastAuthor" : "last_author",
	"Title" : "title",
	"Volume" : "volume",
	"Issue" : "issue",
	"Pages" : "pages",
	"LangList" : "language",
	"NlmUniqueID" : "nlmuniqueid",
	"ISSN" : "issn",
	"ESSN" : "essn",
	"PubTypeList" : "study_design",
	"RecordStatus" : "recordstatus",
	"PubStatus" : "pubstatus",
	"Articlelds" : "articlelds",
	"DOI" : "doi",
	"History" : "history",
	"References" : "references",
	"HasAbstract" : "hasabstract",
	"PmcRefCount" : "pmcrefcount",
	"FullJournalName" : "journal",
	"ELocationID" : "elocationid",
	"SO" : "so",
	"abstract" : "abstract",
	"source" : "source",
	"subgroup" : "subgroup"
}, inplace = True)

wos.rename(columns = {
    "id": "id",
	"ï»¿PT" : "study_design",
	"AU" : "authors",
	"BA" : "book_authors",
	"BE" : "book_editors",
	"GP" : "book_group_authors",
	"AF" : "authors_full",
	"BF" : "book_author_full_names",
	"CA" : "group_authors",
	"TI" : "title",
	"SO" : "journal",
	"SE" : "book_series_title",
	"BS" : "book_series_subtitle",
	"LA" : "language",
	"DT" : "document_type",
	"CT" : "conference_title",
	"CY" : "conference_date",
	"CL" : "conference_location",
	"SP" : "conference_sponsor",
	"HO" : "conference_host",
	"DE" : "author_keywords",
	"ID" : "keywords_plus",
	"AB" : "abstract",
	"C1" : "addresses",
	"C3" : "affiliations",
	"RP" : "reprint_addresses",
	"EM" : "email_addresses",
	"RI" : "researcher_ids",
	"OI" : "orcids",
	"FU" : "funding_orgs",
	"FP" : "funding_name_preferred",
	"FX" : "funding_text",
	"CR" : "cited_references",
	"NR" : "cited_reference_count",
	"TC" : "times_cited, wos_core",
	"Z9" : "times_cited, all_databases",
	"U1" : "180_day_usage_count",
	"U2" : "since_2013_usage_count",
	"PU" : "publisher",
	"PI" : "publisher_city",
	"PA" : "publisher_address",
	"SN" : "issn",
	"EI" : "eissn",
	"BN" : "isbn",
	"J9" : "journal_9",
	"JI" : "journal_abbr",
	"PD" : "date",
	"PY" : "year",
	"VL" : "volume",
	"IS" : "issue",
	"PN" : "part_number",
	"SU" : "supplement",
	"SI" : "special_issue",
	"MA" : "meeting_abstract",
	"BP" : "start_page",
	"EP" : "end_page",
	"AR" : "article_number",
	"DI" : "doi",
	"DL" : "doi_link",
	"D2" : "book_doi",
	"EA" : "early_access_date",
	"PG" : "number_of_pages",
	"WC" : "wos_categories",
	"WE" : "web_of_science_index",
	"SC" : "research_areas",
	"GA" : "ids_number",
	"PM" : "pmid",
	"OA" : "open_access_designations",
	"HC" : "highly_cited_status",
	"HP" : "hot_paper_status",
	"DA" : "date_of_export",
	"UT" : "ut (unique_wos_id)",
	"source" : "source",
    "subgroup": "subgroup"
}, inplace = True)

# Step 3: write the CSV files
pubmed.to_csv(f"{search}/pubmed.csv", encoding = "utf-8")
embase.to_csv(f"{search}/embase.csv", encoding = "utf-8")
wos.to_csv(f"{search}/wos.csv", encoding = "latin-1")
```
:::

::: {#24d92b75-3253-4a8c-9f78-0b04e7ba9813 .cell .code execution_count="18" scrolled="true"}
``` python
databases = {
    'pubmed': pubmed, 
    'embase': embase,
    'wos': wos
}

for text, var in databases.items():
    df = pd.DataFrame({
        "id": var["id"],
        "pmid": var["pmid"],
        "source": var["source"],
        "subgroup": var["subgroup"],
        "doi": var["doi"],
        "authors": var["authors"],
        "journal": var["journal"],
        "title": var["title"],
        "abstract": var["abstract"],
        "year": var["year"],
        "language": var["language"]
    })
    df['pmid'] = round(df['pmid'],0)
    df['pmid'] = df['pmid'].astype(str)
    df['language'] = df['language'].str.replace(r"[\'\[\]]","", regex = True)
    globals()[f"{text}"] = df
```
:::

:::: {#fd216fd2-2ab6-43ac-b358-043b69e216e2 .cell .code execution_count="19"}
``` python
wos.info()
```

::: {.output .stream .stdout}
    <class 'pandas.DataFrame'>
    RangeIndex: 531 entries, 0 to 530
    Data columns (total 11 columns):
     #   Column    Non-Null Count  Dtype
    ---  ------    --------------  -----
     0   id        531 non-null    int64
     1   pmid      516 non-null    str  
     2   source    531 non-null    str  
     3   subgroup  531 non-null    str  
     4   doi       524 non-null    str  
     5   authors   531 non-null    str  
     6   journal   531 non-null    str  
     7   title     531 non-null    str  
     8   abstract  521 non-null    str  
     9   year      531 non-null    int64
     10  language  531 non-null    str  
    dtypes: int64(2), str(9)
    memory usage: 45.8 KB
:::
::::

::: {#aac9bb35-f65a-40a3-9f7c-fb96c8c6c638 .cell .code execution_count="20"}
``` python

wos['authors'] = wos['authors'].str.replace(r"[\'\[\].,]","", regex = True)
wos['authors'] = wos['authors'].str.replace(r";",",", regex = True)
```
:::

:::: {#bfb89528-6aaf-4669-8087-a24896b6f1e7 .cell .code execution_count="21"}
``` python
pubmed['authors'] = pubmed['authors'].str.replace(r"[\'\[\]]","", regex = True)
pubmed['journal'] = pubmed['journal'].str.replace(r"[\'\[,\]]","", regex = True)
pubmed['journal'] = pubmed['journal'].str.replace(r"\(.*?\)","", regex=True)
pubmed['journal'] = pubmed['journal'].str.capitalize()
pubmed.head()
```

::: {.output .execute_result execution_count="21"}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>pmid</th>
      <th>source</th>
      <th>subgroup</th>
      <th>doi</th>
      <th>authors</th>
      <th>journal</th>
      <th>title</th>
      <th>abstract</th>
      <th>year</th>
      <th>language</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>41562143</td>
      <td>pubmed</td>
      <td>bptb</td>
      <td>10.1002/ksa.70275</td>
      <td>Vendrig T, Keizer MNJ, Brouwer RW, Houdijk H, ...</td>
      <td>Knee surgery sports traumatology arthroscopy :...</td>
      <td>Similar dynamic tibiofemoral movements during ...</td>
      <td>PURPOSE: Dynamic tibiofemoral movements follow...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>41536854</td>
      <td>pubmed</td>
      <td>bptb</td>
      <td>10.1016/j.lanepe.2025.101561</td>
      <td>Sonnery-Cottet B, Carrozzo A, Poilvache H, Fay...</td>
      <td>The lancet regional health. europe</td>
      <td>Anterior cruciate ligament reconstruction comb...</td>
      <td>BACKGROUND: Anterior Cruciate Ligament (ACL) r...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>41522461</td>
      <td>pubmed</td>
      <td>bptb</td>
      <td>10.1177/23259671251401596</td>
      <td>Johns WL, Voskeridjian A, Miltenberg B, Muchin...</td>
      <td>Orthopaedic journal of sports medicine</td>
      <td>Regional Anesthesia Utilizing Liposomal Bupiva...</td>
      <td>BACKGROUND: Perioperative nerve blocks are com...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>40308075</td>
      <td>pubmed</td>
      <td>bptb</td>
      <td>10.1177/03635465251328609</td>
      <td>Rao N, Triana J, Avila A, Campbell KA, Alaia M...</td>
      <td>The american journal of sports medicine</td>
      <td>Postoperative Pain and Opioid Usage With Combi...</td>
      <td>BACKGROUND: Efforts to decrease pain, improve ...</td>
      <td>2025</td>
      <td>English</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>39886263</td>
      <td>pubmed</td>
      <td>bptb</td>
      <td>10.1177/23259671241302348</td>
      <td>Lucidi GA, Agostinone P, Di Paolo S, Dal Fabbr...</td>
      <td>Orthopaedic journal of sports medicine</td>
      <td>Long-term Outcomes After Anterior Cruciate Lig...</td>
      <td>BACKGROUND: In recent years, lateral extra-art...</td>
      <td>2025</td>
      <td>English</td>
    </tr>
  </tbody>
</table>
</div>
:::
::::

::::: {#65103fb4-0ddb-4cb0-be7f-fd827eff2e71 .cell .code execution_count="22"}
``` python
embase['authors'] = embase['authors'].dropna()
embase['authors'] = embase['authors'].fillna("")
embase['doi'] = embase['doi'].fillna("")
embase['pmid'] = embase['pmid'].fillna("")
embase['pmid'] = round(embase['pmid'],0)
embase['pmid'] = embase['pmid'].astype(str).replace(r"\.0","",regex=True)
embase['authors'] = embase['authors'].str.replace(r"[\'\[\].]","", regex = True)
pubmed['journal'] = pubmed['journal'].str.replace(r"\(.*?\)","", regex=True)
embase['journal'] = embase['journal'].str.replace(r"[\'\[,\]]","", regex = True)
embase['journal'] = embase['journal'].str.capitalize()

embase.info()
embase.head()
```

::: {.output .stream .stdout}
    <class 'pandas.DataFrame'>
    RangeIndex: 317 entries, 0 to 316
    Data columns (total 11 columns):
     #   Column    Non-Null Count  Dtype
    ---  ------    --------------  -----
     0   id        317 non-null    int64
     1   pmid      317 non-null    str  
     2   source    317 non-null    str  
     3   subgroup  317 non-null    str  
     4   doi       317 non-null    str  
     5   authors   317 non-null    str  
     6   journal   317 non-null    str  
     7   title     317 non-null    str  
     8   abstract  315 non-null    str  
     9   year      317 non-null    int64
     10  language  317 non-null    str  
    dtypes: int64(2), str(9)
    memory usage: 27.4 KB
:::

::: {.output .execute_result execution_count="22"}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>pmid</th>
      <th>source</th>
      <th>subgroup</th>
      <th>doi</th>
      <th>authors</th>
      <th>journal</th>
      <th>title</th>
      <th>abstract</th>
      <th>year</th>
      <th>language</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>41562143</td>
      <td>embase</td>
      <td>bptb</td>
      <td>10.1002/ksa.70275</td>
      <td>Vendrig T, Keizer MNJ, Brouwer RW, Houdijk H, ...</td>
      <td>Knee surgery sports traumatology arthroscopy :...</td>
      <td>Similar dynamic tibiofemoral movements during ...</td>
      <td>PURPOSE: Dynamic tibiofemoral movements follow...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td></td>
      <td>embase</td>
      <td>bptb</td>
      <td>10.1177/23259671251401596</td>
      <td>Johns WL, Voskeridjian A, Miltenberg B, Muchin...</td>
      <td>Orthopaedic journal of sports medicine</td>
      <td>Regional Anesthesia Utilizing Liposomal Bupiva...</td>
      <td>Background: Perioperative nerve blocks are com...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td></td>
      <td>embase</td>
      <td>bptb</td>
      <td></td>
      <td></td>
      <td>Clinicaltrials.gov</td>
      <td>Extended Post-Operative Oral Tranexamic Acid D...</td>
      <td>Brief SummaryThis is a prospective, multi-cent...</td>
      <td>2025</td>
      <td>English</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>40308075</td>
      <td>embase</td>
      <td>bptb</td>
      <td>10.1177/03635465251328609</td>
      <td>Rao N, Triana J, Avila A, Campbell KA, Alaia M...</td>
      <td>The american journal of sports medicine</td>
      <td>Postoperative Pain and Opioid Usage With Combi...</td>
      <td>BACKGROUND: Efforts to decrease pain, improve ...</td>
      <td>2025</td>
      <td>English</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td></td>
      <td>embase</td>
      <td>bptb</td>
      <td>10.1177/2325967125S00004</td>
      <td>Miltenberg B, Voskeridjian A, Dodson C, Ciccot...</td>
      <td>Orthopaedic journal of sports medicine</td>
      <td>Liposomal Bupivacaine-Based Regional Anesthesi...</td>
      <td>Objectives: Femoral nerve blockade (FNB), addu...</td>
      <td>2025</td>
      <td>English</td>
    </tr>
  </tbody>
</table>
</div>
:::
:::::

:::: {#3f12c27e-b6c8-4f68-9464-9b9060dcab28 .cell .code execution_count="23"}
``` python
wos['journal'] = wos['journal'].str.replace(r"[\'\[,\]]","", regex = True)
wos['journal'] = wos['journal'].str.capitalize()
wos.head()
```

::: {.output .execute_result execution_count="23"}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>pmid</th>
      <th>source</th>
      <th>subgroup</th>
      <th>doi</th>
      <th>authors</th>
      <th>journal</th>
      <th>title</th>
      <th>abstract</th>
      <th>year</th>
      <th>language</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>41758993.0</td>
      <td>wos</td>
      <td>bptb</td>
      <td>10.1002/ksa.70354</td>
      <td>Boer BC, Brouwer RW, Heuvel JO, de Vries AJ, v...</td>
      <td>Knee surgery sports traumatology arthroscopy</td>
      <td>Quadriceps tendon autograft is not inferior to...</td>
      <td>Purpose: To evaluate the effectiveness of quad...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>41733021.0</td>
      <td>wos</td>
      <td>bptb</td>
      <td>10.1177/03635465261415842</td>
      <td>Petit CB, Hussain ZB, Read PJ, Mcpherson AL, P...</td>
      <td>American journal of sports medicine</td>
      <td>Graft Failure Rates in Bone-Patellar Tendon-Bo...</td>
      <td>Background: Anterior cruciate ligament reconst...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>41717284.0</td>
      <td>wos</td>
      <td>bptb</td>
      <td>10.1002/jeo2.70665</td>
      <td>Heinz M, Lettner J, Topkarci YB, KrÃ³likowska ...</td>
      <td>Journal of experimental orthopaedics</td>
      <td>Hamstring autografts favour knee extension str...</td>
      <td>Purpose Quadriceps tendon (QT), hamstring tend...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>41562143.0</td>
      <td>wos</td>
      <td>bptb</td>
      <td>10.1002/ksa.70275</td>
      <td>Vendrig T, Keizer MNJ, Brouwer RW, Houdijk H, ...</td>
      <td>Knee surgery sports traumatology arthroscopy</td>
      <td>Similar dynamic tibiofemoral movements during ...</td>
      <td>Purpose: Dynamic tibiofemoral movements follow...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>41522461.0</td>
      <td>wos</td>
      <td>bptb</td>
      <td>10.1177/23259671251401596</td>
      <td>Johns WL, Voskeridjian A, Miltenberg B, Muchin...</td>
      <td>Orthopaedic journal of sports medicine</td>
      <td>Regional Anesthesia Utilizing Liposomal Bupiva...</td>
      <td>Background: Perioperative nerve blocks are com...</td>
      <td>2026</td>
      <td>English</td>
    </tr>
  </tbody>
</table>
</div>
:::
::::

::: {#a69486a2-b450-4396-85aa-13c42de80855 .cell .markdown}
Finally, create a `records.csv` file, representing the search results of
all database searches.
:::

:::: {#92773818-cb1d-4856-85c1-a636f851cc1b .cell .code execution_count="24" scrolled="true"}
``` python
records = pd.concat([pubmed, embase, wos], ignore_index = True)

records['first_author'] = records['authors'].str.replace(r"[\'\[\],.;]","", regex = True).str.split().str[0]
records['authors'] = records['authors'].str.replace(r"[\'\[\].;]","", regex = True)
records['short_title'] = records['title'].str.replace(r'[\[\]\s,.;-]','',regex = True).str.lower().str[:60]
records['title+author+year'] = records['first_author'] + '+' + records['short_title'] + '+' + records['year'].astype(str)
records['title+year'] = records['short_title'] + '+' + records['year'].astype(str)
records['language'] = records['language'].str.replace(r"[\'\[\]]","", regex = True)
records["pmid"] = pd.to_numeric(records["pmid"], errors="coerce").astype("Int64")
records["subgroup"] = records["subgroup"].str.upper()
records["doi_url"] = f"https://doi.org/" + records["doi"]
records["pmid_url"] = "https://pubmed.ncbi.nlm.nih.gov/" + records["pmid"].astype(str) + "/"
records["study"] = records['first_author'] + " (" + records['year'].astype(str) + ")"
records = records[["id", "study", "subgroup", "authors", "first_author", "title", "short_title", "abstract", "year", "language", "journal", "source", "doi", "doi_url", "pmid", "pmid_url", "title+author+year", "title+year"]]
records.sort_values(by = ['subgroup', 'year', 'authors'])
records.to_csv(f"{search}/records.csv", encoding= "utf-8")
records.to_csv(f"{deduplication}/records.csv", encoding = "utf-8")
records.head(10)
```

::: {.output .execute_result execution_count="24"}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>study</th>
      <th>subgroup</th>
      <th>authors</th>
      <th>first_author</th>
      <th>title</th>
      <th>short_title</th>
      <th>abstract</th>
      <th>year</th>
      <th>language</th>
      <th>journal</th>
      <th>source</th>
      <th>doi</th>
      <th>doi_url</th>
      <th>pmid</th>
      <th>pmid_url</th>
      <th>title+author+year</th>
      <th>title+year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Vendrig (2026)</td>
      <td>BPTB</td>
      <td>Vendrig T, Keizer MNJ, Brouwer RW, Houdijk H, ...</td>
      <td>Vendrig</td>
      <td>Similar dynamic tibiofemoral movements during ...</td>
      <td>similardynamictibiofemoralmovementsduringjumpl...</td>
      <td>PURPOSE: Dynamic tibiofemoral movements follow...</td>
      <td>2026</td>
      <td>English</td>
      <td>Knee surgery sports traumatology arthroscopy :...</td>
      <td>pubmed</td>
      <td>10.1002/ksa.70275</td>
      <td>https://doi.org/10.1002/ksa.70275</td>
      <td>41562143</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/41562143/</td>
      <td>Vendrig+similardynamictibiofemoralmovementsdur...</td>
      <td>similardynamictibiofemoralmovementsduringjumpl...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Sonnery-Cottet (2026)</td>
      <td>BPTB</td>
      <td>Sonnery-Cottet B, Carrozzo A, Poilvache H, Fay...</td>
      <td>Sonnery-Cottet</td>
      <td>Anterior cruciate ligament reconstruction comb...</td>
      <td>anteriorcruciateligamentreconstructioncombined...</td>
      <td>BACKGROUND: Anterior Cruciate Ligament (ACL) r...</td>
      <td>2026</td>
      <td>English</td>
      <td>The lancet regional health. europe</td>
      <td>pubmed</td>
      <td>10.1016/j.lanepe.2025.101561</td>
      <td>https://doi.org/10.1016/j.lanepe.2025.101561</td>
      <td>41536854</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/41536854/</td>
      <td>Sonnery-Cottet+anteriorcruciateligamentreconst...</td>
      <td>anteriorcruciateligamentreconstructioncombined...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Johns (2026)</td>
      <td>BPTB</td>
      <td>Johns WL, Voskeridjian A, Miltenberg B, Muchin...</td>
      <td>Johns</td>
      <td>Regional Anesthesia Utilizing Liposomal Bupiva...</td>
      <td>regionalanesthesiautilizingliposomalbupivacain...</td>
      <td>BACKGROUND: Perioperative nerve blocks are com...</td>
      <td>2026</td>
      <td>English</td>
      <td>Orthopaedic journal of sports medicine</td>
      <td>pubmed</td>
      <td>10.1177/23259671251401596</td>
      <td>https://doi.org/10.1177/23259671251401596</td>
      <td>41522461</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/41522461/</td>
      <td>Johns+regionalanesthesiautilizingliposomalbupi...</td>
      <td>regionalanesthesiautilizingliposomalbupivacain...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Rao (2025)</td>
      <td>BPTB</td>
      <td>Rao N, Triana J, Avila A, Campbell KA, Alaia M...</td>
      <td>Rao</td>
      <td>Postoperative Pain and Opioid Usage With Combi...</td>
      <td>postoperativepainandopioidusagewithcombinedadd...</td>
      <td>BACKGROUND: Efforts to decrease pain, improve ...</td>
      <td>2025</td>
      <td>English</td>
      <td>The american journal of sports medicine</td>
      <td>pubmed</td>
      <td>10.1177/03635465251328609</td>
      <td>https://doi.org/10.1177/03635465251328609</td>
      <td>40308075</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/40308075/</td>
      <td>Rao+postoperativepainandopioidusagewithcombine...</td>
      <td>postoperativepainandopioidusagewithcombinedadd...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Lucidi (2025)</td>
      <td>BPTB</td>
      <td>Lucidi GA, Agostinone P, Di Paolo S, Dal Fabbr...</td>
      <td>Lucidi</td>
      <td>Long-term Outcomes After Anterior Cruciate Lig...</td>
      <td>longtermoutcomesafteranteriorcruciateligamentr...</td>
      <td>BACKGROUND: In recent years, lateral extra-art...</td>
      <td>2025</td>
      <td>English</td>
      <td>Orthopaedic journal of sports medicine</td>
      <td>pubmed</td>
      <td>10.1177/23259671241302348</td>
      <td>https://doi.org/10.1177/23259671241302348</td>
      <td>39886263</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/39886263/</td>
      <td>Lucidi+longtermoutcomesafteranteriorcruciateli...</td>
      <td>longtermoutcomesafteranteriorcruciateligamentr...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Martorell-de (2025)</td>
      <td>BPTB</td>
      <td>Martorell-de Fortuny L, Torres-Claramunt R, Sá...</td>
      <td>Martorell-de</td>
      <td>Patellar bone defect grafting does not reduce ...</td>
      <td>patellarbonedefectgraftingdoesnotreduceanterio...</td>
      <td>PURPOSE: Donor site morbidity is the main draw...</td>
      <td>2025</td>
      <td>English</td>
      <td>Knee surgery sports traumatology arthroscopy :...</td>
      <td>pubmed</td>
      <td>10.1002/ksa.12449</td>
      <td>https://doi.org/10.1002/ksa.12449</td>
      <td>39194385</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/39194385/</td>
      <td>Martorell-de+patellarbonedefectgraftingdoesnot...</td>
      <td>patellarbonedefectgraftingdoesnotreduceanterio...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Martin (2024)</td>
      <td>BPTB</td>
      <td>Martin RK, Marmura H, Wastvedt S, Pareek A, Pe...</td>
      <td>Martin</td>
      <td>External validation of the Norwegian anterior ...</td>
      <td>externalvalidationofthenorwegiananteriorcrucia...</td>
      <td>PURPOSE: A machine learning-based anterior cru...</td>
      <td>2024</td>
      <td>English</td>
      <td>Knee surgery sports traumatology arthroscopy :...</td>
      <td>pubmed</td>
      <td>10.1002/ksa.12031</td>
      <td>https://doi.org/10.1002/ksa.12031</td>
      <td>38226736</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/38226736/</td>
      <td>Martin+externalvalidationofthenorwegiananterio...</td>
      <td>externalvalidationofthenorwegiananteriorcrucia...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Obradović (2023)</td>
      <td>BPTB</td>
      <td>Obradović M, Ninković S, Gvozdenović N, Tošić ...</td>
      <td>Obradović</td>
      <td>Tubularization of Bone-Tendon-Bone Grafts: Eff...</td>
      <td>tubularizationofbonetendonbonegrafts:effectson...</td>
      <td>Background and Objectives: The study addresses...</td>
      <td>2023</td>
      <td>English</td>
      <td>Medicina</td>
      <td>pubmed</td>
      <td>10.3390/medicina59101764</td>
      <td>https://doi.org/10.3390/medicina59101764</td>
      <td>37893482</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/37893482/</td>
      <td>Obradović+tubularizationofbonetendonbonegrafts...</td>
      <td>tubularizationofbonetendonbonegrafts:effectson...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Jack (2023)</td>
      <td>BPTB</td>
      <td>Jack RA 2nd, Lambert BS, Hedt CA, Delgado D, G...</td>
      <td>Jack</td>
      <td>Blood Flow Restriction Therapy Preserves Lower...</td>
      <td>bloodflowrestrictiontherapypreserveslowerextre...</td>
      <td>BACKGROUND: Muscle atrophy is common after an ...</td>
      <td>2023</td>
      <td>English</td>
      <td>Sports health</td>
      <td>pubmed</td>
      <td>10.1177/19417381221101006</td>
      <td>https://doi.org/10.1177/19417381221101006</td>
      <td>35762124</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/35762124/</td>
      <td>Jack+bloodflowrestrictiontherapypreserveslower...</td>
      <td>bloodflowrestrictiontherapypreserveslowerextre...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>de (2022)</td>
      <td>BPTB</td>
      <td>de Souza Borges JH, Oliveira M, Junior PL, de ...</td>
      <td>de</td>
      <td>Is contralateral autogenous patellar tendon gr...</td>
      <td>iscontralateralautogenouspatellartendongraftab...</td>
      <td>AIM: The aim of this study was to compare the ...</td>
      <td>2022</td>
      <td>English</td>
      <td>The knee</td>
      <td>pubmed</td>
      <td>10.1016/j.knee.2022.03.015</td>
      <td>https://doi.org/10.1016/j.knee.2022.03.015</td>
      <td>35468330</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/35468330/</td>
      <td>de+iscontralateralautogenouspatellartendongraf...</td>
      <td>iscontralateralautogenouspatellartendongraftab...</td>
    </tr>
  </tbody>
</table>
</div>
:::
::::

::::: {#eb3bad54-bb36-4ab4-b562-c0294a54a0ce .cell .code execution_count="25"}
``` python
records['year'] = records['year'].astype(str)

records['pmid'] = round(records['pmid'],0)
records['pmid'] = records['pmid'].astype(str)
records['first_author'] = records['first_author'].astype(str)
records['year'] = records['year'].astype(str)
records.rename(columns = {"id":"source_id"}, inplace = True)
records["id"] = range(1,len(records)+1)
records = records[["id", "source_id", "study", "subgroup", "authors", "first_author", "title", "short_title", "abstract", "year", "language", "journal", "source", "doi", "doi_url", "pmid", "pmid_url",  "title+author+year", "title+year"]]
records[records['source']=='embase'].head()
records.info()
records.head()
```

::: {.output .stream .stdout}
    <class 'pandas.DataFrame'>
    RangeIndex: 1483 entries, 0 to 1482
    Data columns (total 19 columns):
     #   Column             Non-Null Count  Dtype
    ---  ------             --------------  -----
     0   id                 1483 non-null   int64
     1   source_id          1483 non-null   int64
     2   study              1394 non-null   str  
     3   subgroup           1483 non-null   str  
     4   authors            1483 non-null   str  
     5   first_author       1394 non-null   str  
     6   title              1483 non-null   str  
     7   short_title        1483 non-null   str  
     8   abstract           1468 non-null   str  
     9   year               1483 non-null   str  
     10  language           1483 non-null   str  
     11  journal            1483 non-null   str  
     12  source             1483 non-null   str  
     13  doi                1428 non-null   str  
     14  doi_url            1428 non-null   str  
     15  pmid               1322 non-null   str  
     16  pmid_url           1322 non-null   str  
     17  title+author+year  1394 non-null   str  
     18  title+year         1483 non-null   str  
    dtypes: int64(2), str(17)
    memory usage: 220.3 KB
:::

::: {.output .execute_result execution_count="25"}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>source_id</th>
      <th>study</th>
      <th>subgroup</th>
      <th>authors</th>
      <th>first_author</th>
      <th>title</th>
      <th>short_title</th>
      <th>abstract</th>
      <th>year</th>
      <th>language</th>
      <th>journal</th>
      <th>source</th>
      <th>doi</th>
      <th>doi_url</th>
      <th>pmid</th>
      <th>pmid_url</th>
      <th>title+author+year</th>
      <th>title+year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>Vendrig (2026)</td>
      <td>BPTB</td>
      <td>Vendrig T, Keizer MNJ, Brouwer RW, Houdijk H, ...</td>
      <td>Vendrig</td>
      <td>Similar dynamic tibiofemoral movements during ...</td>
      <td>similardynamictibiofemoralmovementsduringjumpl...</td>
      <td>PURPOSE: Dynamic tibiofemoral movements follow...</td>
      <td>2026</td>
      <td>English</td>
      <td>Knee surgery sports traumatology arthroscopy :...</td>
      <td>pubmed</td>
      <td>10.1002/ksa.70275</td>
      <td>https://doi.org/10.1002/ksa.70275</td>
      <td>41562143</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/41562143/</td>
      <td>Vendrig+similardynamictibiofemoralmovementsdur...</td>
      <td>similardynamictibiofemoralmovementsduringjumpl...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2</td>
      <td>Sonnery-Cottet (2026)</td>
      <td>BPTB</td>
      <td>Sonnery-Cottet B, Carrozzo A, Poilvache H, Fay...</td>
      <td>Sonnery-Cottet</td>
      <td>Anterior cruciate ligament reconstruction comb...</td>
      <td>anteriorcruciateligamentreconstructioncombined...</td>
      <td>BACKGROUND: Anterior Cruciate Ligament (ACL) r...</td>
      <td>2026</td>
      <td>English</td>
      <td>The lancet regional health. europe</td>
      <td>pubmed</td>
      <td>10.1016/j.lanepe.2025.101561</td>
      <td>https://doi.org/10.1016/j.lanepe.2025.101561</td>
      <td>41536854</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/41536854/</td>
      <td>Sonnery-Cottet+anteriorcruciateligamentreconst...</td>
      <td>anteriorcruciateligamentreconstructioncombined...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
      <td>Johns (2026)</td>
      <td>BPTB</td>
      <td>Johns WL, Voskeridjian A, Miltenberg B, Muchin...</td>
      <td>Johns</td>
      <td>Regional Anesthesia Utilizing Liposomal Bupiva...</td>
      <td>regionalanesthesiautilizingliposomalbupivacain...</td>
      <td>BACKGROUND: Perioperative nerve blocks are com...</td>
      <td>2026</td>
      <td>English</td>
      <td>Orthopaedic journal of sports medicine</td>
      <td>pubmed</td>
      <td>10.1177/23259671251401596</td>
      <td>https://doi.org/10.1177/23259671251401596</td>
      <td>41522461</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/41522461/</td>
      <td>Johns+regionalanesthesiautilizingliposomalbupi...</td>
      <td>regionalanesthesiautilizingliposomalbupivacain...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
      <td>Rao (2025)</td>
      <td>BPTB</td>
      <td>Rao N, Triana J, Avila A, Campbell KA, Alaia M...</td>
      <td>Rao</td>
      <td>Postoperative Pain and Opioid Usage With Combi...</td>
      <td>postoperativepainandopioidusagewithcombinedadd...</td>
      <td>BACKGROUND: Efforts to decrease pain, improve ...</td>
      <td>2025</td>
      <td>English</td>
      <td>The american journal of sports medicine</td>
      <td>pubmed</td>
      <td>10.1177/03635465251328609</td>
      <td>https://doi.org/10.1177/03635465251328609</td>
      <td>40308075</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/40308075/</td>
      <td>Rao+postoperativepainandopioidusagewithcombine...</td>
      <td>postoperativepainandopioidusagewithcombinedadd...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>5</td>
      <td>Lucidi (2025)</td>
      <td>BPTB</td>
      <td>Lucidi GA, Agostinone P, Di Paolo S, Dal Fabbr...</td>
      <td>Lucidi</td>
      <td>Long-term Outcomes After Anterior Cruciate Lig...</td>
      <td>longtermoutcomesafteranteriorcruciateligamentr...</td>
      <td>BACKGROUND: In recent years, lateral extra-art...</td>
      <td>2025</td>
      <td>English</td>
      <td>Orthopaedic journal of sports medicine</td>
      <td>pubmed</td>
      <td>10.1177/23259671241302348</td>
      <td>https://doi.org/10.1177/23259671241302348</td>
      <td>39886263</td>
      <td>https://pubmed.ncbi.nlm.nih.gov/39886263/</td>
      <td>Lucidi+longtermoutcomesafteranteriorcruciateli...</td>
      <td>longtermoutcomesafteranteriorcruciateligamentr...</td>
    </tr>
  </tbody>
</table>
</div>
:::
:::::

::: {#ab86ea52-5c9b-4162-94d8-7cedb5c1a931 .cell .markdown}
[previous](#search) \| [top](#toc) \| [next](#screening)\
[search strategy](#search-strategy) \| [search](#search) \|
[deduplication](#deduplication) \| [screening](#screening)

`<a id="deduplication">`{=html}`</a>`{=html}
`<div align="center">`{=html}
`<font size="5" style="font-family:Times New Roman;font-variant: small-caps;">`{=html}Deduplication`</font>`{=html}`<br>`{=html}
`</div>`{=html}
:::

::: {#e46b858e-9906-4721-9652-ac052cde0457 .cell .markdown}
input file(s): `records.csv`, output file(s): `doi_deduplicated.csv`,
`pmid_deduplicated.csv`, \`key_de
:::

::::: {#c5865181-766d-478a-8a8d-81d5a275c3ed .cell .code execution_count="30"}
``` python
import pandas as pd
import mermaid
import os

input_file_name = f"{deduplication}/" + input('Enter file name: ') + '.csv'
df = pd.read_csv(input_file_name) # A (records)
cols_input = input('Enter the column for which to deduplicate based on: ')
cols = [c.strip() for c in cols_input.split(',')]
folder = '_'.join(cols)
os.makedirs(f"{deduplication}/{folder}/", exist_ok = True)

output_file = f"{deduplication}/{folder}/{folder}_deduplicated"
output_file_name = f"{output_file}.csv"
output_for_recycle = f"{deduplication}/{folder}_deduplicated.csv"
prisma_file_name = f"{output_file}.mmd"

nulls_mask = df[cols].isnull().any(axis=1)
df_nulls = df[nulls_mask] # B
df_non_nulls = df[~nulls_mask] # C

duplicates_mask = df_non_nulls.duplicated(subset = cols, keep = False)
df_non_duplicates = df_non_nulls[~duplicates_mask] # D
df_duplicates = df_non_nulls[duplicates_mask] # E
#df_duplicates.groupby(cols, as_index=False).agg(agg_map)
df_kept = df_duplicates.drop_duplicates(subset = cols, keep = 'first')
#df_kept = df_duplicates.groupby(cols, as_index=False).agg(lambda s: list(dict.fromkeys(s.dropna())) if s.name in ['subgroup', 'source'] else s.dropna().iloc[0] if len(s.dropna()) else pd.NA)
#df_kept = df_duplicates.groupby(cols, as_index=False).agg(lambda s: list(dict.fromkeys(s.dropna())) if s.name == 'subgroup' else s.dropna().iloc[0] if len(s.dropna()) else pd.NA)
df_removed = df_duplicates[~df_duplicates.index.isin(df_kept.index)]
#df_kept = df_duplicates.groupby(cols, as_index=False).agg(lambda s: '; '.join(dict.fromkeys(s.dropna().astype(str).str.strip())) if s.name == 'subgroup' and s.dropna().astype(str).str.strip().nunique() > 1 else (s.dropna().astype(str).str.strip().iloc[0] if len(s.dropna().astype(str).str.strip()) else pd.NA))
df_unique = df_non_nulls.drop_duplicates(subset = cols, keep = 'first') # df of unique
df_deduplicated = pd.concat([df_non_duplicates, df_kept, df_nulls], ignore_index=True) # df of unique + df of non-duplicates

results = {"records": len(df),  
"nulls": len(df_nulls), 
"non_nulls": len(df_non_nulls), 
"non_duplicates": len(df_non_duplicates), 
"duplicates": len(df_duplicates), 
"removed": len(df_removed), 
"kept": len(df_kept),
"unique": len(df_unique),
"deduplicated": len(df_deduplicated)
}

# output_file_name = deduplication/doi/doi_deduplicated.csv
df_nulls.to_csv(output_file_name.replace('deduplicated','nulls'), index = False)
df_deduplicated.to_csv(output_file_name, index = False)
df_removed.to_csv(output_file_name.replace('deduplicated','duplicates_removed'), index = False)
df_deduplicated.to_csv(output_for_recycle, index = False)

graph_text = f"""---
config:
theme: neutral
curve: stepBefore
---
graph TD;
A["`**records** (*n* = {results['records']})`"];
B["`null (*n* = {results['nulls']})`"];
C["`non-null (*n* = {results['non_nulls']})`"];
D["`non-duplicates (*n* = {results['non_duplicates']})`"];
E["`duplicates (*n* = {results['duplicates']})`"];
F["`duplicates kept (*n* = {results['kept']})`"];
G["`duplicates removed (*n* = {results['removed']})`"];
H["`unique (*n* = {results['unique']})`"];
I["`deduplicated (*n* = {results['deduplicated']})`"];

A --> B & C;
C --> D & E;
E --> F & G;
D & F --> H
B & H --> I"""

with open(prisma_file_name, "w") as f:
    f.write(graph_text)

!mmdc -i "{prisma_file_name}" -o "{output_file}"_light.svg
!mmdc -i "{prisma_file_name}" -o "{output_file}"_dark.svg -t dark -b transparent
print(results)
```

::: {.output .stream .stdin}
    Enter file name:  title+author+year_deduplicated
    Enter the column for which to deduplicate based on:  title+year
:::

::: {.output .stream .stdout}
    Generating single mermaid chart
    Generating single mermaid chart
    {'records': 780, 'nulls': 0, 'non_nulls': 780, 'non_duplicates': 727, 'duplicates': 53, 'removed': 29, 'kept': 24, 'unique': 751, 'deduplicated': 751}
:::
:::::

::: {#8b0bd931-14da-4011-84c9-b04838cb0ddf .cell .markdown}
[top](#toc) \| [search strategy](#search-strategy) \| [search](#search)
\| [deduplication](#deduplication) \| [screening](#screening) \| [data
collection](#data-collection) \|

`<a id="screening">`{=html}`</a>`{=html}

<div align="center">
	<font size="5" style="font-family:Times New Roman;font-variant: small-caps;">Screening</font><br>
</div>

------------------------------------------------------------------------
:::

::: {#ca452bbe-8098-40e0-8247-fca3c19a3cb5 .cell .markdown}
Screening filter #1: Language
:::

:::: {#fb242547-5f5e-498c-ad9b-a1c477fa67a1 .cell .code execution_count="85"}
``` python
df = pd.read_csv(f"{deduplication}/title+year_deduplicated.csv", encoding = "utf-8")
df.to_csv(f"{screening}/screening.csv", encoding = "utf-8")
df.sort_values(by = ['subgroup', 'year', 'authors'])

dict = {"language": "English"}
import pandas as pd
import os

for x, y in dict.items():
    mask = df[x].astype(str).str.contains(y, case=False, na=False)
    true = df[mask]
    false = df[~mask]
    folder = f"{title_abstract}/{x}"
    os.makedirs(folder, exist_ok = True)
    file = f"{y}"
    true.to_csv(f"{folder}/{file}.csv", encoding = "utf-8")
    false.to_csv(f"{folder}/non_{file}.csv", encoding = "utf-8")
    print(f"Number of records that contain '{y}' in column {x}: ",len(true))
    print(f"Number of records that don't contain '{y}' in column '{x}': ",len(false))
    
```

::: {.output .error ename="OSError" evalue="Cannot save file into a non-existent directory: '     Unnamed: 0   id                study                    subgroup  \\
0             4    5  Martorell-de (2025)                        BPTB   
1             6    7     Obradović (2023)                        BPTB   
2            35   36        Biswal (2016)                        BPTB   
3            36   37    Iliopoulos (2017)                        BPTB   
4            46   47       Valentí (2014)                        BPTB   
..          ...  ...                  ...                         ...   
745         657   32                  NaN              ['BPTB', 'QT']   
746         634    9                  NaN              ['BPTB', 'QT']   
747         638   13                  NaN        ['BPTB', 'HT', 'QT']   
748         818  193                  NaN               ['QT', 'PLT']   
749        1100  158     Andersson (2009)  ['BPTB', \"['BPTB', 'HT']\"]   

                                               authors  first_author  \\
0    Martorell-de Fortuny L, Torres-Claramunt R, Sá...  Martorell-de   
1    Obradović M, Ninković S, Gvozdenović N, Tošić ...     Obradović   
2    Biswal UK, Balaji G, Nema S, Poduval M, Menon ...        Biswal   
3    Iliopoulos E, Galanis N, Zafeiridis A, Iosifid...    Iliopoulos   
4    Valentí Azcárate A, Lamo-Espinosa J, Aquerreta...       Valentí   
..                                                 ...           ...   
745                                                NaN           NaN   
746                                                NaN           NaN   
747                                                NaN           NaN   
748                                                NaN           NaN   
749              Andersson D, Samuelsson K, Karlsson J     Andersson   

                                                 title  \\
0    Patellar bone defect grafting does not reduce ...   
1    Tubularization of Bone-Tendon-Bone Grafts: Eff...   
2    Correlation of tunnel widening and tunnel posi...   
3    Anatomic single-bundle anterior cruciate ligam...   
4    Comparison between two different platelet-rich...   
..                                                 ...   
745  Postoperative Blood Flow Restriction Training ...   
746  Prospective Evaluation of Post-operative Pain ...   
747  Reduced Knee Flexion Strength 18 Years After A...   
748  Reducing the Burden of Post-traumatic Knee Ost...   
749  Treatment of Anterior Cruciate Ligament Injuri...   

                                           short_title  \\
0    patellarbonedefectgraftingdoesnotreduceanterio...   
1    tubularizationofbonetendonbonegrafts:effectson...   
2    correlationoftunnelwideningandtunnelpositionin...   
3    anatomicsinglebundleanteriorcruciateligamentre...   
4    comparisonbetweentwodifferentplateletrichplasm...   
..                                                 ...   
745  postoperativebloodflowrestrictiontrainingfollo...   
746  prospectiveevaluationofpostoperativepainmanage...   
747  reducedkneeflexionstrength18yearsafteraclrecon...   
748  reducingtheburdenofposttraumatickneeosteoarthr...   
749  treatmentofanteriorcruciateligamentinjurieswit...   

                                              abstract  year language  \\
0    PURPOSE: Donor site morbidity is the main draw...  2025  English   
1    Background and Objectives: The study addresses...  2023  English   
2    OBJECTIVE: To study the correlation between tu...  2016  English   
3    PURPOSE: Anterior cruciate ligament (ACL) inju...  2017  English   
4    INTRODUCTION: To compare the clinical, analyti...  2014  English   
..                                                 ...   ...      ...   
745  Brief SummaryThe purpose of this study is to e...  2019  English   
746  Brief SummaryThe goal of this randomized clini...  2024  English   
747  Brief SummaryBackground: Bone-patellar tendon-...  2023  English   
748  Brief SummaryFROM RISK FACTORS TO THE PREVENTI...  2025  English   
749  Purpose: The primary aim was to investigate an...  2009  English   

                                               journal  source  \\
0    Knee surgery sports traumatology arthroscopy :...  pubmed   
1                                            Medicina   pubmed   
2    European journal of orthopaedic surgery & trau...  pubmed   
3    Knee surgery sports traumatology arthroscopy :...  pubmed   
4                                               Injury  pubmed   
..                                                 ...     ...   
745                                 Clinicaltrials.gov  embase   
746                                 Clinicaltrials.gov  embase   
747                                 Clinicaltrials.gov  embase   
748                                 Clinicaltrials.gov  embase   
749  Arthroscopy-the journal of arthroscopic and re...     wos   

                               doi  \\
0                10.1002\\ksa.12449   
1         10.3390\\medicina59101764   
2        10.1007\\s00590-016-1809-4   
3        10.1007\\s00167-016-4229-4   
4    10.1016\\S0020-1383(14)70008-7   
..                             ...   
745                            NaN   
746                            NaN   
747                            NaN   
748                            NaN   
749   10.1016\\j.arthro.2009.04.066   

                                           doi_url        pmid  \\
0                https:\\doi.org\\10.1002\\ksa.12449  39194385.0   
1         https:\\doi.org\\10.3390\\medicina59101764  37893482.0   
2        https:\\doi.org\\10.1007\\s00590-016-1809-4  27376940.0   
3        https:\\doi.org\\10.1007\\s00167-016-4229-4  27371291.0   
4    https:\\doi.org\\10.1016\\S0020-1383(14)70008-7  25384473.0   
..                                             ...         ...   
745                               https:\\doi.org\\         NaN   
746                               https:\\doi.org\\         NaN   
747                               https:\\doi.org\\         NaN   
748                               https:\\doi.org\\         NaN   
749   https:\\doi.org\\10.1016\\j.arthro.2009.04.066  19501297.0   

                                      pmid_url  \\
0    https:\\pubmed.ncbi.nlm.nih.gov\\39194385\\   
1    https:\\pubmed.ncbi.nlm.nih.gov\\37893482\\   
2    https:\\pubmed.ncbi.nlm.nih.gov\\27376940\\   
3    https:\\pubmed.ncbi.nlm.nih.gov\\27371291\\   
4    https:\\pubmed.ncbi.nlm.nih.gov\\25384473\\   
..                                         ...   
745                                        NaN   
746                                        NaN   
747                                        NaN   
748                                        NaN   
749  https:\\pubmed.ncbi.nlm.nih.gov\\19501297\\   

                                     title+author+year  \\
0    Martorell-de+patellarbonedefectgraftingdoesnot...   
1    Obradović+tubularizationofbonetendonbonegrafts...   
2    Biswal+correlationoftunnelwideningandtunnelpos...   
3    Iliopoulos+anatomicsinglebundleanteriorcruciat...   
4    Valentí+comparisonbetweentwodifferentplateletr...   
..                                                 ...   
745                                                NaN   
746                                                NaN   
747                                                NaN   
748                                                NaN   
749  Andersson+treatmentofanteriorcruciateligamenti...   

                                            title+year  
0    patellarbonedefectgraftingdoesnotreduceanterio...  
1    tubularizationofbonetendonbonegrafts:effectson...  
2    correlationoftunnelwideningandtunnelpositionin...  
3    anatomicsinglebundleanteriorcruciateligamentre...  
4    comparisonbetweentwodifferentplateletrichplasm...  
..                                                 ...  
745  postoperativebloodflowrestrictiontrainingfollo...  
746  prospectiveevaluationofpostoperativepainmanage...  
747  reducedkneeflexionstrength18yearsafteraclrecon...  
748  reducingtheburdenofposttraumatickneeosteoarthr...  
749  treatmentofanteriorcruciateligamentinjurieswit...  

[750 rows x 19 columns]'"}
    ---------------------------------------------------------------------------
    OSError                                   Traceback (most recent call last)
    Cell In[85], line 2
          1 screening = pd.read_csv(f"{deduplication}/title+year_deduplicated.csv", encoding = "utf-8")
    ----> 2 screening.to_csv(f"{screening}/screening.csv", encoding = "utf-8")
          3 screening.sort_values(by = ['subgroup', 'year', 'authors'])
          4 df = screening
          5 

    File G:\My Drive\.venv\Lib\site-packages\pandas\core\generic.py:3988, in NDFrame.to_csv(self, path_or_buf, sep, na_rep, float_format, columns, header, index, index_label, mode, encoding, compression, quoting, quotechar, lineterminator, chunksize, date_format, doublequote, escapechar, decimal, errors, storage_options)
       3984             float_format=float_format,
       3985             decimal=decimal,
       3986         )
       3987 
    -> 3988         return DataFrameRenderer(formatter).to_csv(
       3989             path_or_buf,
       3990             lineterminator=lineterminator,
       3991             sep=sep,

    File G:\My Drive\.venv\Lib\site-packages\pandas\io\formats\format.py:1025, in DataFrameRenderer.to_csv(self, path_or_buf, encoding, sep, columns, index_label, mode, compression, quoting, quotechar, lineterminator, chunksize, date_format, doublequote, escapechar, errors, storage_options)
       1004     created_buffer = False
       1006 csv_formatter = CSVFormatter(
       1007     path_or_buf=path_or_buf,
       1008     lineterminator=lineterminator,
       (...)   1023     formatter=self.fmt,
       1024 )
    -> 1025 csv_formatter.save()
       1027 if created_buffer:
       1028     assert isinstance(path_or_buf, StringIO)

    File G:\My Drive\.venv\Lib\site-packages\pandas\io\formats\csvs.py:251, in CSVFormatter.save(self)
        247 """
        248 Create the writer & save.
        249 """
        250 # apply compression and byte/text conversion
    --> 251 with get_handle(
        252     self.filepath_or_buffer,
        253     self.mode,
        254     encoding=self.encoding,
        255     errors=self.errors,
        256     compression=self.compression,
        257     storage_options=self.storage_options,
        258 ) as handles:
        259     # Note: self.encoding is irrelevant here
        260     # error: Argument "quoting" to "writer" has incompatible type "int";
        261     # expected "Literal[0, 1, 2, 3]"
        262     self.writer = csvlib.writer(
        263         handles.handle,
        264         lineterminator=self.lineterminator,
       (...)    269         quotechar=self.quotechar,
        270     )
        272     self._save()

    File G:\My Drive\.venv\Lib\site-packages\pandas\io\common.py:793, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
        791 # Only for write methods
        792 if "r" not in mode and is_path:
    --> 793     check_parent_directory(str(handle))
        795 if compression:
        796     if compression != "zstd":
        797         # compression libraries do not like an explicit text-mode

    File G:\My Drive\.venv\Lib\site-packages\pandas\io\common.py:652, in check_parent_directory(path)
        650 parent = Path(path).parent
        651 if not parent.is_dir():
    --> 652     raise OSError(rf"Cannot save file into a non-existent directory: '{parent}'")

    OSError: Cannot save file into a non-existent directory: '     Unnamed: 0   id                study                    subgroup  \
    0             4    5  Martorell-de (2025)                        BPTB   
    1             6    7     Obradović (2023)                        BPTB   
    2            35   36        Biswal (2016)                        BPTB   
    3            36   37    Iliopoulos (2017)                        BPTB   
    4            46   47       Valentí (2014)                        BPTB   
    ..          ...  ...                  ...                         ...   
    745         657   32                  NaN              ['BPTB', 'QT']   
    746         634    9                  NaN              ['BPTB', 'QT']   
    747         638   13                  NaN        ['BPTB', 'HT', 'QT']   
    748         818  193                  NaN               ['QT', 'PLT']   
    749        1100  158     Andersson (2009)  ['BPTB', "['BPTB', 'HT']"]   

                                                   authors  first_author  \
    0    Martorell-de Fortuny L, Torres-Claramunt R, Sá...  Martorell-de   
    1    Obradović M, Ninković S, Gvozdenović N, Tošić ...     Obradović   
    2    Biswal UK, Balaji G, Nema S, Poduval M, Menon ...        Biswal   
    3    Iliopoulos E, Galanis N, Zafeiridis A, Iosifid...    Iliopoulos   
    4    Valentí Azcárate A, Lamo-Espinosa J, Aquerreta...       Valentí   
    ..                                                 ...           ...   
    745                                                NaN           NaN   
    746                                                NaN           NaN   
    747                                                NaN           NaN   
    748                                                NaN           NaN   
    749              Andersson D, Samuelsson K, Karlsson J     Andersson   

                                                     title  \
    0    Patellar bone defect grafting does not reduce ...   
    1    Tubularization of Bone-Tendon-Bone Grafts: Eff...   
    2    Correlation of tunnel widening and tunnel posi...   
    3    Anatomic single-bundle anterior cruciate ligam...   
    4    Comparison between two different platelet-rich...   
    ..                                                 ...   
    745  Postoperative Blood Flow Restriction Training ...   
    746  Prospective Evaluation of Post-operative Pain ...   
    747  Reduced Knee Flexion Strength 18 Years After A...   
    748  Reducing the Burden of Post-traumatic Knee Ost...   
    749  Treatment of Anterior Cruciate Ligament Injuri...   

                                               short_title  \
    0    patellarbonedefectgraftingdoesnotreduceanterio...   
    1    tubularizationofbonetendonbonegrafts:effectson...   
    2    correlationoftunnelwideningandtunnelpositionin...   
    3    anatomicsinglebundleanteriorcruciateligamentre...   
    4    comparisonbetweentwodifferentplateletrichplasm...   
    ..                                                 ...   
    745  postoperativebloodflowrestrictiontrainingfollo...   
    746  prospectiveevaluationofpostoperativepainmanage...   
    747  reducedkneeflexionstrength18yearsafteraclrecon...   
    748  reducingtheburdenofposttraumatickneeosteoarthr...   
    749  treatmentofanteriorcruciateligamentinjurieswit...   

                                                  abstract  year language  \
    0    PURPOSE: Donor site morbidity is the main draw...  2025  English   
    1    Background and Objectives: The study addresses...  2023  English   
    2    OBJECTIVE: To study the correlation between tu...  2016  English   
    3    PURPOSE: Anterior cruciate ligament (ACL) inju...  2017  English   
    4    INTRODUCTION: To compare the clinical, analyti...  2014  English   
    ..                                                 ...   ...      ...   
    745  Brief SummaryThe purpose of this study is to e...  2019  English   
    746  Brief SummaryThe goal of this randomized clini...  2024  English   
    747  Brief SummaryBackground: Bone-patellar tendon-...  2023  English   
    748  Brief SummaryFROM RISK FACTORS TO THE PREVENTI...  2025  English   
    749  Purpose: The primary aim was to investigate an...  2009  English   

                                                   journal  source  \
    0    Knee surgery sports traumatology arthroscopy :...  pubmed   
    1                                            Medicina   pubmed   
    2    European journal of orthopaedic surgery & trau...  pubmed   
    3    Knee surgery sports traumatology arthroscopy :...  pubmed   
    4                                               Injury  pubmed   
    ..                                                 ...     ...   
    745                                 Clinicaltrials.gov  embase   
    746                                 Clinicaltrials.gov  embase   
    747                                 Clinicaltrials.gov  embase   
    748                                 Clinicaltrials.gov  embase   
    749  Arthroscopy-the journal of arthroscopic and re...     wos   

                                   doi  \
    0                10.1002\ksa.12449   
    1         10.3390\medicina59101764   
    2        10.1007\s00590-016-1809-4   
    3        10.1007\s00167-016-4229-4   
    4    10.1016\S0020-1383(14)70008-7   
    ..                             ...   
    745                            NaN   
    746                            NaN   
    747                            NaN   
    748                            NaN   
    749   10.1016\j.arthro.2009.04.066   

                                               doi_url        pmid  \
    0                https:\doi.org\10.1002\ksa.12449  39194385.0   
    1         https:\doi.org\10.3390\medicina59101764  37893482.0   
    2        https:\doi.org\10.1007\s00590-016-1809-4  27376940.0   
    3        https:\doi.org\10.1007\s00167-016-4229-4  27371291.0   
    4    https:\doi.org\10.1016\S0020-1383(14)70008-7  25384473.0   
    ..                                             ...         ...   
    745                               https:\doi.org\         NaN   
    746                               https:\doi.org\         NaN   
    747                               https:\doi.org\         NaN   
    748                               https:\doi.org\         NaN   
    749   https:\doi.org\10.1016\j.arthro.2009.04.066  19501297.0   

                                          pmid_url  \
    0    https:\pubmed.ncbi.nlm.nih.gov\39194385\   
    1    https:\pubmed.ncbi.nlm.nih.gov\37893482\   
    2    https:\pubmed.ncbi.nlm.nih.gov\27376940\   
    3    https:\pubmed.ncbi.nlm.nih.gov\27371291\   
    4    https:\pubmed.ncbi.nlm.nih.gov\25384473\   
    ..                                         ...   
    745                                        NaN   
    746                                        NaN   
    747                                        NaN   
    748                                        NaN   
    749  https:\pubmed.ncbi.nlm.nih.gov\19501297\   

                                         title+author+year  \
    0    Martorell-de+patellarbonedefectgraftingdoesnot...   
    1    Obradović+tubularizationofbonetendonbonegrafts...   
    2    Biswal+correlationoftunnelwideningandtunnelpos...   
    3    Iliopoulos+anatomicsinglebundleanteriorcruciat...   
    4    Valentí+comparisonbetweentwodifferentplateletr...   
    ..                                                 ...   
    745                                                NaN   
    746                                                NaN   
    747                                                NaN   
    748                                                NaN   
    749  Andersson+treatmentofanteriorcruciateligamenti...   

                                                title+year  
    0    patellarbonedefectgraftingdoesnotreduceanterio...  
    1    tubularizationofbonetendonbonegrafts:effectson...  
    2    correlationoftunnelwideningandtunnelpositionin...  
    3    anatomicsinglebundleanteriorcruciateligamentre...  
    4    comparisonbetweentwodifferentplateletrichplasm...  
    ..                                                 ...  
    745  postoperativebloodflowrestrictiontrainingfollo...  
    746  prospectiveevaluationofpostoperativepainmanage...  
    747  reducedkneeflexionstrength18yearsafteraclrecon...  
    748  reducingtheburdenofposttraumatickneeosteoarthr...  
    749  treatmentofanteriorcruciateligamentinjurieswit...  

    [750 rows x 19 columns]'
:::
::::

:::: {#127c57bf-5f14-49c3-82f4-af43f5ecf722 .cell .code execution_count="16"}
``` python
df.info()
```

::: {.output .stream .stdout}
    <class 'pandas.DataFrame'>
    RangeIndex: 1346 entries, 0 to 1345
    Data columns (total 28 columns):
     #   Column           Non-Null Count  Dtype 
    ---  ------           --------------  ----- 
     0   pmid             1346 non-null   str   
     1   PubDate          1346 non-null   str   
     2   EPubDate         980 non-null    str   
     3   Source           1346 non-null   str   
     4   AuthorList       1346 non-null   object
     5   LastAuthor       1345 non-null   str   
     6   Title            1346 non-null   str   
     7   Volume           1315 non-null   str   
     8   Issue            1228 non-null   str   
     9   Pages            1290 non-null   str   
     10  language         1346 non-null   object
     11  NlmUniqueID      1346 non-null   str   
     12  ISSN             1223 non-null   str   
     13  ESSN             1119 non-null   str   
     14  PubTypeList      1346 non-null   object
     15  RecordStatus     1346 non-null   str   
     16  PubStatus        1039 non-null   str   
     17  ArticleIds       1346 non-null   object
     18  DOI              1282 non-null   str   
     19  History          1346 non-null   object
     20  References       1346 non-null   object
     21  HasAbstract      1346 non-null   str   
     22  PmcRefCount      1346 non-null   str   
     23  FullJournalName  1346 non-null   str   
     24  ELocationID      1069 non-null   str   
     25  SO               1346 non-null   str   
     26  abstract         1322 non-null   str   
     27  year             1346 non-null   str   
    dtypes: object(6), str(22)
    memory usage: 294.6+ KB
:::
::::

::: {#6cf283b8-9cc2-495a-987a-5b3638920114 .cell .markdown}
Screening filter #2: Randomized controlled trials
:::

:::: {#3730dea5-134e-494c-b844-98536ce004ec .cell .code execution_count="25"}
``` python
# Screen for 'randomized' in a newly made 'title and abstract' column
df = true
df['tiab'] = df['title'] + " " + df['abstract']
dict = {"tiab": "random"}
for x, y in dict.items():
    mask = df[x].astype(str).str.contains(y, case=False, na=False)
    true = df[mask]
    false = df[~mask]
    folder = f"{title_abstract}/{x}"
    os.makedirs(folder, exist_ok = True)
    file = f"{y}"
    true.to_csv(f"{folder}/{file}.csv", encoding = "utf-8")
    false.to_csv(f"{folder}/non_{file}.csv", encoding = "utf-8")
    print(f"Number of records that contain '{y}' in column {x}: ",len(true))
    print(f"Number of records that don't contain '{y}' in column '{x}': ",len(false))
```

::: {.output .stream .stdout}
    Number of records that contain 'random' in column tiab:  174
    Number of records that don't contain 'random' in column 'tiab':  1127
:::
::::

::: {#3031adfe-3342-4a7f-b4bf-b09009015410 .cell .markdown}
Screening filter #3: Clinical trials (unpublished and without results)
:::

:::: {#d9f10964-7af6-4eb1-bb41-e80c8daf2c64 .cell .code execution_count="26"}
``` python
# Screen out unpublished clinical trials from "clinicaltrials.gov" (only published RCTs, from peer-reviewed journals included)
df = true
dict = {"journal": "clinicaltrials.gov"}
for x, y in dict.items():
    mask = df[x].astype(str).str.contains(y, case=False, na=False)
    true = df[mask]
    false = df[~mask]
    folder = f"{title_abstract}/{x}"
    os.makedirs(folder, exist_ok = True)
    file = f"{y}"
    true.to_csv(f"{folder}/{file}.csv", encoding = "utf-8")
    false.to_csv(f"{folder}/non_{file}.csv", encoding = "utf-8")
    print(f"Number of records that contain '{y}' in column {x}: ",len(true))
    print(f"Number of records that don't contain '{y}' in column '{x}': ",len(false))
```

::: {.output .stream .stdout}
    Number of records that contain 'clinicaltrials.gov' in column journal:  0
    Number of records that don't contain 'clinicaltrials.gov' in column 'journal':  174
:::
::::

::: {#d29e63bb-749b-4ea5-8ad0-5149aed21951 .cell .markdown}

------------------------------------------------------------------------

[top](#toc) \| [search strategy](#search-strategy) \| [search](#search)
\| [deduplication](#deduplication) \| [screening](#screening) \| [data
collection](#data-collection) \|

`<a id="data-collection">`{=html}`</a>`{=html}

<h1 align="center" style="font-family:Times New Roman;font-variant:small-caps;">Data Collection</h1>
:::

::: {#783c60cf-218a-4048-afb1-1bec22c6923c .cell .markdown}
:::

::: {#1803f402-0746-418d-b74a-1b92d9f851ed .cell .markdown}
<div align="center">
	<font size="5" style="font-family:Times New Roman;font-variant: small-caps;">patellar</font><br>
</div>
:::

::: {#59ca5e30-b165-43cf-aca2-8467a35538a8 .cell .code}
``` python
patellar = tiab[tiab["subgroup"] == "bptb"]
patellar.to_csv(f"{title_abstract}/patellar.csv", encoding = "utf-8")
```
:::

::: {#37fe44d0-c6d7-4ae5-b112-f8613309e251 .cell .code}
``` python
```
:::

::: {#f31098f7-c621-4c2f-8f71-eb294419e654 .cell .code}
``` python
```
:::
