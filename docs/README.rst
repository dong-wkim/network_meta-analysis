.. container:: cell markdown
   :name: 60a2cb4f-08fd-4b71-beca-29f72e57b338

   .. raw:: html

      <!-- Notes:

      Read this and follow the steps to organize and stuff.
      https://medium.com/@caneuenschwander/how-to-turn-a-messy-jupyter-notebook-into-a-professional-python-project-f34d5ee7f88b



      -->

.. container:: cell markdown
   :name: 3963aa21-61c3-448e-9a26-f21b97d39bba

   .. raw:: html

      <div align="center" style="font-family:Times New Roman;">
          <h1>
              What is the optimal graft choice for primary anterior cruciate ligament reconstruction surgery?
          </h1>
      </div>

   A systematic review and network meta-analysis

   .. raw:: html

      <div align = "center"><a href="https://dongwkim.com">
          <img src="https://raw.githubusercontent.com/dong-wkim/assets/refs/heads/master/uj_logo.jpg" alt="Logo" width="100" height="100"></a></br></br>
          <div align="center">
              <h3 size="5" style="font-family:Times New Roman;font-variant: small-caps;">
                  Doctoral Thesis
              </h3>
          </div>
          </br>
          </br>
          <div align="center">
                  <i style="font-family:Times New Roman;">
                      In fulfillment for the award of the degree of:
                  </i>
              </h5>
          </div>
          <div align="center">
              <h3 size="3" style="font-family:Times New Roman;font-variant: small-caps;">
                  Doctor of Philosophy
              </h3>
          </div>
      </br>
          <div align = "center">
              <sub>
                  <i style="font-family:Times New Roman;">
                      Submitted by:
                  </i>
              </sub>
          </div>
          <div align = "center"><sub style="font-family:Times New Roman;">Dong Woon Kim, M.D.</sub></div></br>
              <div align = "center"><sub style="font-family:Times New Roman;"><i>Supervised by:</i></sub></div>
              <div align = "center"><sub style="font-family:Times New Roman;">Konrad Malinowski, M.D., Ph.D</sub></div>
      </div>

   \ https://doi.org/10.7910/DVN/NGIW6E\  1 Department of Anatomy,
   Jagiellonian University, Kraków, Poland 2 Whiting College of
   Engineering, Johns Hopkins University, Baltimore, MD, United States 3
   Harvard University, Cambridge, MA, United States

.. container:: cell markdown
   :name: 1370ab4e-67a5-4962-b418-90da4313b85b

   .. raw:: html

      <details>
          <summary style="font-family:Times New Roman;">Table of Contents</summary>  

      - [Systematic Review](#systematic_review)
          - [Search strategy](#search_strategy)
          - [Search](#search)
          - [Deduplication](#deduplication)
          - [Screening](#screening)
              - [Title abstract screening](#title_abstract_screening)
              - [Full-text screening](#full-text-screening)
      - [Data Collection](#data_collection)
          - [Forms](#forms)



      </details>

   .. raw:: html

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

   .. raw:: html

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

   .. raw:: html

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

.. container:: cell markdown
   :name: fdfd4938-8fe0-4d87-adc4-3b2be2b82c2e

   Remote Jupyter servers:

   - `JupyterLite <https://dong-wkim.github.io/jupyter/lab/index.html>`__
   - `PythonAnywhere <https://www.pythonanywhere.com/user/dongwkim/>`__
   - `Anaconda Cloud <https://anaconda.com/app/>`__

.. container:: cell markdown
   :name: 21224837-cff8-4d48-8dab-3c860194fc3d

   Kim, Danny, and Konrad Malinowski. 2026. “What Is the Optimal Graft
   for Primary Anterior Cruciate Ligament Reconstruction Surgery?”
   Harvard Dataverse. https://doi.org/10.7910/DVN/NGIW6E.

.. container:: cell code
   :name: 9c00985a-004a-43a3-b8a0-730303f4077a

   .. code:: python

      import numpy as np
      import matplotlib.pyplot as plt
      from mpl_toolkits.mplot3d.art3d import Poly3DCollection

      def icosahedral():
          # Golden ratio
          phi = (1 + np.sqrt(5)) / 2
          
          # Vertices of a regular icosahedron
          vertices = np.array([
              [-1, phi, 0],
              [1, phi, 0],
              [-1, -phi, 0],
              [1, -phi, 0],
              [0, -1, phi],
              [0, 1, phi],
              [0, -1, -phi],
              [0, 1, -phi],
              [phi, 0, -1],
              [phi, 0, 1],
              [-phi, 0, -1],
              [-phi, 0, 1]
          ])
          
          # Faces of the icosahedron
          faces = [
              [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
              [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
              [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
              [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
          ]
          
          # Create the 3D plot
          fig = plt.figure()
          ax = fig.add_subplot(111, projection='3d')
          
          
          # Plot the faces
          poly3d = [[[vertices[index] for index in face] for face in faces]]
          ax.add_collection3d(
              Poly3DCollection(
                  poly3d[0],
                  linewidths=0.05,
                  facecolors='black',
                  edgecolors='black',
                  alpha=0.1
              )
          )
          
          # Plot the vertices
          ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='black')
          
          # Ensure the axes are scaled equally to prevent distortion
          max_radius = np.max(np.abs(vertices)) + 0.5
          ax.set_xlim([-max_radius, max_radius])
          ax.set_ylim([-max_radius, max_radius])
          ax.set_zlim([-max_radius, max_radius])
          ax.set_aspect('auto')
          
          plt.show()

      fig2 = icosahedral() 
      # make a 3D network icosahedral diagram that is also interactive and clickable to the individual graft manuscripts!
      # make into title page for quick navigation to the 6 srma projects that will follow this one for each graft.

   .. container:: output display_data

      |image1|

.. container:: cell code
   :name: def966ee-a0ab-438a-a4f8-f82690928982

   .. code:: python

.. container:: cell markdown
   :name: a57fbc61-c21b-45aa-b0ff-7da6ef6ca746

   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---+
   |            | pubmed                                                                                                                                                   | embase                                                                                                                                                   | web of science                                                                                                                                          |   |
   +============+==========================================================================================================================================================+==========================================================================================================================================================+=========================================================================================================================================================+===+
   | patellar   | `pm_bptb.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_bptb.csv>`__\ (*n* | `em_bptb.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_bptb.csv>`__\ (*n* | `wos_bptb.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_bptb.csv>`__\ (*n* |   |
   |            | = 190)                                                                                                                                                   | = 73)                                                                                                                                                    | = 186)                                                                                                                                                  |   |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---+
   | hamstring  | `pm_ht.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_ht.csv>`__\ (*n* =   | `em_ht.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_ht.csv>`__\ (*n* =   | `wos_ht.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_ht.csv>`__\ (*n*     |   |
   |            | 202)                                                                                                                                                     | 97)                                                                                                                                                      | =253)                                                                                                                                                   |   |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---+
   | quadriceps | `pm_qt.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_qt.csv>`__\ (*n* =   | `em_qt.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_qt.csv>`__\ (*n* =   | `wos_qt.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_qt.csv>`__\ (*n* =   |   |
   |            | 165)                                                                                                                                                     | 114)                                                                                                                                                     | 70)                                                                                                                                                     |   |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---+
   | peroneus   | `pm_plt.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_plt.csv>`__\ (*n* = | `em_plt.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_plt.csv>`__\ (*n* = | `wos_plt.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_plt.csv>`__\ (*n* = |   |
   | longus     | 2)                                                                                                                                                       | 25)                                                                                                                                                      | 4)                                                                                                                                                      |   |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---+
   | Achilles   | `pm_at.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_at.csv>`__\ (*n* =   | `em_at.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_at.csv>`__\ (*n* =   | `wos_at.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_at.csv>`__\ (*n* =   |   |
   |            | 7)                                                                                                                                                       | 5)                                                                                                                                                       | 10)                                                                                                                                                     |   |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---+
   | tibialis   | `pm_ta.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed/pm_ta.csv>`__\ (*n* =   | `em_ta.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase/em_ta.csv>`__\ (*n* =   | `wos_ta.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos/wos_ta.csv>`__\ (*n* =   |   |
   |            | 7)                                                                                                                                                       | 3)                                                                                                                                                       | 8)                                                                                                                                                      |   |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---+
   |            | `pubmed.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//pubmed.csv>`__\ (*n* = )      | `embase.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//embase.csv>`__\ (*n* = )      | `wos.csv <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//wos.csv>`__\ (*n* = )           |   |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---+

.. container:: cell markdown
   :name: a9e0b03e-b911-4658-b53f-f90874ebfe50

   Add columns for deduplication, screening, and data collection to show
   the number of rows per each stage.

.. container:: cell markdown
   :name: 21087bf9-4181-4397-8e10-dee41e958637

   Define directory structure and store paths as [STRIKEOUT:global]
   static webpages (even better).

.. container:: cell markdown
   :name: 1c51cdb3-ee2e-4fd9-9fb4-971278dfdeae

   - `network
     meta-analysis <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master//.md>`__

     - `systematic_review/ <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review//systematic_review/.md>`__

       - `protocol <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/protocol//systematic_review/protocol/.md>`__

         - `prospero <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/protocol/prospero/systematic_review/protocol/prospero.md>`__
         - `cochrane <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/protocol/cochrane/systematic_review/protocol/cochrane.md>`__

       - `search_strategy <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search_strategy/systematic_review/search_strategy.md>`__

         - `pubmed <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search_strategy/pubmed/systematic_review/search_strategy/pubmed.md>`__
         - `embase <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search_strategy/embase/systematic_review/search_strategy/embase.md>`__
         - `wos <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search_strategy/wos/systematic_review/search_strategy/wos.md>`__

       - `search <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search//systematic_review/search/.md>`__

         - `pubmed <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search/pubmed/systematic_review/search/pubmed.md>`__
         - `embase <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search/embase/systematic_review/search/embase.md>`__
         - `wos <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/search/wos/systematic_review/search/wos.md>`__

       - `deduplication/ <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/deduplication//systematic_review/deduplication/.md>`__

         - `doi <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/deduplication/doi/doi_deduplicated.csv>`__
         - `title+author+year <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/deduplication/title+author+year/title+author+year_deduplicated.csv>`__
         - `title+year <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/deduplication/title+year/title+year_deduplicated.csv>`__

       - `screening/ <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/screening//systematic_review/screening/.md>`__

         - `title_abstract_screening <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/screening/title_abstract_screening/systematic_review/screening/title_abstract_screening.md>`__
         - `PDF <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/screening/PDF/systematic_review/screening/PDF.md>`__
         - `full-text_screening <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/systematic_review/screening/full-text_screening/systematic_review/screening/full-text_screening.md>`__

   - `data <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/data/data.md>`__
   - `meta-analysis <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/meta-analysis/meta-analysis.md>`__
   - `manuscript <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/manuscript/manuscript.md>`__
   - `README.ipynb <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/README.ipynb/README.ipynb.md>`__
   - `docs <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/docs/docs.md>`__
   - `src <https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/refs/heads/master/src/src.md>`__
     \``\`

.. container:: cell markdown
   :name: abba1a82-3b54-4fc0-bac9-a83d6192c552

   .. raw:: html

      <!---
      Put all supportive scripts into an __init__.py file or main.py file (?)
      This README file must be now deconstructured, picked apart piece by piece until you're left with:

      1. back-end scripts are placed in src folder as py files that are imported.
      2. individual ipynb notebooks (for testing and easy conversion) that are converted into markdown -> ReStructuredText and MyST-MD, which are deployed to
      3. Sphinx OR jupyter book with interactive widgets that is hosted / deployed to the web
      4. the documentation remains

      --->

.. container:: cell code
   :name: ebd2e89d-4ce0-44d6-8b2c-45b1f3395b9f

   .. code:: python

      requirements = f"""
      numpy
      matplotlib
      seaborn
      biopython
      mermaid-py
      ipywidgets
      google-drive
      ipysheet
      ipydatagrid
      shinywidgets
      altair
      bokeh
      plotly 
      ipyleaflet 
      pydeck==0.8.0
      jupyterlite-pyodide-kernel
      jupyter-book>=2.0
      jupyter_server
      """

      with open("./requirements.txt", "w") as f:
          f.write(requirements)

      %pip install -r requirements.txt

   .. container:: output stream stdout

      ::

         Requirement already satisfied: numpy in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 2)) (2.4.4)
         Requirement already satisfied: matplotlib in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 3)) (3.10.9)
         Requirement already satisfied: seaborn in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 4)) (0.13.2)
         Requirement already satisfied: biopython in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 5)) (1.87)
         Requirement already satisfied: mermaid-py in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 6)) (0.8.4)
         Requirement already satisfied: ipywidgets in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 7)) (8.1.8)
         Requirement already satisfied: google-drive in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 8)) (0.5.1)
         Requirement already satisfied: ipysheet in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 9)) (0.7.0)
         Requirement already satisfied: ipydatagrid in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 10)) (1.4.0)
         Requirement already satisfied: shinywidgets in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 11)) (0.8.0)
         Requirement already satisfied: altair in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 12)) (6.1.0)
         Requirement already satisfied: bokeh in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 13)) (3.9.0)
         Requirement already satisfied: plotly in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 14)) (6.7.0)
         Requirement already satisfied: ipyleaflet in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 15)) (0.20.0)
         Requirement already satisfied: pydeck==0.8.0 in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 16)) (0.8.0)
         Requirement already satisfied: jupyterlite-pyodide-kernel in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 17)) (0.7.1)
         Requirement already satisfied: jupyter-book>=2.0 in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 18)) (2.1.4)
         Requirement already satisfied: jupyter_server in C:\tools\.venv\Lib\site-packages (from -r requirements.txt (line 19)) (2.17.0)
         Requirement already satisfied: jinja2>=2.10.1 in C:\tools\.venv\Lib\site-packages (from pydeck==0.8.0->-r requirements.txt (line 16)) (3.1.6)
         Requirement already satisfied: contourpy>=1.0.1 in C:\tools\.venv\Lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (1.3.3)
         Requirement already satisfied: cycler>=0.10 in C:\tools\.venv\Lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (0.12.1)
         Requirement already satisfied: fonttools>=4.22.0 in C:\tools\.venv\Lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (4.62.1)
         Requirement already satisfied: kiwisolver>=1.3.1 in C:\tools\.venv\Lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (1.5.0)
         Requirement already satisfied: packaging>=20.0 in C:\tools\.venv\Lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (26.2)
         Requirement already satisfied: pillow>=8 in C:\tools\.venv\Lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (12.2.0)
         Requirement already satisfied: pyparsing>=3 in C:\tools\.venv\Lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (3.3.2)
         Requirement already satisfied: python-dateutil>=2.7 in C:\tools\.venv\Lib\site-packages (from matplotlib->-r requirements.txt (line 3)) (2.9.0.post0)
         Requirement already satisfied: pandas>=1.2 in C:\tools\.venv\Lib\site-packages (from seaborn->-r requirements.txt (line 4)) (2.3.3)
         Requirement already satisfied: requests>=2.32.5 in C:\tools\.venv\Lib\site-packages (from mermaid-py->-r requirements.txt (line 6)) (2.33.1)
         Requirement already satisfied: comm>=0.1.3 in C:\tools\.venv\Lib\site-packages (from ipywidgets->-r requirements.txt (line 7)) (0.2.3)
         Requirement already satisfied: ipython>=6.1.0 in C:\tools\.venv\Lib\site-packages (from ipywidgets->-r requirements.txt (line 7)) (9.13.0)
         Requirement already satisfied: traitlets>=4.3.1 in C:\tools\.venv\Lib\site-packages (from ipywidgets->-r requirements.txt (line 7)) (5.14.3)
         Requirement already satisfied: widgetsnbextension~=4.0.14 in C:\tools\.venv\Lib\site-packages (from ipywidgets->-r requirements.txt (line 7)) (4.0.15)
         Requirement already satisfied: jupyterlab_widgets~=3.0.15 in C:\tools\.venv\Lib\site-packages (from ipywidgets->-r requirements.txt (line 7)) (3.0.16)
         Requirement already satisfied: google-api-core==1.31.5 in C:\tools\.venv\Lib\site-packages (from google-drive->-r requirements.txt (line 8)) (1.31.5)
         Requirement already satisfied: google-api-python-client==2.6.0 in C:\tools\.venv\Lib\site-packages (from google-drive->-r requirements.txt (line 8)) (2.6.0)
         Requirement already satisfied: google-auth==1.35.0 in C:\tools\.venv\Lib\site-packages (from google-drive->-r requirements.txt (line 8)) (1.35.0)
         Requirement already satisfied: google-auth-httplib2==0.1.0 in C:\tools\.venv\Lib\site-packages (from google-drive->-r requirements.txt (line 8)) (0.1.0)
         Requirement already satisfied: google-auth-oauthlib==0.4.1 in C:\tools\.venv\Lib\site-packages (from google-drive->-r requirements.txt (line 8)) (0.4.1)
         Requirement already satisfied: googleapis-common-protos==1.56.0 in C:\tools\.venv\Lib\site-packages (from google-drive->-r requirements.txt (line 8)) (1.56.0)
         Requirement already satisfied: dataclasses==0.6 in C:\tools\.venv\Lib\site-packages (from google-drive->-r requirements.txt (line 8)) (0.6)
         Requirement already satisfied: click==8.1.7 in C:\tools\.venv\Lib\site-packages (from google-drive->-r requirements.txt (line 8)) (8.1.7)
         Requirement already satisfied: colorama in C:\tools\.venv\Lib\site-packages (from click==8.1.7->google-drive->-r requirements.txt (line 8)) (0.4.6)
         Requirement already satisfied: setuptools>=40.3.0 in C:\tools\.venv\Lib\site-packages (from google-api-core==1.31.5->google-drive->-r requirements.txt (line 8)) (82.0.1)
         Requirement already satisfied: six>=1.13.0 in C:\tools\.venv\Lib\site-packages (from google-api-core==1.31.5->google-drive->-r requirements.txt (line 8)) (1.17.0)
         Requirement already satisfied: pytz in C:\tools\.venv\Lib\site-packages (from google-api-core==1.31.5->google-drive->-r requirements.txt (line 8)) (2026.1.post1)
         Requirement already satisfied: protobuf>=3.12.0 in C:\tools\.venv\Lib\site-packages (from google-api-core==1.31.5->google-drive->-r requirements.txt (line 8)) (7.34.1)
         Requirement already satisfied: cachetools<5.0,>=2.0.0 in C:\tools\.venv\Lib\site-packages (from google-auth==1.35.0->google-drive->-r requirements.txt (line 8)) (4.2.4)
         Requirement already satisfied: pyasn1-modules>=0.2.1 in C:\tools\.venv\Lib\site-packages (from google-auth==1.35.0->google-drive->-r requirements.txt (line 8)) (0.4.2)
         Requirement already satisfied: rsa<5,>=3.1.4 in C:\tools\.venv\Lib\site-packages (from google-auth==1.35.0->google-drive->-r requirements.txt (line 8)) (4.9.1)
         Requirement already satisfied: httplib2<1dev,>=0.15.0 in C:\tools\.venv\Lib\site-packages (from google-api-python-client==2.6.0->google-drive->-r requirements.txt (line 8)) (0.31.2)
         Requirement already satisfied: uritemplate<4dev,>=3.0.0 in C:\tools\.venv\Lib\site-packages (from google-api-python-client==2.6.0->google-drive->-r requirements.txt (line 8)) (3.0.1)
         Requirement already satisfied: requests-oauthlib>=0.7.0 in C:\tools\.venv\Lib\site-packages (from google-auth-oauthlib==0.4.1->google-drive->-r requirements.txt (line 8)) (2.0.0)
         Requirement already satisfied: charset_normalizer<4,>=2 in C:\tools\.venv\Lib\site-packages (from requests>=2.32.5->mermaid-py->-r requirements.txt (line 6)) (3.4.7)
         Requirement already satisfied: idna<4,>=2.5 in C:\tools\.venv\Lib\site-packages (from requests>=2.32.5->mermaid-py->-r requirements.txt (line 6)) (3.13)
         Requirement already satisfied: urllib3<3,>=1.26 in C:\tools\.venv\Lib\site-packages (from requests>=2.32.5->mermaid-py->-r requirements.txt (line 6)) (1.26.20)
         Requirement already satisfied: certifi>=2023.5.7 in C:\tools\.venv\Lib\site-packages (from requests>=2.32.5->mermaid-py->-r requirements.txt (line 6)) (2026.4.22)
         Requirement already satisfied: pyasn1>=0.1.3 in C:\tools\.venv\Lib\site-packages (from rsa<5,>=3.1.4->google-auth==1.35.0->google-drive->-r requirements.txt (line 8)) (0.6.3)
         Requirement already satisfied: bqplot>=0.11.6 in C:\tools\.venv\Lib\site-packages (from ipydatagrid->-r requirements.txt (line 10)) (0.12.46)
         Requirement already satisfied: py2vega>=0.5 in C:\tools\.venv\Lib\site-packages (from ipydatagrid->-r requirements.txt (line 10)) (0.7.0)
         Requirement already satisfied: anywidget in C:\tools\.venv\Lib\site-packages (from shinywidgets->-r requirements.txt (line 11)) (0.11.0)
         Requirement already satisfied: jupyter-core in C:\tools\.venv\Lib\site-packages (from shinywidgets->-r requirements.txt (line 11)) (5.9.1)
         Requirement already satisfied: shiny>=0.6.1.9005 in C:\tools\.venv\Lib\site-packages (from shinywidgets->-r requirements.txt (line 11)) (1.6.0)
         Requirement already satisfied: jsonschema>=3.0 in C:\tools\.venv\Lib\site-packages (from altair->-r requirements.txt (line 12)) (4.26.0)
         Requirement already satisfied: narwhals>=2.4.0 in C:\tools\.venv\Lib\site-packages (from altair->-r requirements.txt (line 12)) (2.20.0)
         Requirement already satisfied: typing-extensions>=4.12.0 in C:\tools\.venv\Lib\site-packages (from altair->-r requirements.txt (line 12)) (4.15.0)
         Requirement already satisfied: PyYAML>=3.10 in C:\tools\.venv\Lib\site-packages (from bokeh->-r requirements.txt (line 13)) (6.0.3)
         Requirement already satisfied: tornado>=6.2 in C:\tools\.venv\Lib\site-packages (from bokeh->-r requirements.txt (line 13)) (6.5.5)
         Requirement already satisfied: xyzservices>=2021.09.1 in C:\tools\.venv\Lib\site-packages (from bokeh->-r requirements.txt (line 13)) (2026.3.0)
         Requirement already satisfied: branca>=0.5.0 in C:\tools\.venv\Lib\site-packages (from ipyleaflet->-r requirements.txt (line 15)) (0.8.2)
         Requirement already satisfied: jupyter-leaflet<0.21,>=0.20 in C:\tools\.venv\Lib\site-packages (from ipyleaflet->-r requirements.txt (line 15)) (0.20.0)
         Requirement already satisfied: traittypes<3,>=0.2.1 in C:\tools\.venv\Lib\site-packages (from ipyleaflet->-r requirements.txt (line 15)) (0.2.3)
         Requirement already satisfied: jupyterlite-core<0.8.0,>=0.7.3 in C:\tools\.venv\Lib\site-packages (from jupyterlite-pyodide-kernel->-r requirements.txt (line 17)) (0.7.4)
         Requirement already satisfied: pkginfo in C:\tools\.venv\Lib\site-packages (from jupyterlite-pyodide-kernel->-r requirements.txt (line 17)) (1.12.1.2)
         Requirement already satisfied: doit<1,>=0.34 in C:\tools\.venv\Lib\site-packages (from jupyterlite-core<0.8.0,>=0.7.3->jupyterlite-pyodide-kernel->-r requirements.txt (line 17)) (0.37.0)
         Requirement already satisfied: ipykernel in C:\tools\.venv\Lib\site-packages (from jupyter-book>=2.0->-r requirements.txt (line 18)) (7.2.0)
         Requirement already satisfied: platformdirs>=4.2.2 in C:\tools\.venv\Lib\site-packages (from jupyter-book>=2.0->-r requirements.txt (line 18)) (4.2.2)
         Requirement already satisfied: nodeenv>=1.9.1 in C:\tools\.venv\Lib\site-packages (from jupyter-book>=2.0->-r requirements.txt (line 18)) (1.9.1)
         Requirement already satisfied: anyio>=3.1.0 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (4.13.0)
         Requirement already satisfied: argon2-cffi>=21.1 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (25.1.0)
         Requirement already satisfied: jupyter-client>=7.4.4 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (8.8.0)
         Requirement already satisfied: jupyter-events>=0.11.0 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (0.12.1)
         Requirement already satisfied: jupyter-server-terminals>=0.4.4 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (0.5.4)
         Requirement already satisfied: nbconvert>=6.4.4 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (7.17.1)
         Requirement already satisfied: nbformat>=5.3.0 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (5.10.4)
         Requirement already satisfied: prometheus-client>=0.9 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (0.25.0)
         Requirement already satisfied: pywinpty>=2.0.1 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (3.0.3)
         Requirement already satisfied: pyzmq>=24 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (27.1.0)
         Requirement already satisfied: send2trash>=1.8.2 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (2.1.0)
         Requirement already satisfied: terminado>=0.8.3 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (0.18.1)
         Requirement already satisfied: websocket-client>=1.7 in C:\tools\.venv\Lib\site-packages (from jupyter_server->-r requirements.txt (line 19)) (1.9.0)
         Requirement already satisfied: argon2-cffi-bindings in C:\tools\.venv\Lib\site-packages (from argon2-cffi>=21.1->jupyter_server->-r requirements.txt (line 19)) (25.1.0)
         Requirement already satisfied: tzdata>=2022.7 in C:\tools\.venv\Lib\site-packages (from pandas>=1.2->seaborn->-r requirements.txt (line 4)) (2026.2)
         Requirement already satisfied: decorator>=5.1.0 in C:\tools\.venv\Lib\site-packages (from ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (5.2.1)
         Requirement already satisfied: ipython-pygments-lexers>=1.0.0 in C:\tools\.venv\Lib\site-packages (from ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (1.1.1)
         Requirement already satisfied: jedi>=0.18.2 in C:\tools\.venv\Lib\site-packages (from ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (0.19.2)
         Requirement already satisfied: matplotlib-inline>=0.1.6 in C:\tools\.venv\Lib\site-packages (from ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (0.2.1)
         Requirement already satisfied: prompt_toolkit<3.1.0,>=3.0.41 in C:\tools\.venv\Lib\site-packages (from ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (3.0.52)
         Requirement already satisfied: psutil>=7 in C:\tools\.venv\Lib\site-packages (from ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (7.2.2)
         Requirement already satisfied: pygments>=2.14.0 in C:\tools\.venv\Lib\site-packages (from ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (2.20.0)
         Requirement already satisfied: stack_data>=0.6.0 in C:\tools\.venv\Lib\site-packages (from ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (0.6.3)
         Requirement already satisfied: wcwidth in C:\tools\.venv\Lib\site-packages (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (0.6.0)
         Requirement already satisfied: parso<0.9.0,>=0.8.4 in C:\tools\.venv\Lib\site-packages (from jedi>=0.18.2->ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (0.8.6)
         Requirement already satisfied: MarkupSafe>=2.0 in C:\tools\.venv\Lib\site-packages (from jinja2>=2.10.1->pydeck==0.8.0->-r requirements.txt (line 16)) (3.0.3)
         Requirement already satisfied: attrs>=22.2.0 in C:\tools\.venv\Lib\site-packages (from jsonschema>=3.0->altair->-r requirements.txt (line 12)) (26.1.0)
         Requirement already satisfied: jsonschema-specifications>=2023.03.6 in C:\tools\.venv\Lib\site-packages (from jsonschema>=3.0->altair->-r requirements.txt (line 12)) (2025.9.1)
         Requirement already satisfied: referencing>=0.28.4 in C:\tools\.venv\Lib\site-packages (from jsonschema>=3.0->altair->-r requirements.txt (line 12)) (0.37.0)
         Requirement already satisfied: rpds-py>=0.25.0 in C:\tools\.venv\Lib\site-packages (from jsonschema>=3.0->altair->-r requirements.txt (line 12)) (0.30.0)
         Requirement already satisfied: python-json-logger>=2.0.4 in C:\tools\.venv\Lib\site-packages (from jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (4.1.0)
         Requirement already satisfied: rfc3339-validator in C:\tools\.venv\Lib\site-packages (from jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (0.1.4)
         Requirement already satisfied: rfc3986-validator>=0.1.1 in C:\tools\.venv\Lib\site-packages (from jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (0.1.1)
         Requirement already satisfied: fqdn in C:\tools\.venv\Lib\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (1.5.1)
         Requirement already satisfied: isoduration in C:\tools\.venv\Lib\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (20.11.0)
         Requirement already satisfied: jsonpointer>1.13 in C:\tools\.venv\Lib\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (3.1.1)
         Requirement already satisfied: rfc3987-syntax>=1.1.0 in C:\tools\.venv\Lib\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (1.1.0)
         Requirement already satisfied: uri-template in C:\tools\.venv\Lib\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (1.3.0)
         Requirement already satisfied: webcolors>=24.6.0 in C:\tools\.venv\Lib\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (25.10.0)
         Requirement already satisfied: beautifulsoup4 in C:\tools\.venv\Lib\site-packages (from nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (4.14.3)
         Requirement already satisfied: bleach!=5.0.0 in C:\tools\.venv\Lib\site-packages (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (6.3.0)
         Requirement already satisfied: defusedxml in C:\tools\.venv\Lib\site-packages (from nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (0.7.1)
         Requirement already satisfied: jupyterlab-pygments in C:\tools\.venv\Lib\site-packages (from nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (0.3.0)
         Requirement already satisfied: mistune<4,>=2.0.3 in C:\tools\.venv\Lib\site-packages (from nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (3.2.0)
         Requirement already satisfied: nbclient>=0.5.0 in C:\tools\.venv\Lib\site-packages (from nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (0.10.4)
         Requirement already satisfied: pandocfilters>=1.4.1 in C:\tools\.venv\Lib\site-packages (from nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (1.5.1)
         Requirement already satisfied: webencodings in C:\tools\.venv\Lib\site-packages (from bleach!=5.0.0->bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (0.5.1)
         Requirement already satisfied: tinycss2<1.5,>=1.1.0 in C:\tools\.venv\Lib\site-packages (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (1.4.0)
         Requirement already satisfied: fastjsonschema>=2.15 in C:\tools\.venv\Lib\site-packages (from nbformat>=5.3.0->jupyter_server->-r requirements.txt (line 19)) (2.21.2)
         Requirement already satisfied: gast<0.8,>=0.7.0 in C:\tools\.venv\Lib\site-packages (from py2vega>=0.5->ipydatagrid->-r requirements.txt (line 10)) (0.7.0)
         Requirement already satisfied: oauthlib>=3.0.0 in C:\tools\.venv\Lib\site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib==0.4.1->google-drive->-r requirements.txt (line 8)) (3.3.1)
         Requirement already satisfied: lark>=1.2.2 in C:\tools\.venv\Lib\site-packages (from rfc3987-syntax>=1.1.0->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (1.3.1)
         Requirement already satisfied: uvicorn>=0.16.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (0.46.0)
         Requirement already satisfied: starlette in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (1.0.0)
         Requirement already satisfied: websockets>=13.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (16.0)
         Requirement already satisfied: htmltools>=0.6.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (0.6.0)
         Requirement already satisfied: markdown-it-py>=1.1.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (4.0.0)
         Requirement already satisfied: mdit-py-plugins>=0.3.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (0.5.0)
         Requirement already satisfied: linkify-it-py>=1.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (2.1.0)
         Requirement already satisfied: asgiref>=3.5.2 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (3.11.1)
         Requirement already satisfied: watchfiles>=0.18.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (1.1.1)
         Requirement already satisfied: questionary>=2.0.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (2.1.1)
         Requirement already satisfied: python-multipart>=0.0.7 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (0.0.27)
         Requirement already satisfied: orjson>=3.10.7 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (3.11.8)
         Requirement already satisfied: shinychat>=0.1.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (0.2.9)
         Requirement already satisfied: opentelemetry-api>=1.20.0 in C:\tools\.venv\Lib\site-packages (from shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (1.41.1)
         Requirement already satisfied: uc-micro-py in C:\tools\.venv\Lib\site-packages (from linkify-it-py>=1.0->shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (2.0.0)
         Requirement already satisfied: mdurl~=0.1 in C:\tools\.venv\Lib\site-packages (from markdown-it-py>=1.1.0->shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (0.1.2)
         Requirement already satisfied: importlib-metadata<8.8.0,>=6.0 in C:\tools\.venv\Lib\site-packages (from opentelemetry-api>=1.20.0->shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (8.7.1)
         Requirement already satisfied: zipp>=3.20 in C:\tools\.venv\Lib\site-packages (from importlib-metadata<8.8.0,>=6.0->opentelemetry-api>=1.20.0->shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (3.23.1)
         Requirement already satisfied: executing>=1.2.0 in C:\tools\.venv\Lib\site-packages (from stack_data>=0.6.0->ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (2.2.1)
         Requirement already satisfied: asttokens>=2.1.0 in C:\tools\.venv\Lib\site-packages (from stack_data>=0.6.0->ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (3.0.1)
         Requirement already satisfied: pure-eval in C:\tools\.venv\Lib\site-packages (from stack_data>=0.6.0->ipython>=6.1.0->ipywidgets->-r requirements.txt (line 7)) (0.2.3)
         Requirement already satisfied: h11>=0.8 in C:\tools\.venv\Lib\site-packages (from uvicorn>=0.16.0->shiny>=0.6.1.9005->shinywidgets->-r requirements.txt (line 11)) (0.16.0)
         Requirement already satisfied: psygnal>=0.8.1 in C:\tools\.venv\Lib\site-packages (from anywidget->shinywidgets->-r requirements.txt (line 11)) (0.15.1)
         Requirement already satisfied: cffi>=1.0.1 in C:\tools\.venv\Lib\site-packages (from argon2-cffi-bindings->argon2-cffi>=21.1->jupyter_server->-r requirements.txt (line 19)) (2.0.0)
         Requirement already satisfied: pycparser in C:\tools\.venv\Lib\site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi>=21.1->jupyter_server->-r requirements.txt (line 19)) (3.0)
         Requirement already satisfied: soupsieve>=1.6.1 in C:\tools\.venv\Lib\site-packages (from beautifulsoup4->nbconvert>=6.4.4->jupyter_server->-r requirements.txt (line 19)) (2.8.3)
         Requirement already satisfied: debugpy>=1.6.5 in C:\tools\.venv\Lib\site-packages (from ipykernel->jupyter-book>=2.0->-r requirements.txt (line 18)) (1.8.20)
         Requirement already satisfied: nest-asyncio>=1.4 in C:\tools\.venv\Lib\site-packages (from ipykernel->jupyter-book>=2.0->-r requirements.txt (line 18)) (1.6.0)
         Requirement already satisfied: arrow>=0.15.0 in C:\tools\.venv\Lib\site-packages (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter_server->-r requirements.txt (line 19)) (1.4.0)
         Note: you may need to restart the kernel to use updated packages.

   .. container:: output stream stderr

      ::

         WARNING: Ignoring invalid distribution ~otebook (C:\tools\.venv\Lib\site-packages)
         WARNING: Ignoring invalid distribution ~otebook (C:\tools\.venv\Lib\site-packages)
         WARNING: Ignoring invalid distribution ~otebook (C:\tools\.venv\Lib\site-packages)

.. container:: cell code
   :name: b43de98b-fdd5-4982-8b49-111c6a60bcc5

   .. code:: python

      ignore = f""".venv/
      */*.gsheet
      */*.gdoc"""

      gitignore = ['.venv/', '.gsheet', '.gdoc']
      ignore = "\n".join(gitignore)
      with open(f"./.gitignore", "w") as f:
          f.write(ignore)

.. container:: cell markdown
   :name: f1cedad7-1235-4008-9dbb-5f34414c77bd

   Import the necessary modules.

.. container:: cell code
   :name: ee98e7bc-08ac-45ca-b0fd-bacd14a99af3

   .. code:: python

      import subprocess
      import sys
      import os
      from Bio import Entrez, Medline
      import ssl
      import certifi
      import re
      from pathlib import Path

.. container:: cell code
   :name: def2aff0-5673-4673-a151-304dcbb0d2f7

   .. code:: python

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
      "manuscript": f"{root}/manuscript"    
      }

      for var, f in folders.items():
          relative = "./"
          absolute = os.getcwd()
          directory = Path(f)
          globals()[f"{var}"] = directory
          path = Path(relative, directory)
          os.makedirs(path, exist_ok = True)

.. container:: cell code
   :name: 6b17992c-d672-4e73-a649-bda3ed872e39

   .. code:: python

      def csv2df(filename, folders):
          filename = f"{filename.strip()}"
          for x, y in folders.items():
              try:
                  while True:
                      df = pd.read_csv(f"{y}/{filename}.csv", encoding = "utf-8")
              except:
                  continue
                      
          globals()[f"{filename}"] = pd.DataFrame(df)
          print(df.head())
          return filename

.. container:: cell markdown
   :name: 7d195cc2-e9cd-4d8b-9212-4678d60a6f14

   | `top <#toc>`__ \| `next <#search>`__
   | `search strategy <#search-strategy>`__ \| `search <#search>`__ \|
     `deduplication <#deduplication>`__ \| `screening <#screening>`__

   .. raw:: html

      <div>
          <h1 align="center" style="font-family:Times New Roman;font-variant:small-caps;">
                      Systematic Review
          </h1>
      </div>

.. container:: cell markdown
   :name: 9a091f2f-b92c-444a-8f29-3b0ab9f584fd

   .. raw:: html

      <div align="center">
          <h2 align="center" style="font-family:Times New Roman;font-variant: small-caps;">
              Search Strategy
          </h2>
          </br>
      </div>

   .. raw:: html

      <p>
          Search strategies were developed for randomized controlled trials: `pm_bptb.txt`, `pm_ht.txt`, `pm_qt.txt`, `pm_plt.txt`, `pm_at.txt` and `pm_ta.txt` corresponding to PubMed search strategies for patellar, hamstring, quadriceps, peroneus longus, achilles and tibialis anterior and posterior tendones, respectively. From the protocol that was developed, extract key terms from the eligibility criteria for inclusion and exclusion of studies in order to develop a *search strategy*.
      </p>

   .. raw:: html

      <p>
          The search strategies were 'translated' via regular expressions from PubMed syntax to Embase and Web of Science syntax, store them into the global environment, and save them as plain text files for importing and use as queries for search.
      </p>

   **Search strategies**

   +-------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **P** | Population   | ``NOT (("pediatric"[tiab] OR "paediatric"[tiab]) OR ("revision"[tiab] OR "repair"[tiab]))``                                                                                                                                                                        |
   +-------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **I** | Intervention | ``("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab])``                                                                                                                   |
   +-------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **C** | Comparators  | ``("bone-patellar tendon-bone"[tiab] OR "patellar tendon"[tiab] OR "bptb"[tiab])`` ``("hamstring tendon"[tiab] OR "semitendinosus"[tiab] OR "gracilis"[tiab])`` ``("quadriceps"[tiab] OR "quadriceps tendon"[tiab] OR "qt"[tiab])``                                |
   |       |              | ``("peroneus longus"[tiab] OR "fibularis longus"[tiab])`` ``("achilles"[tiab])`` ``("tibialis anterior"[tiab] OR "tibialis posterior"[tiab]``                                                                                                                      |
   +-------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **O** | Outcomes     | ``("ikdc"[tiab] OR "lysholm"[tiab] OR "tegner"[tiab] OR (("instrumental laxity"[tiab] OR "kt-1000"[tiab] OR "kt-2000"[tiab] OR "rolimeter"[tiab]) OR "pivot shift"[tiab] OR "lachman"[tiab]) OR ("graft failure"[tiab] OR "graft rupture"[tiab]))``                |
   +-------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **S** | Study design | ``("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab]) NOT ("review"[pt] OR "review"[tiab] OR "systematic review"[pt] OR "systematic review"[tiab] OR "meta-analysis"[pt] OR "meta-analysis"[tiab])`` |
   +-------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. container:: cell code
   :name: 40b2e50d-ae01-4fe6-b6cb-7c9254d1288d

   .. code:: python

      acl = f"""("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab])"""
      rct = f"""("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab])"""
      reviews = f"""("review"[pt] OR "review"[tiab] OR "systematic review"[pt] OR "systematic review"[tiab] OR "meta-analysis"[pt] OR "meta-analysis"[tiab])"""
      outcomes = f"""("ikdc"[tiab] OR "lysholm"[tiab] OR "tegner"[tiab] OR (("instrumental laxity"[tiab] OR "kt-1000"[tiab] OR "kt-2000"[tiab] OR "rolimeter"[tiab]) OR "pivot shift"[tiab] OR "lachman"[tiab]) OR ("graft failure"[tiab] OR "graft rupture"[tiab]))"""

      bptb = f"""("bone-patellar tendon-bone"[tiab] OR "patellar tendon"[tiab] OR "bptb"[tiab])"""
      ht = f"""("hamstring tendon"[tiab] OR "semitendinosus"[tiab] OR "gracilis"[tiab])"""
      qt = f"""("quadriceps"[tiab] OR "quadriceps tendon"[tiab] OR "qt"[tiab])"""
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

.. container:: cell code
   :name: c87f8e5c-7b36-4ad0-8bf0-0bd897221065

   .. code:: python

      import ipywidgets as widgets
      from IPython.display import display, clear_output

      entries = []

      term_input = widgets.Text(
          placeholder="Search term",
          layout = widgets.Layout(width="75%")
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
      save_button = widgets.Button(description="Save", icon="save")

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
          filepath = f"./data/{filename}.txt"

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

   .. container:: output display_data

      .. code:: json

         {"model_id":"7032ac33c33541849487bc30b3b43887","version_major":2,"version_minor":0}

.. container:: cell markdown
   :name: d8fea9ab-4fbc-4357-b3fa-9777c1b5b977

   | `previous <#search-strategy>`__ \| `top <#toc>`__ \|
     `next <#deduplication>`__
   | `search strategy <#search-strategy>`__ \| `search <#search>`__ \|
     `deduplication <#deduplication>`__ \| `screening <#screening>`__

   .. raw:: html

      <!--
      <div align="center"><font size="5" style="font-family:Times New Roman;font-variant: small-caps;">Search</font><br></div>
      -->

   .. raw:: html

      <h2 align="center" style="font-family:Times New Roman;font-variant:small-caps;">Search</h2>

   --------------

.. container:: cell markdown
   :name: 2a081847-333d-47ed-bdcc-3fbdbd45b078

   A script to either create a search strategy using the terms, field
   tags, and Boolean operators and save them as plain text files or load
   already written and saved plain text files for import into the API
   search scripts. This uses the search strategies (e.g.,
   ``pm_bptb.txt``, search strategy in plain text written in PubMed
   syntax for bone-patellar tendon-bone (BPTB) subgroup search) and
   pulls data from PubMed to output PMIDs (``pmid_pm_bptb.txt``) and
   search results in XML (``pm_bptb.xml``) and parses this into CSV
   files (``pm_bptb.csv``).

.. container:: cell code
   :name: 1fda7696-1363-48ba-8834-abf37cf86cb9

   .. code:: python

      ssl._create_default_https_context = lambda: ssl.create_default_context(
          cafile=certifi.where()
      )

      # create search strategy using structured inputs

      question = input("Do you already have a search strategy file saved?") # get rid of this
      filename = input("Enter the file name of the search strategy: ") # use file upload widget ! and present the results as data table widgets !!! 
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

.. container:: cell markdown
   :name: 2874372b-6f87-482f-9b32-4b1cdf673499

   The CSV files from the three databases were now cleaned, prepared,
   and transformed; this is otherwise known as 'data wrangling' in Data
   Science.

   | Step 1: import the 18 datasets for each subgroup from database
     search.
   | Step 2: rename the columns for each dataset and merge them into 3
     separate datasets, one for each database.
   | Step 3: merge the datasets, with matching columns into 1 dataset.
   | Step 4: clean and prepare the records dataset (as it is the most
     important output).
   | Step 5: save records as csv files into the appropriate directory.

.. container:: cell markdown
   :name: 820fad24-3a40-4d2d-9cc3-69f2f40a1c96

   .. code:: mermaid

      ---
      config:
        theme: light
        curve: step
      ---

      flowchart LR

      A01["`**RCT**<br>rct_pm_bptb`"]
      B01["`**RCT**<br>rct_pm_ht`"]
      C01["`**RCT**<br>rct_pm_qt`"]
      D01["`**RCT**<br>rct_pm_plt`"]
      E01["`**RCT**<br>rct_pm_at`"]
      F01["`**RCT**<br>rct_pm_ta`"]

      A02["reviews_pm_bptb"]
      B02["reviews_pm_ht"]
      C02["reviews_pm_qt"]
      D02["reviews_pm_plt"]
      E02["reviews_pm_at"]
      F02["reviews_pm_ta"]

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

       
      A02 & A01 --> A1
      B02 & B01 --> B1
      C02 & C01 --> C1
      D02 & D01 --> D1
      E02 & E01 --> E1
      F02 & F01 --> F1

      A1 & B1 & C1 & D1 & E1 & F1 --> G
      A2 & B2 & C2 & D2 & E2 & F2 --> H
      A3 & B3 & C3 & D3 & E3 & F3 --> I

      G & H & I --> J["records"]

.. container:: cell markdown
   :name: c3358e33-3d57-4002-a570-1269cd09191e

   Step 1: import the 18 datasets for each subgroup from database search
   and load them into the global environment.

.. container:: cell code
   :name: b86f9620-b237-43fb-9363-8a58c8e3aeac

   .. code:: python


      subgroups = {
          "bptb": "patellar",
          "ht": "hamstring",
          "qt": "quadriceps",
          "plt": "peroneus",
          "at": "achilles",
          "ta": "tibialis"}

      for x, y in subgroups.items():
          df = pd.read_csv(f"{search}/wos/tsv/wos_{x}.tsv", sep = '\t', encoding = "latin-1")
          df.to_csv(f"{search}/wos/wos_{x}.csv", encoding = "utf-8", sep = ",", index = False)
          globals()[f"wos_{x}"] = df

      databases = {"pm": "pubmed", 
                   "em": "embase", 
                   "wos": "wos"}

      subgroups = {"bptb": "patellar", 
                   "ht": "hamstring", 
                   "qt": "quadriceps", 
                   "plt": "peroneus", 
                   "at": "achilles", 
                   "ta": "tibialis"}

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
              globals()[f"{b}"] = data # saving as variables

.. container:: cell markdown
   :name: 0eaf9def-5173-48d8-b4c3-84a58cf2de8b

   Step 2: rename the columns for each dataset and merge them into 3
   separate datasets, one for each database.

.. container:: cell code
   :name: 636d0011-31ef-4fb2-a8ad-fc642240ca0b

   .. code:: python

      databases = {"pm": "pubmed", 
                   "em": "embase", 
                   "wos": "wos"}

      subgroups = {"bptb": "patellar", 
                   "ht": "hamstring", 
                   "qt": "quadriceps", 
                   "plt": "peroneus", 
                   "at": "achilles", 
                   "ta": "tibialis"}

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
      	"Open URL Link" : "open_url_link",
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

.. container:: cell code
   :name: abbcf18f-b967-49b3-b70e-2cd25a8b7cfc

   .. code:: python

      a = len(pubmed)
      b = len(embase)
      c = len(wos)

      a + b + c

   .. container:: output execute_result

      ::

         1563

.. container:: cell markdown
   :name: 49b73d68-0b95-4783-9a72-36d69977ef0c

   .. rubric:: Step 3: clean and prepare the datasets before merging
      them into 1 dataset.
      :name: step-3-clean-and-prepare-the-datasets-before-merging-them-into-1-dataset

.. container:: cell code
   :name: 5f6c87a8-7a76-49b1-98ac-b47e21dc699f

   .. code:: python

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
              "authors": var["authors"].str.replace(r"[\['\]]","",regex=True),
              "journal": var["journal"],
              "title": var["title"],
              "abstract": var["abstract"],
              "year": var["year"],
              "language": var["language"]
          })
          df['pmid'] = df['pmid'].astype(str)
          df['language'] = df['language'].str.replace(r"[\'\[\]]","", regex = True)
          df.fillna("")
          globals()[f"{text}"] = df


      # authors
      pubmed["first_author"] = pubmed["authors"].str.replace(r"[\'\[\].;]","", regex = True).str.split(r",\s*").str[0]
      pubmed["second_author"] = pubmed["authors"].str.replace(r"[\'\[\].;]","", regex = True).str.split(r",\s*").str[1]

      embase["authors"] = embase["authors"].str.replace(r"\.", "", regex = True)
      embase["first_author"] = embase["authors"].str.replace(r"[\'\[\].;]","", regex = True).str.split(r",\s*").str[0]
      embase["second_author"] = embase["authors"].str.replace(r"[\'\[\].;]","", regex = True).str.split(r",\s*").str[1]

      wos["authors"] = wos["authors"].str.replace(r",","", regex = True)
      wos["authors"] = wos["authors"].str.replace(r";",",", regex = True)
      wos["first_author"] = wos["authors"].str.replace(r"[\'\[\].;]","", regex = True).str.split(r",\s*").str[0]
      wos["second_author"] = wos["authors"].str.replace(r"[\'\[\].;]","", regex = True).str.split(r",\s*").str[1]

      pubmed.head()

.. container:: cell code
   :name: 24d92b75-3253-4a8c-9f78-0b04e7ba9813

   .. code:: python

      pubmed['authors'] = pubmed['authors'].str.replace(r"[\'\[\]]","", regex = True)
      pubmed['journal'] = pubmed['journal'].str.replace(r"[\'\[,\]]","", regex = True)
      pubmed['journal'] = pubmed['journal'].str.replace(r"\(.*?\)","", regex=True)
      pubmed['journal'] = pubmed['journal'].str.capitalize()

      embase['doi'] = embase['doi'].fillna("")
      embase['pmid'] = embase['pmid'].fillna("")
      pubmed['journal'] = pubmed['journal'].str.replace(r"\(.*?\)","", regex=True)
      embase['journal'] = embase['journal'].str.replace(r"[\'\[,\]]","", regex = True)
      embase['journal'] = embase['journal'].str.capitalize()

      wos['journal'] = wos['journal'].str.replace(r"[\'\[\]]","", regex = True)
      wos['journal'] = wos['journal'].str.capitalize()

      records = pd.concat([pubmed, embase, wos], ignore_index = True)

.. container:: cell markdown
   :name: 61ff45f8-4c21-450a-a78e-a6e70c4e47ad

   Step 5: Clean and prepare the records dataset for the next stage.

.. container:: cell code
   :name: d5b16909-d345-4034-a910-dfe86e07ca4a

   .. code:: python

      wos.head()

.. container:: cell code
   :name: 92773818-cb1d-4856-85c1-a636f851cc1b

   .. code:: python

      records['short_title'] = records['title'].str.replace(r'[\[\]\s,.;-]','',regex = True).str.lower().str[:60]
      records['title+author+year'] = records['first_author'] + '+' + records['short_title'] + '+' + records['year'].astype(str)
      records['title+year'] = records['short_title'] + '+' + records['year'].astype(str)
      records['language'] = records['language'].str.replace(r"[\'\[\]]","", regex = True)
      records["subgroup"] = records["subgroup"].str.upper()
      records["doi_url"] = f"https://doi.org/" + records["doi"]
      records["pmid_url"] = "https://pubmed.ncbi.nlm.nih.gov/" + records["pmid"].astype(str) + "/"
      records["study"] = records['first_author'] + " (" + records['year'].astype(str) + ")"
      records = records[["id", "study", "subgroup", "authors", "first_author", "title", "short_title", "abstract", "year", "language", "journal", "source", "doi", "doi_url", "pmid", "pmid_url", "title+author+year", "title+year"]]

      records['year'] = records['year'].astype(str)
      records['pmid'] = round(records['pmid'],0)
      records['pmid'] = records['pmid'].astype(str)
      records['first_author'] = records['first_author'].astype(str)
      records['year'] = records['year'].astype(str)
      records.rename(columns = {"id":"source_id"}, inplace = True)
      records["id"] = range(1,len(records)+1)
      records = records[["id", "source_id", "study", "subgroup", "authors", "first_author", "title", "short_title", "abstract", "year", "language", "journal", "source", "doi", "doi_url", "pmid", "pmid_url",  "title+author+year", "title+year"]]

      records['first_author'] = authors_split.str[0].str.strip().str.split().str[0]
      records['second_author'] = authors_split.str[1].fillna('').str.strip().str.split().str[0]
      records['num_authors'] = authors_split.str.len()

      records.loc[records['num_authors'] >= 3, 'study'] = (
          records['first_author'] + ' et al. (' + records['year'].astype(str) + ')'
      )

      records = records.sort_values(by = ['subgroup', 'year', 'authors'])
      records["authors"] = records["authors"].fillna("")
      records = records.fillna("")
      records = records.sort_values(by = ['authors'])
      records = records.sort_values(by = ['subgroup'])
      records = records.sort_values(by = ['year'], ascending = False)
      records.to_csv(f"{search}/records.csv", encoding= "utf-8")
      records.to_csv(f"{deduplication}/records.csv", encoding = "utf-8")

.. container:: cell markdown
   :name: c20c9b3e-2bc9-4a7b-8c58-6128b1443c73

   | `previous <#search>`__ \| `top <#toc>`__ \| `next <#screening>`__
   | `search strategy <#search-strategy>`__ \| `search <#search>`__ \|
     `deduplication <#deduplication>`__ \| `screening <#screening>`__

   Deduplication

.. container:: cell markdown
   :name: e46b858e-9906-4721-9652-ac052cde0457

   The 'gold-standard' or consensus agreement among researchers seems to
   converge on the idea that removal of duplicate records is best
   performed in a process that involves three ordered stages. The first
   is deduplication based on a unique record identifier, such as a
   digital object identifier (DOI) number, PubMed identifier (PMID)
   number, or clinicaltrials.gov (NCT) number. Then, as according to as
   described for the second stage, the remaining records were
   deduplicated based on a concatenated column consisting of the title,
   author, and year. The title was standardized by converting to
   sentence case, and punctuation marks and white spaces were removed.
   The character length was decreased to 50. For the authors column, the
   last name of the first author was chosen to be used. For the year of
   publication, the year was extracted from the date of publication in
   the electronic version of the journal and converted into a string
   data structure.

   input file(s): ``records.csv``, output file(s):
   ``doi_deduplicated.csv``, ``pmid_deduplicated.csv``,
   ``title+author+year_deduplicated.csv``, and
   ``title+year_deduplicated.csv``.

.. container:: cell code
   :name: c5865181-766d-478a-8a8d-81d5a275c3ed

   .. code:: python

      import pandas as pd
      import mermaid
      import os

      input_file_name = f"{root}/systematic_review/deduplication/records.csv"

      #input_file_name = f"{deduplication}/" + input('Enter file name: ') + '.csv'

      deduplication = f"{root}/systematic_review/deduplication",

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

      output_file_name = f"{deduplication}/deduplicated.csv"
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

   .. container:: output error

      ::

         ---------------------------------------------------------------------------
         NameError                                 Traceback (most recent call last)
         Cell In[1], line 5
               1 import pandas as pd
               2 import mermaid
               3 import os
               4 
         ----> 5 input_file_name = f"{root}/systematic_review/deduplication/records.csv"
               6 
               7 #input_file_name = f"{deduplication}/" + input('Enter file name: ') + '.csv'
               8 

         NameError: name 'root' is not defined

.. container:: cell markdown
   :name: 8b0bd931-14da-4011-84c9-b04838cb0ddf

   `top <#toc>`__ \| `search strategy <#search-strategy>`__ \|
   `search <#search>`__ \| `deduplication <#deduplication>`__ \|
   `screening <#screening>`__ \| `data collection <#data-collection>`__
   \|

   .. raw:: html

      <h2 align="center" style="font-family:Times New Roman;font-variant: small-caps;">Screening</h2>

   --------------

.. container:: cell markdown
   :name: bd194488-5c7f-4acc-98cd-439c6dc13927

   .. raw:: html

      <h3 align="center" style="font-family:Times New Roman;font-variant:small-caps;">Title abstract screening</h3>

.. container:: cell code
   :name: 45cf4438-250c-4ec9-80eb-8dfc86ac1c51

   .. code:: python

      %pip install -q ipywidgets
      import ipywidgets as widgets
      import pandas as pd

      df = csv2df('records')

      df = pd.read_csv(f"./records.csv", encoding = "utf-8")
      columns = df.columns
      ", ".join(columns)

      text = f"""id, source_id, study, subgroup, authors, first_author, title, short_title, abstract, year, language, journal, source, doi, doi_url, pmid, pmid_url, title+author+year, title+year, second_author, num_authors'"""
      list = text.split(", ")
      list

      A = widgets.IntText(value=0, description="Study ID ", layout={"width":"20%"})
      B = widgets.HTML(value="", layout={"width":"80%", "height":"100%"})
      C = widgets.HTML(value="", layout={"width":"80%", "height":"100%"})

      def update(change):
          title = df.loc[df["id"] == A.value, "title"]
          abstract = df.loc[df["id"] == A.value, "abstract"]

          if  A.value > 0:
              B.value = f"<p>{str(title.iloc[0])}</p>"
              C.value = f"<p>{str(abstract.iloc[0])}</p>"
          else:
              B.value = ""
              C.value = ""

      A.observe(update, names="value")

      Yes = widgets.Button(value = "Yes", description = "Yes")
      Maybe = widgets.Button(value = "Maybe", description = "Maybe")
      No = widgets.Button(value = "No", description = "No")

      Label = widgets.Label(value = "Result of Title / Abstract screening ")
      items = [A, Label, Yes, No]

      D = widgets.HBox(items, layout = {"width":"100%"})

      screening = display(D, B, C)
      update(None)

   .. container:: output stream stdout

      ::

         Note: you may need to restart the kernel to use updated packages.

   .. container:: output error

      ::

         ---------------------------------------------------------------------------
         NameError                                 Traceback (most recent call last)
         Cell In[12], line 5
               1 get_ipython().run_line_magic('pip', 'install -q ipywidgets')
               2 import ipywidgets as widgets
               3 import pandas as pd
               4 
         ----> 5 df = csv2df('records')
               6 
               7 df = pd.read_csv(f"./records.csv", encoding = "utf-8")
               8 columns = df.columns

         NameError: name 'csv2df' is not defined

.. container:: cell markdown
   :name: ca452bbe-8098-40e0-8247-fca3c19a3cb5

   Screening filter #1: Language

.. container:: cell code
   :name: fb242547-5f5e-498c-ad9b-a1c477fa67a1

   .. code:: python

      df = pd.read_csv(f"{deduplication}/title+year_deduplicated.csv", encoding = "utf-8")
                      
      df.to_csv(f"{screening}/screening.csv", encoding = "utf-8")
      df.sort_values(by = ['subgroup', 'year', 'authors'])

      dict = {"language": "English"}
      import pandas as pd
      import os
      print(df['pmid'])
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

.. container:: cell code
   :name: 127c57bf-5f14-49c3-82f4-af43f5ecf722

   .. code:: python

      df.head()

.. container:: cell markdown
   :name: 6cf283b8-9cc2-495a-987a-5b3638920114

   Screening filter #2: Randomized controlled trials

.. container:: cell code
   :name: 3730dea5-134e-494c-b844-98536ce004ec

   .. code:: python

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

.. container:: cell markdown
   :name: 3031adfe-3342-4a7f-b4bf-b09009015410

   Screening filter #3: Clinical trials (unpublished and without
   results)

.. container:: cell code
   :name: 5551acb4-5e0a-4803-8cd4-21ffe9485a72

   .. code:: python

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

.. container:: cell code
   :name: d9f10964-7af6-4eb1-bb41-e80c8daf2c64

   .. code:: python

      df = false
      df.to_csv(f"{full_text}/full_text_screening.csv", encoding = "utf-8")

.. container:: cell markdown
   :name: c74c4fef-41b9-4342-b4ae-b62f07d1aa73

   --------------

   `top <#toc>`__ \| `search strategy <#search-strategy>`__ \|
   `search <#search>`__ \| `deduplication <#deduplication>`__ \|
   `screening <#screening>`__ \| `data collection <#data-collection>`__
   \|

   .. raw:: html

      <h3 align="center" style="font-family:Times New Roman;font-variant:small-caps;">Full-text screening</h3>

.. container:: cell code
   :name: e626312b-5614-4dcd-9d4f-0b5fd68dba8c

   .. code:: python

      import requests
      import pandas as pd

      df = pd.read_csv(f"{full_text}/full_text_screening.csv", encoding = "utf-8")

      doi = df["doi"].fillna("").str.strip()
      print(doi)

      #sci = df["doi"].where(df["year"]==2010).dropna()

      downloads = []
      views = []
      for x in doi:
          base = f"sci.bban.top/pdf" # options = sci-hub.al
          download = f"https://{base}/{x}.pdf?download=true"
          view = f"https://{base}/{x}.pdf"
          downloads.append(download)
          views.append(view)

      df["pdf.download"] = downloads
      df["pdf.view"] = views
      df.to_csv(f"{screening}/PDF/pdf.csv", encoding = "utf-8")
      df.to_csv(f"{screening}/PDF/pdf.csv", encoding = "utf-8")
      df.head()
      display(df)

.. container:: cell markdown
   :name: d29e63bb-749b-4ea5-8ad0-5149aed21951

   --------------

   `top <#toc>`__ \| `search strategy <#search-strategy>`__ \|
   `search <#search>`__ \| `deduplication <#deduplication>`__ \|
   `screening <#screening>`__ \| `data collection <#data-collection>`__
   \|

   .. raw:: html

      <h1 align="center" style="font-family:Times New Roman;font-variant:small-caps;">Data Collection</h1>

.. container:: cell markdown
   :name: 783c60cf-218a-4048-afb1-1bec22c6923c

   Data collection involves database design and creation, data entry
   forms design and creation, then data collection, also known as data
   extraction.

.. container:: cell code
   :name: 9fa1c3ad-b1c0-426a-a86d-09a0bca4bb77

   .. code:: python

      df = csv2df("pdf")

.. container:: cell code
   :name: 0f208222-8f2f-422f-b501-148ef8d1e835

   .. code:: python

      import ipywidgets as widgets
      from ipyflex import FlexLayout
      from IPython.display import display, Latex, HTML

.. container:: cell code
   :name: 59ca5e30-b165-43cf-aca2-8467a35538a8

   .. code:: python

      df = csv2df("records")
      df.head()

.. container:: cell markdown
   :name: 1803f402-0746-418d-b74a-1b92d9f851ed

   Forms

.. container:: cell markdown
   :name: 7f067fb6-89c6-4f23-b706-0cce05595bc8

   - `Views <#views>`__

     - `Layout <#layouts>`__
     - `Containers <#containers>`__
     - `Widgets <./src/notebooks/data/components.ipynb>`__

   - `Compose <#compose>`__

     - `Linking <#linking>`__

   - `Models <#models>`__

.. container:: cell markdown
   :name: 5d6e3f85-22ac-4794-be95-4bc1f20aa588

   .. rubric:: Views
      :name: views

.. container:: cell markdown
   :name: a7ab9573-00bb-42d3-b2d6-6d4d91e0ccae

   **Linking** widgets' attributes from the client side

.. container:: cell code
   :name: 4ecfefba-052d-462c-9e72-90719615a710

   .. code:: python

      grid = widgets.Grid()

.. container:: cell code
   :name: b42fd8ae-99b6-4e3c-bf9a-13255c408ceb

   .. code:: python

.. container:: cell markdown
   :name: d3643c61-8671-48fd-a73c-a42e9027cb27

.. container:: cell code
   :name: 1122e951-064f-46ee-95c1-6294b3591f39

   .. code:: python

.. container:: cell code
   :name: f31098f7-c621-4c2f-8f71-eb294419e654

   .. code:: python

.. container:: cell code
   :name: 69c23da5-517e-45e9-a2c8-ff21f7ef9afd

   .. code:: python

.. |image1| image:: 643bd2068a442fe31afb7444cbd3374956d08db0.png
