===========================================================================================================================================================
Comparative analysis of outcome measures using the most commonly used graft harvesting sources in primary anterior cruciate ligament reconstruction surgery
===========================================================================================================================================================
A systematic review and network meta-analysis
---------------------------------------------
:Authors: 
    Dong Woon Kim, M.D.,
    Konrad Malinowski, M.D., Ph.D.
:Version: 1.0.0 of 2026/23/07
:Description: Documentation for python code and scripts used in the project. Written in rST syntax and published `online <https://d-wkim-project.readthedocs.io/en/latest/README.html>`_.

.. contents:: Table of Contents
   :local:
   :depth: 5


.. raw:: html
   
   <p align = "center">
    Jagiellonian University<br>
    Medical College<br>
    Doctoral School of Medical and Health Sciences</p>

    <div  align="center" ><a href="https://github.com/d-wkim/phd"><img alt = "" src="https://raw.githubusercontent.com/d-wkim/assets/refs/heads/main/icons/uj_black.jpg" width="100" height="150"></a></div>

   <h2 align="center">
    Comparative analysis of outcome measures using the most commonly used graft harvesting sources in primary anterior cruciate ligament reconstruction surgery.<br>
    A systematic review and network meta-analysis
   </h2>
   <p align = "center">
    <sub>A dissertation submitted in partial fulfillment of the requirements for the award of the degree of:</sub><br><br>
    Doctor of Philosophy (Ph.D.)<br><br>
    <sup>submitted by:</sup><br>
    <strong>Dong Woon Kim</strong>, M.D.
   </p>
   


**Abstract**

Objective
    The objective of this paper was to produce a comprehensive set of data that—by the use of network meta-analysis—forms both direct and indirect comparisons between the most commonly used grafts for primary anterior cruciate ligament reconstruction surgery in adult patients.

Design
    This paper is a follow-up and partially an update to a previously published systematic review and meta-analysis on the quadriceps tendon autograft. As a living systematic review, the intention is to also provide continuous updates to the publicly accessible datasets that were extracted and used for the analyses for future studies. In its present version, the paper includes five additional grafts as subgroups in a network meta-analysis.

Data sources
    Literature search was performed for each of the six graft types from three database sources: PubMed/MEDLINE, Embase, and Web of Science Core Collection. Citation/reference back-searching was performed on previously published systematic review and meta-analysis papers to catch any studies that may have been missed during the initial search.

Eligibility criteria
    Randomized controlled trials that compared the outcomes of at least two of the six grafts adult patients for primary anterior cruciate ligament reconstruction surgery were considered for inclusion. Furthermore, only those that reported on the most directly comparable outcomes were included in the analyses.

Systematic Review
#################

Protocol
********

**Research question**

The proposed review answers the question of whether graft choice plays a
factor in determining outcomes after primary anterior cruciate ligament
reconstruction surgery. And if so, which outcomes are affected by which
grafts, as well as the degree of effect specific graft have on each
outcome(s) that is/are found to have statistically significant
differences in effect sizes. Finally, it answers whether controlling for
gender, age and follow-up duration have any effect on the results of the
study

**Rationale**

The current state of knowledge in literature is that there are gold
standard surgical techniques for primary anterior cruciate ligament
reconstruction surgery in terms of specific grafts and
suspension/fixation techniques and tools; however, as advancements in
the latter over recent years has opened the door for all soft-tissue and
even allogenic grafts as just as viable—if not better—alternative graft
choices.

Specifically, the bone-patellar tendon-bone and hamstring tendon
autologous grafts have been tried-and-tested and consensus had deemed
these two grafts as the ‘gold standard’ choice for orthopedic surgeons.
However, the quadriceps tendon—particularly without the bony
attachment—was found to produce non-inferior results compared to those
with the patellar bone attachment. This finding opens the door for
comparing all soft-tissue grafts with other that share this similar
characteristic, such as the hamstring and peroneus longus tendon
autologous grafts. As there are numerous studies comparing the various
grafts, but not one comprehensive source from which to guide
evidence-based practice, this review paper seeks to add to fill this gap
in current knowledge by comparing the available randomized controlled
trials to produce an evidence level I network meta-analysis to guide
clinicians in their practice.

**Objectives**

This is an important question because total knee arthroplasty (TKA), or
total knee replacement is one of the most commonly performed surgical
operations in the world. However, studies have found a sole indication
for such a procedure, and that is osteoarthritic knee pain. Pain that is
chronic, and strong in intensity that it permanently degrades the
indicated patients’ quality of lives. TKA, however, also limits
patients’ locomotive capabilities, and is not a procedure that is
synonymous with restorative.

The most commonly cited research topic in orthopedic surgery by
orthopedics surgeons was anterior cruciate ligament reconstruction
(ACLR) surgery, with the link between this and TKA being that the former
(ACLR) is the most common cause of non-degenerative and thus, the most
common modifiable risk factor for preventing TKA and osteoarthritis. If
we are able to answer certain questions through research, then we can
advance our collective body of knowledge surrounding one of the most
debilitating musculoskeletal conditions and preventing those from
developing osteoarthritis after ACLR.

**Eligibility criteria**

+---+--------------+-------------------------------------------------------------+--------------------+----------------+
|   | Categories   | Description                                                 | Inclusion criteria | Exclusion      |
|   |              |                                                             |                    | criteria       |
+===+==============+=============================================================+====================+================+
| P | Population   | Adult patients with post-traumatic grade III (complete      | Adult patients     | Pediatric      |
|   |              | tear) of unilateral anterior cruciateligament are included. |                    | patients       |
|   |              | Both genders are included, and upper limit in age is        |                    |                |
|   |              | unrestricted. Only studies with mean age greater than or    |                    |                |
|   |              | equal to 18 years old across all patients will be presumed  |                    |                |
|   |              | to have targeted a population that is considered            |                    |                |
|   |              | skeletally-mature.                                          |                    |                |
+---+--------------+-------------------------------------------------------------+--------------------+----------------+
| I | Intervention | Primary anterior cruciate ligament reconstruction (ACLR)    | Primary ACLR       | Revision ACLR  |
|   |              | surgeries are included. ACLRs performed simultaneously on   |                    | or ACL repair  |
|   |              | both knees, in conjunction with other ligamental            |                    | (BEAR)         |
|   |              | reconstructions aside from meniscal, and revision ACLRs     |                    |                |
|   |              | were excluded.                                              |                    |                |
+---+--------------+-------------------------------------------------------------+--------------------+----------------+
| C | Comparators  | Autologous grafts: bone-patellar tendon-bone, hamstring     | Bone-patellar      | All other      |
|   |              | tendon, quadriceps tendon,and peroneus longus tendon are    | tendon-bone,       | graft types    |
|   |              | included. Allogenic grafts: Achilles tendon and tibialis    | hamstring tendon,  | (LET)          |
|   |              | anterior and posterior are also included. All other graft   | quadriceps, or     |                |
|   |              | types, such as synthetic grafts and allogenic versions of   | peroneus longus    |                |
|   |              | commonly used autologous ones are excluded (the Achillesand | tendon autologous  |                |
|   |              | tibialis tendon grafts are included despite being allogenic | grafts, or         |                |
|   |              | because autologous versions cannot be grafted in patients   | Achilles tendon or |                |
|   |              | due to the important roles the muscle from whichthe tendon  | tibialis           |                |
|   |              | is attached plays in normal physiologic biomechanics).      | anterior/posterior |                |
|   |              |                                                             | tendon allogenic   |                |
|   |              |                                                             | grafts.            |                |
+---+--------------+-------------------------------------------------------------+--------------------+----------------+
| O | Outcomes     | The outcomes of interest were measures of (1)               | Primary outcomes   | Secondary      |
|   |              | patient-reported outcome measures(PROMs) of patient         | of interest: IKDC  | outcomes of    |
|   |              | satisfaction as surrogate measure for subjective quality    | subjective,        | interest       |
|   |              | oflife—answering the question of how much is the patient    | Lysholm, Tegner,   |                |
|   |              | able to live as close to preinjury state; (2) Objective     | pivot shift,       |                |
|   |              | measures of translational and rotational knee stability;    | Lachman,           |                |
|   |              | and(3) Adverse events and complications. In (1), the        | instrumental       |                |
|   |              | primary (most commonly reported) outcomes were included:    | laxity, graft      |                |
|   |              | IKDC subjective knee form (SKF), Lysholm and Tegner.        | rupture, graft     |                |
|   |              | For(2), instrumental laxity (side-to-side difference in     | failure, revision  |                |
|   |              | millimeters) of antero-posterior translation by the         | rate               |                |
|   |              | anterior drawer test, pivot shift and Lachman tests were    |                    |                |
|   |              | included. For(3) graft failure, including re-re-rupture of  |                    |                |
|   |              | graft (confirmed via imaging), clinical failure(defined by  |                    |                |
|   |              | clinical failure during objective measures) and revision    |                    |                |
|   |              | surgeries(arthroscopic confirmation of tears).Other         |                    |                |
|   |              | outcomes that were excluded were due to their deemed        |                    |                |
|   |              | incompatibility forcomparisons across all grafts. For       |                    |                |
|   |              | example, hamstring and quadriceps muscle strength recovery  |                    |                |
|   |              | is not a relevant outcome measure for determining           |                    |                |
|   |              | effectiveness of ACLR when comparing across grafts in which |                    |                |
|   |              | some were not taken from the patients’ hamstring or         |                    |                |
|   |              | quadriceps muscle, or is a component that disrupts such     |                    |                |
|   |              | biomechanicalphysiology. Donor site morbidity is another    |                    |                |
|   |              | example of an outcome that may be out ofrange in scope, due |                    |                |
|   |              | to the variety of definitions for consistent applicability  |                    |                |
|   |              | incomparisons. Other outcomes such as Marx, KOOS, VAS, were |                    |                |
|   |              | excluded due to thelow number of studies that reported      |                    |                |
|   |              | these outcome measures, in comparison to theother ones that |                    |                |
|   |              | surrogatively measure the same thing.                       |                    |                |
+---+--------------+-------------------------------------------------------------+--------------------+----------------+
| S | Study Design | Only randomized controlled trials will be included into the | Randomized         | Non-randomized |
|   |              | qualitative and quantitative portions of the review.        | controlled trials  | clinical       |
|   |              |                                                             |                    | trials and     |
|   |              |                                                             |                    | observational  |
|   |              |                                                             |                    | studies        |
+---+--------------+-------------------------------------------------------------+--------------------+----------------+

Search Strategy
***************

Search strategies were developed for randomized controlled trials:
``pm_bptb.txt``, ``pm_ht.txt``, ``pm_qt.txt``, ``pm_plt.txt``,
``pm_at.txt`` and ``pm_ta.txt`` corresponding to PubMed search
strategies for patellar, hamstring, quadriceps, peroneus longus,
achilles and tibialis anterior and posterior tendones, respectively.
From the protocol that was developed, extract key terms from the
eligibility criteria for inclusion and exclusion of studies in order to
develop a *search strategy*.

The search strategies were ‘translated’ via regular expressions from
PubMed syntax to Embase and Web of Science syntax, store them into the
global environment, and save them as plain text files for importing and
use as queries for search.


**Table 2** Search strategies of each database search.

+---+--------------+------------------------+------------------------+------------------------+------------------------+------------------------+------------------------+
|   | Categories   | Patellar               | Hamstring              | Quadriceps             | Peroneus               | Achilles               | Tibialis               |
+===+==============+========================+========================+========================+========================+========================+========================+
| P | Population   | NOT                    | NOT                    | NOT                    | NOT                    | NOT                    | NOT                    |
|   |              | ((“pediatric”[tiab] OR | ((“pediatric”[tiab] OR | ((“pediatric”[tiab] OR | ((“pediatric”[tiab] OR | ((“pediatric”[tiab] OR | ((“pediatric”[tiab] OR |
|   |              | “paediatric”[tiab] OR  | “paediatric”[tiab] OR  | “paediatric”[tiab] OR  | “paediatric”[tiab] OR  | “paediatric”[tiab] OR  | “paediatric”[tiab] OR  |
|   |              | “adolescent”[tia) OR   | “adolescent”[tia) OR   | “adolescent”[tia) OR   | “adolescent”[tia) OR   | “adolescent”[tia) OR   | “adolescent”[tia) OR   |
|   |              | (“revision”[tiab] OR   | (“revision”[tiab] OR   | (“revision”[tiab] OR   | (“revision”[tiab] OR   | (“revision”[tiab] OR   | (“revision”[tiab] OR   |
|   |              | “repair”[tiab]))       | “repair”[tiab]))       | “repair”[tiab]))       | “repair”[tiab]))       | “repair”[tiab]))       | “repair”[tiab]))       |
+---+--------------+------------------------+------------------------+------------------------+------------------------+------------------------+------------------------+
| I | Intervention | (“anterior cruciate    | (“anterior cruciate    | (“anterior cruciate    | (“anterior cruciate    | (“anterior cruciate    | (“anterior cruciate    |
|   |              | ligament”[mh] OR       | ligament”[mh] OR       | ligament”[mh] OR       | ligament”[mh] OR       | ligament”[mh] OR       | ligament”[mh] OR       |
|   |              | “anterior cruciate     | “anterior cruciate     | “anterior cruciate     | “anterior cruciate     | “anterior cruciate     | “anterior cruciate     |
|   |              | ligament”[tiab] OR     | ligament”[tiab] OR     | ligament”[tiab] OR     | ligament”[tiab] OR     | ligament”[tiab] OR     | ligament”[tiab] OR     |
|   |              | “anterior cruciate     | “anterior cruciate     | “anterior cruciate     | “anterior cruciate     | “anterior cruciate     | “anterior cruciate     |
|   |              | ligament               | ligament               | ligament               | ligament               | ligament               | ligament               |
|   |              | reconstruction”[tiab]  | reconstruction”[tiab]  | reconstruction”[tiab]  | reconstruction”[tiab]  | reconstruction”[tiab]  | reconstruction”[tiab]  |
|   |              | OR “acl”[tiab])        | OR “acl”[tiab])        | OR “acl”[tiab])        | OR “acl”[tiab])        | OR “acl”[tiab])        | OR “acl”[tiab])        |
+---+--------------+------------------------+------------------------+------------------------+------------------------+------------------------+------------------------+
| C | Comparators  | (“bone-patellar        | (“hamstring”[tiab] OR  | (“quadriceps”[tiab] OR | (“peroneus”[tiab] OR   | (“achilles”[tiab] OR   | (“tibialis”[tiab] OR   |
|   |              | tendon-bone”[tiab] OR  | “hamstring             | “quadriceps            | “peroneus              | “achilles              | “tibialis              |
|   |              | “bone patellar tendon  | tendon”[tiab] OR       | tendon”[tiab] OR       | longus”[tiab] OR       | tendon”[tiab])         | anterior”[tiab] OR     |
|   |              | bone”[tiab] OR         | “semitendinosus”[tiab] | “qt”[tiab])            | “fibularis             |                        | “tibialis              |
|   |              | “patellar              | OR “gracilis”[tiab])   |                        | longus”[tiab])         |                        | posterior”[tiab])      |
|   |              | tendon”[tiab] OR       |                        |                        |                        |                        |                        |
|   |              | “bptb”[tiab])          |                        |                        |                        |                        |                        |
+---+--------------+------------------------+------------------------+------------------------+------------------------+------------------------+------------------------+
| O | Outcomes     | (“ikdc”[tiab] OR       | (“ikdc”[tiab] OR       | (“ikdc”[tiab] OR       | (“ikdc”[tiab] OR       | (“ikdc”[tiab] OR       | (“ikdc”[tiab] OR       |
|   |              | “lysholm”[tiab] OR     | “lysholm”[tiab] OR     | “lysholm”[tiab] OR     | “lysholm”[tiab] OR     | “lysholm”[tiab] OR     | “lysholm”[tiab] OR     |
|   |              | “tegner”[tiab] OR      | “tegner”[tiab] OR      | “tegner”[tiab] OR      | “tegner”[tiab] OR      | “tegner”[tiab] OR      | “tegner”[tiab] OR      |
|   |              | ((“instrumental        | ((“instrumental        | ((“instrumental        | ((“instrumental        | ((“instrumental        | ((“instrumental        |
|   |              | laxity”[tiab] OR       | laxity”[tiab] OR       | laxity”[tiab] OR       | laxity”[tiab] OR       | laxity”[tiab] OR       | laxity”[tiab] OR       |
|   |              | “kt-1000”[tiab] OR     | “kt-1000”[tiab] OR     | “kt-1000”[tiab] OR     | “kt-1000”[tiab] OR     | “kt-1000”[tiab] OR     | “kt-1000”[tiab] OR     |
|   |              | “kt-2000”[tiab] OR     | “kt-2000”[tiab] OR     | “kt-2000”[tiab] OR     | “kt-2000”[tiab] OR     | “kt-2000”[tiab] OR     | “kt-2000”[tiab] OR     |
|   |              | “rolimeter”[tiab]) OR  | “rolimeter”[tiab]) OR  | “rolimeter”[tiab]) OR  | “rolimeter”[tiab]) OR  | “rolimeter”[tiab]) OR  | “rolimeter”[tiab]) OR  |
|   |              | “pivot shift”[tiab] OR | “pivot shift”[tiab] OR | “pivot shift”[tiab] OR | “pivot shift”[tiab] OR | “pivot shift”[tiab] OR | “pivot shift”[tiab] OR |
|   |              | “lachman”[tiab]) OR    | “lachman”[tiab]) OR    | “lachman”[tiab]) OR    | “lachman”[tiab]) OR    | “lachman”[tiab]) OR    | “lachman”[tiab]) OR    |
|   |              | (“graft failure”[tiab] | (“graft failure”[tiab] | (“graft failure”[tiab] | (“graft failure”[tiab] | (“graft failure”[tiab] | (“graft failure”[tiab] |
|   |              | OR “graft              | OR “graft              | OR “graft              | OR “graft              | OR “graft              | OR “graft              |
|   |              | rupture”[tiab]))       | rupture”[tiab]))       | rupture”[tiab]))       | rupture”[tiab]))       | rupture”[tiab]))       | rupture”[tiab]))       |
+---+--------------+------------------------+------------------------+------------------------+------------------------+------------------------+------------------------+
| S | Study Design | (“randomized           | (“randomized           | (“randomized           | (“randomized           | (“randomized           | (“randomized           |
|   |              | controlled trial”[pt]  | controlled trial”[pt]  | controlled trial”[pt]  | controlled trial”[pt]  | controlled trial”[pt]  | controlled trial”[pt]  |
|   |              | OR “randomized         | OR “randomized         | OR “randomized         | OR “randomized         | OR “randomized         | OR “randomized         |
|   |              | controlled             | controlled             | controlled             | controlled             | controlled             | controlled             |
|   |              | trial”[tiab] OR        | trial”[tiab] OR        | trial”[tiab] OR        | trial”[tiab] OR        | trial”[tiab] OR        | trial”[tiab] OR        |
|   |              | “randomised controlled | “randomised controlled | “randomised controlled | “randomised controlled | “randomised controlled | “randomised controlled |
|   |              | trial”[tiab]) NOT      | trial”[tiab]) NOT      | trial”[tiab]) NOT      | trial”[tiab]) NOT      | trial”[tiab]) NOT      | trial”[tiab]) NOT      |
|   |              | (“review”[pt] OR       | (“review”[pt] OR       | (“review”[pt] OR       | (“review”[pt] OR       | (“review”[pt] OR       | (“review”[pt] OR       |
|   |              | “review”[tiab] OR      | “review”[tiab] OR      | “review”[tiab] OR      | “review”[tiab] OR      | “review”[tiab] OR      | “review”[tiab] OR      |
|   |              | “systematic            | “systematic            | “systematic            | “systematic            | “systematic            | “systematic            |
|   |              | review”[pt] OR         | review”[pt] OR         | review”[pt] OR         | review”[pt] OR         | review”[pt] OR         | review”[pt] OR         |
|   |              | “systematic            | “systematic            | “systematic            | “systematic            | “systematic            | “systematic            |
|   |              | review”[tiab] OR       | review”[tiab] OR       | review”[tiab] OR       | review”[tiab] OR       | review”[tiab] OR       | review”[tiab] OR       |
|   |              | “meta-analysis”[pt] OR | “meta-analysis”[pt] OR | “meta-analysis”[pt] OR | “meta-analysis”[pt] OR | “meta-analysis”[pt] OR | “meta-analysis”[pt] OR |
|   |              | “meta-analysis”[tiab]) | “meta-analysis”[tiab]) | “meta-analysis”[tiab]) | “meta-analysis”[tiab]) | “meta-analysis”[tiab]) | “meta-analysis”[tiab]) |
+---+--------------+------------------------+------------------------+------------------------+------------------------+------------------------+------------------------+


.. code:: ipython3

    IC = f"""({acl}) AND ({comparators})"""
    ICS = f"""({acl}) AND ({comparators}) AND ({study_design})"""
    print(ICS)


.. parsed-literal::

    (("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab])) AND (("bone-patellar tendon-bone"[tiab] OR "bone patellar tendon bone"[tiab] OR "patellar tendon"[tiab] OR "bptb"[tiab]) OR ("hamstring"[tiab] OR "hamstring tendon"[tiab] OR "semitendinosus"[tiab] OR "gracilis"[tiab]) OR ("quadriceps"[tiab] OR "quadriceps tendon"[tiab] OR "qt"[tiab]) OR ("peroneus"[tiab] OR "peroneus longus"[tiab] OR "fibularis longus"[tiab]) OR ("achilles"[tiab] OR "achilles tendon"[tiab]) OR ("tibialis"[tiab] OR "tibialis anterior"[tiab] OR "tibialis posterior"[tiab])) AND (("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab]) NOT ("review"[pt] OR "review"[tiab] OR "systematic review"[pt] OR "systematic review"[tiab] OR "meta-analysis"[pt] OR "meta-analysis"[tiab]))
    

.. code:: ipython3

    subgroups = {"bptb": bptb, 
                 "ht": ht, 
                 "qt": qt, 
                 "plt": plt, 
                 "at": at, 
                 "ta": ta}
    
    for x, y in subgroups.items():
        query = f"{acl} AND {y} AND {rct}"
        globals()[f"pm_{x}"] = query
        with open(f"./data/pm_{x}.txt", 'w') as f:
            f.write(query)
        print(query)
    
    pm_queries = {
        "bptb": pm_bptb,
        "ht": pm_ht,
        "qt": pm_qt,
        "plt": pm_plt,
        "at": pm_at,
        "ta": pm_ta
    }


.. parsed-literal::

    ("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab]) AND ("bone-patellar tendon-bone"[tiab] OR "bone patellar tendon bone"[tiab] OR "patellar tendon"[tiab] OR "bptb"[tiab]) AND ("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab])
    ("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab]) AND ("hamstring"[tiab] OR "hamstring tendon"[tiab] OR "semitendinosus"[tiab] OR "gracilis"[tiab]) AND ("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab])
    ("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab]) AND ("quadriceps"[tiab] OR "quadriceps tendon"[tiab] OR "qt"[tiab]) AND ("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab])
    ("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab]) AND ("peroneus"[tiab] OR "peroneus longus"[tiab] OR "fibularis longus"[tiab]) AND ("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab])
    ("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab]) AND ("achilles"[tiab] OR "achilles tendon"[tiab]) AND ("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab])
    ("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab]) AND ("tibialis"[tiab] OR "tibialis anterior"[tiab] OR "tibialis posterior"[tiab]) AND ("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab])
    

**Translate to Embase**

.. code:: ipython3

    for x, y in pm_queries.items():
        query = re.sub(r"\[(.*?)\]",":\\1", y)
        query = re.sub(r"\:tiab",":ti,ab", query)
        query = re.sub(r"\:mh","/exp", query)
        query = re.sub(r"\:pt",":it,ti,ab", query)
        query = re.sub(r'"',"'", query)
        globals()[f"em_{x}"] = query    
        with open(f"./data/em_{x}.txt", 'w') as f:
            f.write(query)
        print(query)


.. parsed-literal::

    ('anterior cruciate ligament'/exp OR 'anterior cruciate ligament':ti,ab OR 'anterior cruciate ligament reconstruction':ti,ab OR 'acl':ti,ab) AND ('bone-patellar tendon-bone':ti,ab OR 'bone patellar tendon bone':ti,ab OR 'patellar tendon':ti,ab OR 'bptb':ti,ab) AND ('randomized controlled trial':it,ti,ab OR 'randomized controlled trial':ti,ab OR 'randomised controlled trial':ti,ab)
    ('anterior cruciate ligament'/exp OR 'anterior cruciate ligament':ti,ab OR 'anterior cruciate ligament reconstruction':ti,ab OR 'acl':ti,ab) AND ('hamstring':ti,ab OR 'hamstring tendon':ti,ab OR 'semitendinosus':ti,ab OR 'gracilis':ti,ab) AND ('randomized controlled trial':it,ti,ab OR 'randomized controlled trial':ti,ab OR 'randomised controlled trial':ti,ab)
    ('anterior cruciate ligament'/exp OR 'anterior cruciate ligament':ti,ab OR 'anterior cruciate ligament reconstruction':ti,ab OR 'acl':ti,ab) AND ('quadriceps':ti,ab OR 'quadriceps tendon':ti,ab OR 'qt':ti,ab) AND ('randomized controlled trial':it,ti,ab OR 'randomized controlled trial':ti,ab OR 'randomised controlled trial':ti,ab)
    ('anterior cruciate ligament'/exp OR 'anterior cruciate ligament':ti,ab OR 'anterior cruciate ligament reconstruction':ti,ab OR 'acl':ti,ab) AND ('peroneus':ti,ab OR 'peroneus longus':ti,ab OR 'fibularis longus':ti,ab) AND ('randomized controlled trial':it,ti,ab OR 'randomized controlled trial':ti,ab OR 'randomised controlled trial':ti,ab)
    ('anterior cruciate ligament'/exp OR 'anterior cruciate ligament':ti,ab OR 'anterior cruciate ligament reconstruction':ti,ab OR 'acl':ti,ab) AND ('achilles':ti,ab OR 'achilles tendon':ti,ab) AND ('randomized controlled trial':it,ti,ab OR 'randomized controlled trial':ti,ab OR 'randomised controlled trial':ti,ab)
    ('anterior cruciate ligament'/exp OR 'anterior cruciate ligament':ti,ab OR 'anterior cruciate ligament reconstruction':ti,ab OR 'acl':ti,ab) AND ('tibialis':ti,ab OR 'tibialis anterior':ti,ab OR 'tibialis posterior':ti,ab) AND ('randomized controlled trial':it,ti,ab OR 'randomized controlled trial':ti,ab OR 'randomised controlled trial':ti,ab)
    

**Translate to Web of Science**

.. code:: ipython3

    for x, y in pm_queries.items():
        query = re.sub(r'"(.*?)"\[(.*?)\]','\\2="\\1"', y)
        query = re.sub(r'tiab="(.*?)"','(TI=(\\1) OR AB=(\\1))', query)
        query = re.sub(r'mh="(.*?)"','(TMIC=(\\1))', query)
        query = re.sub(r'pt="(.*?)"','(TS=(\\1))', query)
        globals()[f"wos_{x}"] = query
        with open(f"./data/wos_{x}.txt", 'w') as f:
            f.write(query)
        print(query)


.. parsed-literal::

    ((TMIC=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament) OR AB=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament reconstruction) OR AB=(anterior cruciate ligament reconstruction)) OR (TI=(acl) OR AB=(acl))) AND ((TI=(bone-patellar tendon-bone) OR AB=(bone-patellar tendon-bone)) OR (TI=(bone patellar tendon bone) OR AB=(bone patellar tendon bone)) OR (TI=(patellar tendon) OR AB=(patellar tendon)) OR (TI=(bptb) OR AB=(bptb))) AND ((TS=(randomized controlled trial)) OR (TI=(randomized controlled trial) OR AB=(randomized controlled trial)) OR (TI=(randomised controlled trial) OR AB=(randomised controlled trial)))
    ((TMIC=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament) OR AB=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament reconstruction) OR AB=(anterior cruciate ligament reconstruction)) OR (TI=(acl) OR AB=(acl))) AND ((TI=(hamstring) OR AB=(hamstring)) OR (TI=(hamstring tendon) OR AB=(hamstring tendon)) OR (TI=(semitendinosus) OR AB=(semitendinosus)) OR (TI=(gracilis) OR AB=(gracilis))) AND ((TS=(randomized controlled trial)) OR (TI=(randomized controlled trial) OR AB=(randomized controlled trial)) OR (TI=(randomised controlled trial) OR AB=(randomised controlled trial)))
    ((TMIC=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament) OR AB=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament reconstruction) OR AB=(anterior cruciate ligament reconstruction)) OR (TI=(acl) OR AB=(acl))) AND ((TI=(quadriceps) OR AB=(quadriceps)) OR (TI=(quadriceps tendon) OR AB=(quadriceps tendon)) OR (TI=(qt) OR AB=(qt))) AND ((TS=(randomized controlled trial)) OR (TI=(randomized controlled trial) OR AB=(randomized controlled trial)) OR (TI=(randomised controlled trial) OR AB=(randomised controlled trial)))
    ((TMIC=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament) OR AB=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament reconstruction) OR AB=(anterior cruciate ligament reconstruction)) OR (TI=(acl) OR AB=(acl))) AND ((TI=(peroneus) OR AB=(peroneus)) OR (TI=(peroneus longus) OR AB=(peroneus longus)) OR (TI=(fibularis longus) OR AB=(fibularis longus))) AND ((TS=(randomized controlled trial)) OR (TI=(randomized controlled trial) OR AB=(randomized controlled trial)) OR (TI=(randomised controlled trial) OR AB=(randomised controlled trial)))
    ((TMIC=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament) OR AB=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament reconstruction) OR AB=(anterior cruciate ligament reconstruction)) OR (TI=(acl) OR AB=(acl))) AND ((TI=(achilles) OR AB=(achilles)) OR (TI=(achilles tendon) OR AB=(achilles tendon))) AND ((TS=(randomized controlled trial)) OR (TI=(randomized controlled trial) OR AB=(randomized controlled trial)) OR (TI=(randomised controlled trial) OR AB=(randomised controlled trial)))
    ((TMIC=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament) OR AB=(anterior cruciate ligament)) OR (TI=(anterior cruciate ligament reconstruction) OR AB=(anterior cruciate ligament reconstruction)) OR (TI=(acl) OR AB=(acl))) AND ((TI=(tibialis) OR AB=(tibialis)) OR (TI=(tibialis anterior) OR AB=(tibialis anterior)) OR (TI=(tibialis posterior) OR AB=(tibialis posterior))) AND ((TS=(randomized controlled trial)) OR (TI=(randomized controlled trial) OR AB=(randomized controlled trial)) OR (TI=(randomised controlled trial) OR AB=(randomised controlled trial)))
    

**Translate to Cochrane Library**

.. code:: ipython3

    for x, y in pm_queries.items():
        query = re.sub(r"\[(.*?)\]",":\\1", y)
        query = re.sub(r"\:tiab",":ti,ab", query)
        query = re.sub(r"\((.*?)\:mh",r"([mh \1]", query)
        globals()[f"co_{x}"] = query
        with open(f"./data/co_{x}.txt", 'w') as f:
            f.write(query)
        print(query)


.. parsed-literal::

    ([mh "anterior cruciate ligament"] OR "anterior cruciate ligament":ti,ab OR "anterior cruciate ligament reconstruction":ti,ab OR "acl":ti,ab) AND ("bone-patellar tendon-bone":ti,ab OR "bone patellar tendon bone":ti,ab OR "patellar tendon":ti,ab OR "bptb":ti,ab) AND ("randomized controlled trial":pt OR "randomized controlled trial":ti,ab OR "randomised controlled trial":ti,ab)
    ([mh "anterior cruciate ligament"] OR "anterior cruciate ligament":ti,ab OR "anterior cruciate ligament reconstruction":ti,ab OR "acl":ti,ab) AND ("hamstring":ti,ab OR "hamstring tendon":ti,ab OR "semitendinosus":ti,ab OR "gracilis":ti,ab) AND ("randomized controlled trial":pt OR "randomized controlled trial":ti,ab OR "randomised controlled trial":ti,ab)
    ([mh "anterior cruciate ligament"] OR "anterior cruciate ligament":ti,ab OR "anterior cruciate ligament reconstruction":ti,ab OR "acl":ti,ab) AND ("quadriceps":ti,ab OR "quadriceps tendon":ti,ab OR "qt":ti,ab) AND ("randomized controlled trial":pt OR "randomized controlled trial":ti,ab OR "randomised controlled trial":ti,ab)
    ([mh "anterior cruciate ligament"] OR "anterior cruciate ligament":ti,ab OR "anterior cruciate ligament reconstruction":ti,ab OR "acl":ti,ab) AND ("peroneus":ti,ab OR "peroneus longus":ti,ab OR "fibularis longus":ti,ab) AND ("randomized controlled trial":pt OR "randomized controlled trial":ti,ab OR "randomised controlled trial":ti,ab)
    ([mh "anterior cruciate ligament"] OR "anterior cruciate ligament":ti,ab OR "anterior cruciate ligament reconstruction":ti,ab OR "acl":ti,ab) AND ("achilles":ti,ab OR "achilles tendon":ti,ab) AND ("randomized controlled trial":pt OR "randomized controlled trial":ti,ab OR "randomised controlled trial":ti,ab)
    ([mh "anterior cruciate ligament"] OR "anterior cruciate ligament":ti,ab OR "anterior cruciate ligament reconstruction":ti,ab OR "acl":ti,ab) AND ("tibialis":ti,ab OR "tibialis anterior":ti,ab OR "tibialis posterior":ti,ab) AND ("randomized controlled trial":pt OR "randomized controlled trial":ti,ab OR "randomised controlled trial":ti,ab)
    

.. code:: ipython3

    queries = [
        pm_bptb, pm_ht, pm_qt, pm_plt, pm_ta, pm_at,
        em_bptb, em_ht, em_qt, em_plt, em_ta, em_at,
        wos_bptb, wos_ht, wos_qt, wos_plt, wos_ta, wos_at,
        co_bptb, co_ht, co_qt, co_plt, co_ta, co_at,
    ]

.. code:: ipython3

    pubmed = [f"{pm_bptb}", f"{pm_ht}", f"{pm_qt}", f"{pm_plt}", f"{pm_at}", f"{pm_ta}"]
    embase = [f"{em_bptb}", f"{em_ht}", f"{em_qt}", f"{em_plt}",f"{em_at}", f"{em_ta}"]
    wos = [f"{wos_bptb}", f"{wos_ht}", f"{wos_qt}", f"{wos_plt}", f"{wos_at}", f"{wos_ta}"]
    cochrane = [f"{co_bptb}", f"{co_ht}", f"{co_qt}", f"{co_plt}", f"{co_at}", f"{co_ta}"]
    
    df = pd.DataFrame({
        " ": ["BPTB", "HT", "QT", "PLT", "AT", "TA"],
        "Subgroup": ["Patellar", "Hamstring", "Quadriceps", "Peroneus", "Achilles", "Tibialis"],
        "PubMed": pubmed,
        "Embase": embase,
        "Web of Science": wos,
        "Cochrane Library": cochrane,
    })
    
    df.to_csv("./data/search_strategies_2.csv", encoding = "utf-8", index = False)
    from IPython.display import Markdown, display
    markdown_table = df.to_markdown(index = False)
    display(Markdown(markdown_table))



+------+------------+------------------------+------------------------+------------------------+------------------------+
|      | Subgroup   | PubMed                 | Embase                 | Web of Science         | Cochrane Library       |
+======+============+========================+========================+========================+========================+
| BPTB | Patellar   | (“anterior cruciate    | (‘anterior cruciate    | ((TMIC=(anterior       | ([mh “anterior         |
|      |            | ligament”[mh] OR       | ligament’/exp OR       | cruciate ligament)) OR | cruciate ligament”] OR |
|      |            | “anterior cruciate     | ‘anterior cruciate     | (TI=(anterior cruciate | “anterior cruciate     |
|      |            | ligament”[tiab] OR     | ligament’:ti,ab OR     | ligament) OR           | ligament”:ti,ab OR     |
|      |            | “anterior cruciate     | ‘anterior cruciate     | AB=(anterior cruciate  | “anterior cruciate     |
|      |            | ligament               | ligament               | ligament)) OR          | ligament               |
|      |            | reconstruction”[tiab]  | reconstruction’:ti,ab  | (TI=(anterior cruciate | reconstruction”:ti,ab  |
|      |            | OR “acl”[tiab]) AND    | OR ‘acl’:ti,ab) AND    | ligament               | OR “acl”:ti,ab) AND    |
|      |            | (“bone-patellar        | (‘bone-patellar        | reconstruction) OR     | (“bone-patellar        |
|      |            | tendon-bone”[tiab] OR  | tendon-bone’:ti,ab OR  | AB=(anterior cruciate  | tendon-bone”:ti,ab OR  |
|      |            | “bone patellar tendon  | ‘bone patellar tendon  | ligament               | “bone patellar tendon  |
|      |            | bone”[tiab] OR         | bone’:ti,ab OR         | reconstruction)) OR    | bone”:ti,ab OR         |
|      |            | “patellar              | ‘patellar              | (TI=(acl) OR           | “patellar              |
|      |            | tendon”[tiab] OR       | tendon’:ti,ab OR       | AB=(acl))) AND         | tendon”:ti,ab OR       |
|      |            | “bptb”[tiab]) AND      | ‘bptb’:ti,ab) AND      | ((TI=(bone-patellar    | “bptb”:ti,ab) AND      |
|      |            | (“randomized           | (‘randomized           | tendon-bone) OR        | (“randomized           |
|      |            | controlled trial”[pt]  | controlled             | AB=(bone-patellar      | controlled trial”:pt   |
|      |            | OR “randomized         | trial’:it,ti,ab OR     | tendon-bone)) OR       | OR “randomized         |
|      |            | controlled             | ‘randomized controlled | (TI=(bone patellar     | controlled             |
|      |            | trial”[tiab] OR        | trial’:ti,ab OR        | tendon bone) OR        | trial”:ti,ab OR        |
|      |            | “randomised controlled | ‘randomised controlled | AB=(bone patellar      | “randomised controlled |
|      |            | trial”[tiab])          | trial’:ti,ab)          | tendon bone)) OR       | trial”:ti,ab)          |
|      |            |                        |                        | (TI=(patellar tendon)  |                        |
|      |            |                        |                        | OR AB=(patellar        |                        |
|      |            |                        |                        | tendon)) OR (TI=(bptb) |                        |
|      |            |                        |                        | OR AB=(bptb))) AND     |                        |
|      |            |                        |                        | ((TS=(randomized       |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomized        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomized         |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomised        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomised         |                        |
|      |            |                        |                        | controlled trial)))    |                        |
+------+------------+------------------------+------------------------+------------------------+------------------------+
| HT   | Hamstring  | (“anterior cruciate    | (‘anterior cruciate    | ((TMIC=(anterior       | ([mh “anterior         |
|      |            | ligament”[mh] OR       | ligament’/exp OR       | cruciate ligament)) OR | cruciate ligament”] OR |
|      |            | “anterior cruciate     | ‘anterior cruciate     | (TI=(anterior cruciate | “anterior cruciate     |
|      |            | ligament”[tiab] OR     | ligament’:ti,ab OR     | ligament) OR           | ligament”:ti,ab OR     |
|      |            | “anterior cruciate     | ‘anterior cruciate     | AB=(anterior cruciate  | “anterior cruciate     |
|      |            | ligament               | ligament               | ligament)) OR          | ligament               |
|      |            | reconstruction”[tiab]  | reconstruction’:ti,ab  | (TI=(anterior cruciate | reconstruction”:ti,ab  |
|      |            | OR “acl”[tiab]) AND    | OR ‘acl’:ti,ab) AND    | ligament               | OR “acl”:ti,ab) AND    |
|      |            | (“hamstring”[tiab] OR  | (‘hamstring’:ti,ab OR  | reconstruction) OR     | (“hamstring”:ti,ab OR  |
|      |            | “hamstring             | ‘hamstring             | AB=(anterior cruciate  | “hamstring             |
|      |            | tendon”[tiab] OR       | tendon’:ti,ab OR       | ligament               | tendon”:ti,ab OR       |
|      |            | “semitendinosus”[tiab] | ‘semitendinosus’:ti,ab | reconstruction)) OR    | “semitendinosus”:ti,ab |
|      |            | OR “gracilis”[tiab])   | OR ‘gracilis’:ti,ab)   | (TI=(acl) OR           | OR “gracilis”:ti,ab)   |
|      |            | AND (“randomized       | AND (‘randomized       | AB=(acl))) AND         | AND (“randomized       |
|      |            | controlled trial”[pt]  | controlled             | ((TI=(hamstring) OR    | controlled trial”:pt   |
|      |            | OR “randomized         | trial’:it,ti,ab OR     | AB=(hamstring)) OR     | OR “randomized         |
|      |            | controlled             | ‘randomized controlled | (TI=(hamstring tendon) | controlled             |
|      |            | trial”[tiab] OR        | trial’:ti,ab OR        | OR AB=(hamstring       | trial”:ti,ab OR        |
|      |            | “randomised controlled | ‘randomised controlled | tendon)) OR            | “randomised controlled |
|      |            | trial”[tiab])          | trial’:ti,ab)          | (TI=(semitendinosus)   | trial”:ti,ab)          |
|      |            |                        |                        | OR                     |                        |
|      |            |                        |                        | AB=(semitendinosus))   |                        |
|      |            |                        |                        | OR (TI=(gracilis) OR   |                        |
|      |            |                        |                        | AB=(gracilis))) AND    |                        |
|      |            |                        |                        | ((TS=(randomized       |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomized        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomized         |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomised        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomised         |                        |
|      |            |                        |                        | controlled trial)))    |                        |
+------+------------+------------------------+------------------------+------------------------+------------------------+
| QT   | Quadriceps | (“anterior cruciate    | (‘anterior cruciate    | ((TMIC=(anterior       | ([mh “anterior         |
|      |            | ligament”[mh] OR       | ligament’/exp OR       | cruciate ligament)) OR | cruciate ligament”] OR |
|      |            | “anterior cruciate     | ‘anterior cruciate     | (TI=(anterior cruciate | “anterior cruciate     |
|      |            | ligament”[tiab] OR     | ligament’:ti,ab OR     | ligament) OR           | ligament”:ti,ab OR     |
|      |            | “anterior cruciate     | ‘anterior cruciate     | AB=(anterior cruciate  | “anterior cruciate     |
|      |            | ligament               | ligament               | ligament)) OR          | ligament               |
|      |            | reconstruction”[tiab]  | reconstruction’:ti,ab  | (TI=(anterior cruciate | reconstruction”:ti,ab  |
|      |            | OR “acl”[tiab]) AND    | OR ‘acl’:ti,ab) AND    | ligament               | OR “acl”:ti,ab) AND    |
|      |            | (“quadriceps”[tiab] OR | (‘quadriceps’:ti,ab OR | reconstruction) OR     | (“quadriceps”:ti,ab OR |
|      |            | “quadriceps            | ‘quadriceps            | AB=(anterior cruciate  | “quadriceps            |
|      |            | tendon”[tiab] OR       | tendon’:ti,ab OR       | ligament               | tendon”:ti,ab OR       |
|      |            | “qt”[tiab]) AND        | ‘qt’:ti,ab) AND        | reconstruction)) OR    | “qt”:ti,ab) AND        |
|      |            | (“randomized           | (‘randomized           | (TI=(acl) OR           | (“randomized           |
|      |            | controlled trial”[pt]  | controlled             | AB=(acl))) AND         | controlled trial”:pt   |
|      |            | OR “randomized         | trial’:it,ti,ab OR     | ((TI=(quadriceps) OR   | OR “randomized         |
|      |            | controlled             | ‘randomized controlled | AB=(quadriceps)) OR    | controlled             |
|      |            | trial”[tiab] OR        | trial’:ti,ab OR        | (TI=(quadriceps        | trial”:ti,ab OR        |
|      |            | “randomised controlled | ‘randomised controlled | tendon) OR             | “randomised controlled |
|      |            | trial”[tiab])          | trial’:ti,ab)          | AB=(quadriceps         | trial”:ti,ab)          |
|      |            |                        |                        | tendon)) OR (TI=(qt)   |                        |
|      |            |                        |                        | OR AB=(qt))) AND       |                        |
|      |            |                        |                        | ((TS=(randomized       |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomized        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomized         |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomised        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomised         |                        |
|      |            |                        |                        | controlled trial)))    |                        |
+------+------------+------------------------+------------------------+------------------------+------------------------+
| PLT  | Peroneus   | (“anterior cruciate    | (‘anterior cruciate    | ((TMIC=(anterior       | ([mh “anterior         |
|      |            | ligament”[mh] OR       | ligament’/exp OR       | cruciate ligament)) OR | cruciate ligament”] OR |
|      |            | “anterior cruciate     | ‘anterior cruciate     | (TI=(anterior cruciate | “anterior cruciate     |
|      |            | ligament”[tiab] OR     | ligament’:ti,ab OR     | ligament) OR           | ligament”:ti,ab OR     |
|      |            | “anterior cruciate     | ‘anterior cruciate     | AB=(anterior cruciate  | “anterior cruciate     |
|      |            | ligament               | ligament               | ligament)) OR          | ligament               |
|      |            | reconstruction”[tiab]  | reconstruction’:ti,ab  | (TI=(anterior cruciate | reconstruction”:ti,ab  |
|      |            | OR “acl”[tiab]) AND    | OR ‘acl’:ti,ab) AND    | ligament               | OR “acl”:ti,ab) AND    |
|      |            | (“peroneus”[tiab] OR   | (‘peroneus’:ti,ab OR   | reconstruction) OR     | (“peroneus”:ti,ab OR   |
|      |            | “peroneus              | ‘peroneus              | AB=(anterior cruciate  | “peroneus              |
|      |            | longus”[tiab] OR       | longus’:ti,ab OR       | ligament               | longus”:ti,ab OR       |
|      |            | “fibularis             | ‘fibularis             | reconstruction)) OR    | “fibularis             |
|      |            | longus”[tiab]) AND     | longus’:ti,ab) AND     | (TI=(acl) OR           | longus”:ti,ab) AND     |
|      |            | (“randomized           | (‘randomized           | AB=(acl))) AND         | (“randomized           |
|      |            | controlled trial”[pt]  | controlled             | ((TI=(peroneus) OR     | controlled trial”:pt   |
|      |            | OR “randomized         | trial’:it,ti,ab OR     | AB=(peroneus)) OR      | OR “randomized         |
|      |            | controlled             | ‘randomized controlled | (TI=(peroneus longus)  | controlled             |
|      |            | trial”[tiab] OR        | trial’:ti,ab OR        | OR AB=(peroneus        | trial”:ti,ab OR        |
|      |            | “randomised controlled | ‘randomised controlled | longus)) OR            | “randomised controlled |
|      |            | trial”[tiab])          | trial’:ti,ab)          | (TI=(fibularis longus) | trial”:ti,ab)          |
|      |            |                        |                        | OR AB=(fibularis       |                        |
|      |            |                        |                        | longus))) AND          |                        |
|      |            |                        |                        | ((TS=(randomized       |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomized        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomized         |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomised        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomised         |                        |
|      |            |                        |                        | controlled trial)))    |                        |
+------+------------+------------------------+------------------------+------------------------+------------------------+
| AT   | Achilles   | (“anterior cruciate    | (‘anterior cruciate    | ((TMIC=(anterior       | ([mh “anterior         |
|      |            | ligament”[mh] OR       | ligament’/exp OR       | cruciate ligament)) OR | cruciate ligament”] OR |
|      |            | “anterior cruciate     | ‘anterior cruciate     | (TI=(anterior cruciate | “anterior cruciate     |
|      |            | ligament”[tiab] OR     | ligament’:ti,ab OR     | ligament) OR           | ligament”:ti,ab OR     |
|      |            | “anterior cruciate     | ‘anterior cruciate     | AB=(anterior cruciate  | “anterior cruciate     |
|      |            | ligament               | ligament               | ligament)) OR          | ligament               |
|      |            | reconstruction”[tiab]  | reconstruction’:ti,ab  | (TI=(anterior cruciate | reconstruction”:ti,ab  |
|      |            | OR “acl”[tiab]) AND    | OR ‘acl’:ti,ab) AND    | ligament               | OR “acl”:ti,ab) AND    |
|      |            | (“achilles”[tiab] OR   | (‘achilles’:ti,ab OR   | reconstruction) OR     | (“achilles”:ti,ab OR   |
|      |            | “achilles              | ‘achilles              | AB=(anterior cruciate  | “achilles              |
|      |            | tendon”[tiab]) AND     | tendon’:ti,ab) AND     | ligament               | tendon”:ti,ab) AND     |
|      |            | (“randomized           | (‘randomized           | reconstruction)) OR    | (“randomized           |
|      |            | controlled trial”[pt]  | controlled             | (TI=(acl) OR           | controlled trial”:pt   |
|      |            | OR “randomized         | trial’:it,ti,ab OR     | AB=(acl))) AND         | OR “randomized         |
|      |            | controlled             | ‘randomized controlled | ((TI=(achilles) OR     | controlled             |
|      |            | trial”[tiab] OR        | trial’:ti,ab OR        | AB=(achilles)) OR      | trial”:ti,ab OR        |
|      |            | “randomised controlled | ‘randomised controlled | (TI=(achilles tendon)  | “randomised controlled |
|      |            | trial”[tiab])          | trial’:ti,ab)          | OR AB=(achilles        | trial”:ti,ab)          |
|      |            |                        |                        | tendon))) AND          |                        |
|      |            |                        |                        | ((TS=(randomized       |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomized        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomized         |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomised        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomised         |                        |
|      |            |                        |                        | controlled trial)))    |                        |
+------+------------+------------------------+------------------------+------------------------+------------------------+
| TA   | Tibialis   | (“anterior cruciate    | (‘anterior cruciate    | ((TMIC=(anterior       | ([mh “anterior         |
|      |            | ligament”[mh] OR       | ligament’/exp OR       | cruciate ligament)) OR | cruciate ligament”] OR |
|      |            | “anterior cruciate     | ‘anterior cruciate     | (TI=(anterior cruciate | “anterior cruciate     |
|      |            | ligament”[tiab] OR     | ligament’:ti,ab OR     | ligament) OR           | ligament”:ti,ab OR     |
|      |            | “anterior cruciate     | ‘anterior cruciate     | AB=(anterior cruciate  | “anterior cruciate     |
|      |            | ligament               | ligament               | ligament)) OR          | ligament               |
|      |            | reconstruction”[tiab]  | reconstruction’:ti,ab  | (TI=(anterior cruciate | reconstruction”:ti,ab  |
|      |            | OR “acl”[tiab]) AND    | OR ‘acl’:ti,ab) AND    | ligament               | OR “acl”:ti,ab) AND    |
|      |            | (“tibialis”[tiab] OR   | (‘tibialis’:ti,ab OR   | reconstruction) OR     | (“tibialis”:ti,ab OR   |
|      |            | “tibialis              | ‘tibialis              | AB=(anterior cruciate  | “tibialis              |
|      |            | anterior”[tiab] OR     | anterior’:ti,ab OR     | ligament               | anterior”:ti,ab OR     |
|      |            | “tibialis              | ‘tibialis              | reconstruction)) OR    | “tibialis              |
|      |            | posterior”[tiab]) AND  | posterior’:ti,ab) AND  | (TI=(acl) OR           | posterior”:ti,ab) AND  |
|      |            | (“randomized           | (‘randomized           | AB=(acl))) AND         | (“randomized           |
|      |            | controlled trial”[pt]  | controlled             | ((TI=(tibialis) OR     | controlled trial”:pt   |
|      |            | OR “randomized         | trial’:it,ti,ab OR     | AB=(tibialis)) OR      | OR “randomized         |
|      |            | controlled             | ‘randomized controlled | (TI=(tibialis          | controlled             |
|      |            | trial”[tiab] OR        | trial’:ti,ab OR        | anterior) OR           | trial”:ti,ab OR        |
|      |            | “randomised controlled | ‘randomised controlled | AB=(tibialis           | “randomised controlled |
|      |            | trial”[tiab])          | trial’:ti,ab)          | anterior)) OR          | trial”:ti,ab)          |
|      |            |                        |                        | (TI=(tibialis          |                        |
|      |            |                        |                        | posterior) OR          |                        |
|      |            |                        |                        | AB=(tibialis           |                        |
|      |            |                        |                        | posterior))) AND       |                        |
|      |            |                        |                        | ((TS=(randomized       |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomized        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomized         |                        |
|      |            |                        |                        | controlled trial)) OR  |                        |
|      |            |                        |                        | (TI=(randomised        |                        |
|      |            |                        |                        | controlled trial) OR   |                        |
|      |            |                        |                        | AB=(randomised         |                        |
|      |            |                        |                        | controlled trial)))    |                        |
+------+------------+------------------------+------------------------+------------------------+------------------------+

Search
******
A script to either create a search strategy using the terms, field tags,
and Boolean operators and save them as plain text files or load already
written and saved plain text files for import into the API search
scripts. This uses the search strategies (e.g., ``pm_bptb.txt``, search
strategy in plain text written in PubMed syntax for bone-patellar
tendon-bone (BPTB) subgroup search) and pulls data from PubMed to output
PMIDs (``pmid_pm_bptb.txt``) and search results in XML (``pm_bptb.xml``)
and parses this into CSV files (``pm_bptb.csv``).

.. code:: ipython3

    from src import search

.. code:: mermaid
   ---
   config:
     theme: light
     curve: stepBefore
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

   A4["co_bptb"]
   B4["co_ht"]
   C4["co_qt"]
   D4["co_plt"]
   E4["co_at"]
   F4["co_ta"]

   G["pubmed"]
   H["embase"]
   I["wos"]
   J["cochrane"]

   A1 & B1 & C1 & D1 & E1 & F1 --> G
   A2 & B2 & C2 & D2 & E2 & F2 --> H
   A3 & B3 & C3 & D3 & E3 & F3 --> I
   A4 & B4 & C4 & D4 & E4 & F4 --> J

   G & H & I & J --> K["records"]

   click A1 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//pm_bptb.csv"
   click B1 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//pm_ht.csv"
   click C1 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//pm_qt.csv"
   click D1 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//pm_plt.csv"
   click E1 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//pm_at.csv"
   click F1 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//pm_ta.csv"
   click A2 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//em_bptb.csv"
   click B2 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//em_ht.csv"
   click C2 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//em_qt.csv"
   click D2 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//em_plt.csv"
   click E2 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//em_at.csv"
   click F2 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//em_ta.csv"
   click A3 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//wos_bptb.csv"
   click B3 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//wos_ht.csv"
   click C3 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//wos_qt.csv"
   click D3 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//wos_plt.csv"
   click E3 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//wos_at.csv"
   click F3 "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data//wos_ta.csv"

**PubMed/MEDLINE**

.. code:: ipython3

    pubmed = {
        "pm_bptb": pm_bptb,
        "pm_ht": pm_ht,
        "pm_qt": pm_qt,
        "pm_plt": pm_plt,
        "pm_at": pm_at,
        "pm_ta": pm_ta
    }
    
    for x, y in pubmed.items():
        df = search(y)
        globals()[f"{x}"] = df

.. code:: ipython3

    dfs = [
        "pm_bptb",
        "pm_ht",
        "pm_qt",
        "pm_plt",
        "pm_at",
        "pm_ta",
        "em_bptb",
        "em_ht",
        "em_qt",
        "em_plt",
        "em_at",
        "em_ta",
        "wos_bptb",
        "wos_ht",
        "wos_qt",
        "wos_plt",
        "wos_at",
        "wos_ta",
        "co_bptb",
        "co_ht",
        "co_qt",
        "co_plt",
        "co_ta",
    ]
    
    url = "https://raw.githubusercontent.com/d-wkim/d-wkim/refs/heads/main/data/"
    
    for filename in dfs:
        df = pd.read_csv(f"{url}/{filename}.csv", encoding = "utf-8")
        globals()[f"{filename}"] = df

**Define the names and data frames of the raw datasets**

.. code:: ipython3

    pubmed = {
        "pm_bptb": pm_bptb,
        "pm_ht": pm_ht,
        "pm_qt": pm_qt,
        "pm_plt": pm_plt,
        "pm_at": pm_at,
        "pm_ta": pm_ta
    }
    
    embase = {
        "em_bptb": em_bptb,
        "em_ht": em_ht,
        "em_qt": em_qt,
        "em_plt": em_plt,
        "em_at": em_at,
        "em_ta": em_ta
    }
    
    web_of_science = {
        "wos_bptb": wos_bptb,
        "wos_ht": wos_ht,
        "wos_qt": wos_qt,
        "wos_plt": wos_plt,
        "wos_at": wos_at,
        "wos_ta": wos_ta
    }
    
    cochrane = {
        "co_bptb": co_bptb,
        "co_ht": co_ht,
        "co_qt": co_qt,
        "co_plt": co_plt,
        "co_ta": co_ta
    }

**PubMed/MEDLINE**: Rename columns, clean and create new data frames
from the raw datasets.

.. code:: ipython3

    for name, df in pubmed.items():
        df.rename(columns = {
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
        
        df["id"] = range(1, len(df)+1)
        
        df = pd.DataFrame({
            "id": df["id"],
            "pmid": df["pmid"],
            "source": "pubmed",
            "doi": df["doi"],
            "authors": df["authors"],
            "journal": df["journal"],
            "title": df["title"],
            "abstract": df["abstract"],
            "year": df["year"],
            "language": df["language"]
        })
        
        globals()[name] = df
        df.to_csv(f"./data/{name}.csv", encoding = "utf-8")
    pubmed = pd.concat([pm_bptb, pm_ht, pm_qt, pm_plt, pm_at, pm_ta])
    pubmed.to_csv(f"./data/pubmed.csv", encoding = "utf-8")

**Embase**: Rename columns, clean and create new data frames from the
raw datasets.

.. code:: ipython3

    for name, df in embase.items():
        df.rename(columns = {
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
        
        df["id"] = range(1, len(df)+1)
    
        df = pd.DataFrame({
            "id": df["id"],
            "pmid": df["pmid"],
            "doi": df["doi"],
            "source": "embase",
            "authors": df["authors"],
            "journal": df["journal"],
            "title": df["title"],
            "abstract": df["abstract"],
            "year": df["year"],
            "language": df["language"]
        })
    
        df['pmid'] = df['pmid'].astype(str)
        df["authors"] = df["authors"].str.replace(r"[\'\[\]]","", regex = True)
        df["language"] = df["language"].str.replace(r"[\'\[\]]","",regex = True)
    
        globals()[name] = df
        
        df.to_csv(f"./data/{name}.csv", encoding = "utf-8")
    embase = pd.concat([em_bptb, em_ht, em_qt, em_plt, em_at, em_ta])
    embase.to_csv(f"./data/embase.csv", encoding = "utf-8")

**Web of Science**: Rename columns, clean and create new data frames
from the raw datasets.

.. code:: ipython3

    for name, df in web_of_science.items():
        df.rename(columns = {
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
    
        df["id"] = range(1, len(df)+1)
    
        df = pd.DataFrame({
            "id": df["id"],
            "pmid": df["pmid"],
            "source": "web_of_science",
            "doi": df["doi"],
            "authors": df["authors"],
            "journal": df["journal"],
            "title": df["title"],
            "abstract": df["abstract"],
            "year": df["year"],
            "language": df["language"]
        })
    
        df['pmid'] = df['pmid'].astype(str)
        df["authors"] = df["authors"].str.replace(r"[\'\[\]]","", regex = True)
        df["language"] = df["language"].str.replace(r"[\'\[\]]","",regex = True)
        globals()[name] = df
        
        df.to_csv(f"./data/{name}.csv", encoding = "latin-1")
    wos = pd.concat([wos_bptb, wos_ht, wos_qt, wos_plt, wos_at, wos_ta])
    wos.to_csv(f"./data/wos.csv", encoding = "latin-1")

**Cochrane Library**

.. code:: ipython3

    for name, df in cochrane.items():
        df.rename(columns = {
            "CENTRAL ID": "CENTRAL_ID",
            "Author(s)": "authors",
            "Title": "title",
            "Source": "source",
            "Year": "year",
            "Abstract": "abstract",
            "PubMed ID": "pmid",
            "DOI": "doi",
            "URL": "url",
        }, inplace = True)
    
        df["id"] = range(1, len(df)+1)
        
        df = pd.DataFrame({
            "id": df["id"],
            "pmid": df["pmid"],
            "source": "Cochrane",
            "doi": df["doi"],
            "authors": df["authors"],
            "journal": df["source"],
            "title": df["title"],
            "abstract": df["abstract"],
            "year": df["year"],
            "language": "English"
        })
    
        df['pmid'] = df['pmid'].astype(str)
        df["authors"] = df["authors"].str.replace(r"[\'\[\]]","", regex = True)
        df["language"] = df["language"].str.replace(r"[\'\[\]]","",regex = True)
        globals()[name] = df
        df.to_csv(f"./data/{name}.csv", encoding = "utf-8")
    cochrane = pd.concat([co_bptb, co_ht, co_qt, co_plt, co_ta])
    cochrane.to_csv(f"./data/cochrane.csv", encoding = "utf-8")
    

**Define variables by grouping** the subgroup data frames.

.. code:: ipython3

    patellar = [pm_bptb, em_bptb, wos_bptb]
    hamstring = [pm_ht, em_ht, wos_ht]
    quadriceps = [pm_qt, em_qt, wos_qt]
    peroneus = [pm_plt, em_plt, wos_plt]
    achilles = [pm_at, em_at, wos_at]
    tibialis = [pm_ta, em_ta, wos_ta]

**Combine dataframes by database** across subgroups and write them to
CSV

.. code:: ipython3

    bptb = pd.concat(patellar).to_csv(f"./data/patellar.csv", encoding = "utf-8")
    ht = pd.concat(hamstring).to_csv(f"./data/hamstring.csv", encoding = "utf-8")
    ta = pd.concat(quadriceps).to_csv(f"./data/tibialis.csv", encoding = "utf-8")
    at = pd.concat(peroneus).to_csv(f"./data/achilles.csv", encoding = "utf-8")
    plt = pd.concat(achilles).to_csv(f"./data/peroneus.csv", encoding = "utf-8")
    qt = pd.concat(tibialis).to_csv(f"./data/quadriceps.csv", encoding = "utf-8")

.. code:: ipython3

    subgroups = [patellar, hamstring, quadriceps, peroneus, achilles, tibialis]

**Combine dataframes by subgroup** across databases and write them to
CSV.

.. code:: ipython3

    records = pd.concat([pubmed, embase, wos, cochrane])
    records.to_csv(f"./data/records.csv", encoding = "utf-8")

.. code:: ipython3

    len(records)




.. parsed-literal::

    1704



.. container::

.. raw:: html

   <hr style="border: none; height: 1.5px; background-color: black;">

.. raw:: html

   <h2 align="center" style="font-family:Times New Roman;font-variant: small-caps;">

Deduplication
*************
The ‘gold-standard’ or consensus agreement among researchers seems to
converge on the idea that removal of duplicate records is best performed
in a process that involves three ordered stages. The first is
deduplication based on a unique record identifier, such as a digital
object identifier (DOI) number, PubMed identifier (PMID) number, or
clinicaltrials.gov (NCT) number. Then, as according to as described for
the second stage, the remaining records were deduplicated based on a
concatenated column consisting of the title, author, and year. The title
was standardized by converting to sentence case, and punctuation marks
and white spaces were removed. The character length was decreased to 50.
For the authors column, the last name of the first author was chosen to
be used. For the year of publication, the year was extracted from the
date of publication in the electronic version of the journal and
converted into a string data structure.

.. code:: ipython3

    def deduplication(df, columns):
        if isinstance(columns, str):
            columns = [columns]
            
        nulls_mask = df[columns].isnull().any(axis=1)
    
        df_nulls = df[nulls_mask]
        df_non_nulls = df[~nulls_mask]
    
        duplicates_mask = df_non_nulls.duplicated(
            subset=columns,
            keep=False,
        )
    
        df_duplicates = df_non_nulls[duplicates_mask]
        df_non_duplicates = df_non_nulls[~duplicates_mask]
    
        df_kept = df_duplicates.drop_duplicates(
            subset=columns,
            keep="first",
        )
    
        df_removed = df_duplicates.loc[
            ~df_duplicates.index.isin(df_kept.index)
        ]
    
        df_unique = df_non_nulls.drop_duplicates(subset=columns)
    
        df_deduplicated = pd.concat(
            [df_non_duplicates, df_kept, df_nulls],
            ignore_index=True,
        )
    
        return df_deduplicated

.. code:: ipython3

    records = deduplication(records, "doi")

.. code:: ipython3

    len(records)




.. parsed-literal::

    925



.. code:: ipython3

    df = deduplication(records, "pmid")
    df.to_csv("./data/title_screening.csv", encoding = "utf-8")

.. code:: ipython3

    len(df)




.. parsed-literal::

    908


Screening
*********

Title and abstract screening
============================

.. code:: ipython3

    import pandas as pd
    
    df = pd.read_csv("./data/full_text_screening.csv", encoding = "utf-8")
    df = df[["DOI", "Author", "Publication Year"]]
    df = df.sort_values(by = ["Publication Year"], ascending = False)
    df = df.sort_values(by = ["Author"], ascending = True)

    df_to_markdown_table(df)


+-----+----------------------------------+-------------------------------------------------+-------------+
|     | DOI                              | Author                                          | Publication |
|     |                                  |                                                 | Year        |
+=====+==================================+=================================================+=============+
| 67  | 10.1007/s00167-008-0645-4        | Ageberg E; Roos HP; Silbernagel KG; Thomeé R;   | 2009        |
|     |                                  | Roos EM                                         |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 83  | nan                              | Aglietti P; Giron F; Buzzi R; Biddau F; Sasso F | 2004        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 65  | 10.1007/s00167-009-0846-5        | Ahldén M; Kartus J; Ejerhed L; Karlsson J;      | 2009        |
|     |                                  | Sernert N                                       |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 37  | 10.1177/0363546516638387         | Akelman MR; Fadale PD; Hulstyn MJ; Shalvoy RM;  | 2016        |
|     |                                  | Garcia A; Chin KE; Duryea J; Badger GJ; Tung    |             |
|     |                                  | GA; Fleming BC                                  |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 91  | 10.1177/03635465010290030201     | Anderson AF; Snyder RB; Lipscomb AB Jr          | 2001        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 15  | 10.1177/23259671231210035        | Anz AW; Jordan SE; Ostrander RV 3rd; Branch EA; | 2023        |
|     |                                  | Denney TS; Cohen A; Andrews JR                  |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 90  | 10.1177/03635465010290060901     | Aune AK; Holm I; Risberg MA; Jensen HK; Steen H | 2001        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 60  | 10.1177/0363546510369549         | Barenius B; Nordlander M; Ponzer S; Tidermark   | 2010        |
|     |                                  | J; Eriksson K                                   |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 48  | 10.1177/0363546514526139         | Barenius B; Ponzer S; Shalabi A; Bujak R;       | 2014        |
|     |                                  | Norlén L; Eriksson K                            |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 22  | 10.1007/s00402-020-03508-1       | Barié A; Sprinckstub T; Huber J; Jaber A        | 2020        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 89  | 10.2106/00004623-200209000-00001 | Beynnon BD; Johnson RJ; Fleming BC; Kannus P;   | 2002        |
|     |                                  | Kaplan M; Samani J; Renström P                  |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 32  | 10.1055/s-0038-1627466           | Bi M; Zhao C; Zhang S; Yao B; Hong Z; Bi Q      | 2018        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 36  | 10.1177/0363546516646378         | Björnsson H; Samuelsson K; Sundemo D; Desai N;  | 2016        |
|     |                                  | Sernert N; Rostgård-Christensen L; Karlsson J;  |             |
|     |                                  | Kartus J                                        |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 40  | 10.1177/0363546515596406         | Bottoni CR; Smith EL; Shaha J; Shaha SS; Raybin | 2015        |
|     |                                  | SG; Tokish JM; Rowles DJ                        |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 96  | 10.1053/jars.2000.18240          | Brand J Jr; Hamilton D; Selby J; Pienkowski D;  | 2000        |
|     |                                  | Caborn DN; Johnson DL                           |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 7   | 10.1177/23259671251320972        | Breker AN; Badger GJ; Kiapour AM; Costa MQ;     | 2025        |
|     |                                  | Fleming EN; Ferrara SL; Chrostek CA; Fadale PD; |             |
|     |                                  | Hulstyn MJ; Shalvoy RM; Gil HC; Fleming BC      |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 33  | 10.1016/j.aott.2017.02.011       | Buescu CT; Onutu AH; Lucaciu DO; Todor A        | 2017        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 11  | 10.1007/s00402-024-05639-1       | Butt U; Vuletic F; Shaikh MAA; Amanullah;       | 2024        |
|     |                                  | Rehman GU; Shah IA; Stålman A; Khan ZA          |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 10  | 10.1002/ksa.12583                | Calvert ND; Ebert JR; Radic R                   | 2025        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 98  | 10.1053/ar.1999.v15.0150161      | Carter TR; Edinger S                            | 1999        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 0   | 10.1016/j.jclinepi.2020.01.008   | Clark, Justin; Glasziou, Paul; Del Mar, Chris;  | 2020        |
|     |                                  | Bannach-Brown, Alexandra; Stehlik, Paulina;     |             |
|     |                                  | Scott, Anna Mae                                 |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 29  | 10.1177/2325967118800298         | Covey DC; Sandoval KE; Riffenburgh RH           | 2018        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 16  | 10.1016/j.jisako.2022.04.002     | Cruz CA; Mannino BJ; Pike A; Thoma D; Lindell   | 2022        |
|     |                                  | K; Kerbel YE; McCadden A; Lopez AJ; Bottoni CR  |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 87  | 10.1177/03635465030310011401     | Ejerhed L; Kartus J; Sernert N; Köhler K;       | 2003        |
|     |                                  | Karlsson J                                      |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 95  | 10.1302/0301-620x.83b3.11685     | Eriksson K; Anderberg P; Hamberg P; Löfgren AC; | 2001        |
|     |                                  | Bredenberg M; Westman I; Wredmark T             |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 92  | nan                              | Eriksson K; Anderberg P; Hamberg P; Olerud P;   | 2001        |
|     |                                  | Wredmark T                                      |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 86  | 10.1177/03635465030310041501     | Feller JA; Webster KE                           | 2003        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 9   | nan                              | García-Linage R; Lassard-Rosenthal J;           | 2025        |
|     |                                  | Noval-García R; Muñiz-Madrazo A; Fraind-Maya G; |             |
|     |                                  | Palmero-Picazo J; German-Córdoba I;             |             |
|     |                                  | Zimbrón-López D                                 |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 69  | 10.2106/JBJS.F.00385             | Gerber JP; Marcus RL; Dibble LE; Greis PE;      | 2007        |
|     |                                  | Burks RT; LaStayo PC                            |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 62  | 10.1016/j.knee.2009.09.008       | Ghalayini SR; Helm AT; Bonshahi AY; Lavender A; | 2010        |
|     |                                  | Johnson DS; Smith RB                            |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 53  | 10.1007/s00167-012-1947-0        | Gifstad T; Sole A; Strand T; Uppheim G;         | 2013        |
|     |                                  | Grøntvedt T; Drogset JO                         |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 77  | 10.1007/s00167-006-0050-9        | Gobbi A; Francisco R                            | 2006        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 18  | 10.1177/23259671211028168        | Guglielmetti LGB; Salas VER; Jorge PB; Severino | 2021        |
|     |                                  | FR; Duarte A; de Oliveira VM; Cury RPL          |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 76  | 10.1007/s00167-006-0059-0        | Harilainen A; Linko E; Sandelin J               | 2006        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 63  | 10.1007/s00167-009-0961-3        | Heijne A; Werner S                              | 2010        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 61  | 10.1177/0363546509350301         | Holm I; Oiestad BE; Risberg MA; Aune AK         | 2010        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 21  | 10.1007/s00402-021-03862-8       | Horstmann H; Petri M; Tegtbur U; Felmet G;      | 2022        |
|     |                                  | Krettek C; Jagodzinski M                        |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 80  | 10.1016/j.arthro.2004.12.002     | Ibrahim SA; Al-Kussary IM; Al-Misfer AR;        | 2005        |
|     |                                  | Al-Mutairi HQ; Ghafar SA; El Noor TA            |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 35  | 10.1007/s00167-016-4229-4        | Iliopoulos E; Galanis N; Zafeiridis A;          | 2017        |
|     |                                  | Iosifidis M; Papadopoulos P; Potoupnis M;       |             |
|     |                                  | Geladas N; Vrabas IS; Kirkos J                  |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 20  | 10.1007/s00167-021-06585-w       | Irrgang JJ; Tashman S; Patterson CG; Musahl V;  | 2021        |
|     |                                  | West R; Oostdyk A; Galvin B; Poploski K; Fu FH  |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 97  | 10.1007/s001670050166            | Jansson KA; Harilainen A; Sandelin J;           | 1999        |
|     |                                  | Karjalainen PT; Aronen HJ; Tallroth K           |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 88  | 10.1177/03635465030310010501     | Jansson KA; Linko E; Sandelin J; Harilainen A   | 2003        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 5   | 10.1177/23259671251401596        | Johns WL; Voskeridjian A; Miltenberg B;         | 2026        |
|     |                                  | Muchintala R; Dodson CC; Cohen SB; Salvo J;     |             |
|     |                                  | Sherman M; Ciccotti MG; Hammoud S               |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 46  | 10.1007/s00264-014-2495-7        | Kautzner J; Kos P; Hanus M; Trc T; Havlas V     | 2015        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 100 | nan                              | Kohn D                                          | 1990        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 19  | 10.1007/s00402-021-04195-2       | Komzák M; Hart R; Náhlík D; Vysoký R            | 2022        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 38  | 10.1007/s00402-015-2386-4        | Konrads C; Reppenhagen S; Plumhoff P; Hoberg M; | 2016        |
|     |                                  | Rudert M; Barthel T                             |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 66  | nan                              | Laoruengthana A; Pattayakorn S; Chotanaputhi T; | 2009        |
|     |                                  | Kosiyatrakul A                                  |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 51  | 10.1016/j.arthro.2012.05.010     | Lawhorn KW; Howell SM; Traina SM; Gottlieb JE;  | 2012        |
|     |                                  | Meade TD; Freedberg HI                          |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 82  | 10.1016/j.arthro.2004.09.014     | Laxdal G; Kartus J; Hansson L; Heidvall M;      | 2005        |
|     |                                  | Ejerhed L; Karlsson J                           |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 47  | 10.1007/s00508-014-0550-4        | Leitgeb J; Köttstorfer J; Schuster R; Kovar FM; | 2014        |
|     |                                  | Platzer P; Aldrian S                            |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 42  | 10.1016/j.arthro.2015.02.033     | Li J; Wang J; Li Y; Shao D; You X; Shen Y       | 2015        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 70  | 10.1177/0363546506298275         | Lidén M; Ejerhed L; Sernert N; Laxdal G; Kartus | 2007        |
|     |                                  | J                                               |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 26  | 10.1136/bjsports-2019-101000     | Lind M; Nielsen TG; Soerensen OG;               | 2020        |
|     |                                  | Mygind-Klavsen B; Faunø P                       |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 8   | 10.1177/23259671241302348        | Lucidi GA; Agostinone P; Di Paolo S; Dal Fabbro | 2025        |
|     |                                  | G; Serra M; Viotto M; Grassi A; Zaffagnini S    |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 52  | 10.1016/j.knee.2012.02.005       | Lui PP; Cheng YY; Yung SH; Hung AS; Chan KM     | 2012        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 49  | 10.1016/j.arthro.2014.01.012     | Lund B; Nielsen T; Faunø P; Christiansen SE;    | 2014        |
|     |                                  | Lind M                                          |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 72  | 10.1177/0363546506294361         | Maletis GB; Cameron SL; Tengan JJ; Burchette RJ | 2007        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 2   | 10.13107/jocr.2026.v16.i05.7294  | Malik S; Biswas G; Singh SK; Sundaresan N; Bera | 2026        |
|     |                                  | AP; Kyada M                                     |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 14  | 10.1002/ksa.12031                | Martin RK; Marmura H; Wastvedt S; Pareek A;     | 2024        |
|     |                                  | Persson A; Moatshe G; Bryant D; Wolfson J;      |             |
|     |                                  | Engebretsen L; Getgood A                        |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 27  | 10.1016/j.aott.2019.04.012       | Martin-Alguacil JL; Arroyo-Morales M;           | 2019        |
|     |                                  | Martin-Gómez JL; Lozano-Lozano M;               |             |
|     |                                  | Galiano-Castillo N; Cantarero-Villanueva I      |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 30  | 10.1016/j.knee.2018.03.011       | Martin-Alguacil JL; Arroyo-Morales M;           | 2018        |
|     |                                  | Martín-Gomez JL; Monje-Cabrera IM;              |             |
|     |                                  | Abellán-Guillén JF; Esparza-Ros F; Lozano ML;   |             |
|     |                                  | Cantarero-Villanueva I                          |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 78  | 10.1177/0363546505279919         | Matsumoto A; Yoshiya S; Muratsu H; Yagi M;      | 2006        |
|     |                                  | Iwasaki Y; Kurosaka M; Kuroda R                 |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 75  | 10.1016/j.arthro.2006.05.004     | McCormack RG; Greenhow RJ; Fogagnolo F; Shrier  | 2006        |
|     |                                  | I                                               |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 50  | 10.2106/JBJS.L.00724             | Mohammadi F; Salavati M; Akhbari B; Mazaheri M; | 2013        |
|     |                                  | Mohsen Mir S; Etemadi Y                         |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 43  | 10.1097/JSM.0000000000000202     | Mohtadi N; Barber R; Chan D; Paolucci EO        | 2016        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 41  | 10.1097/JSM.0000000000000209     | Mohtadi N; Chan D; Barber R; Paolucci EO        | 2016        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 28  | 10.2106/JBJS.18.01322            | Mohtadi NG; Chan DS                             | 2019        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 59  | 10.1016/j.gaitpost.2010.04.008   | Moraiti CO; Stergiou N; Vasiliadis HS; Motsis   | 2010        |
|     |                                  | E; Georgoulis A                                 |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 44  | 10.1007/s00264-014-2662-x        | Mouzopoulos G; Siebold R; Tzurbakis M           | 2015        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 56  | 10.1007/s00167-010-1388-6        | Noh JH; Yi SR; Song SJ; Kim SW; Kim W           | 2011        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 84  | 10.1177/0363546503261703         | Nurmi JT; Kannus P; Sievänen H; Järvelä T;      | 2004        |
|     |                                  | Järvinen M; Järvinen TL                         |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 99  | nan                              | O’Neill DB                                      | 1996        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 45  | 10.1007/s00264-014-2513-9        | Papalia R; Franceschi F; Tecame A; D’Adamio S;  | 2015        |
|     |                                  | Maffulli N; Denaro V                            |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 81  | nan                              | Pigozzi F; Di Salvo V; Parisi A; Giombini A;    | 2004        |
|     |                                  | Fagnani F; Magini W; Franceschi F; Denaro E     |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 71  | 10.1177/0363546506296042         | Pinczewski LA; Lyman J; Salmon LJ; Russell VJ;  | 2007        |
|     |                                  | Roe J; Linklater J                              |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 13  | 10.1177/03635465241271524        | Popovic M; Myhre JR; Holen JIH; Gifstad T;      | 2024        |
|     |                                  | Strand IL; Strand T; Mo IF; Fischer-Bredenbeck  |             |
|     |                                  | C; Drogset JO                                   |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 58  | 10.1007/s00113-010-1791-y        | Pässler HH                                      | 2010        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 93  | 10.1007/s001130050733            | Röpke M; Becker R; Urbach D; Nebelung W         | 2001        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 54  | 10.1177/0363546511411702         | Sajovic M; Strahovnik A; Dernovsek MZ; Skaza K  | 2011        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 68  | 10.1007/s00264-007-0341-x        | Sajovic M; Strahovnik A; Komadina R; Dernovsek  | 2008        |
|     |                                  | MZ                                              |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 31  | 10.1177/0363546518768768         | Sajovic M; Stropnik D; Skaza K                  | 2018        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 73  | 10.1177/0363546506290726         | Sajovic M; Vengust V; Komadina R; Tavcar R;     | 2006        |
|     |                                  | Skaza K                                         |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 79  | 10.1007/s00264-005-0011-9        | Sato N; Higuchi H; Terauchi M; Kimura M;        | 2005        |
|     |                                  | Takagishi K                                     |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 24  | 10.1007/s40279-020-01276-x       | Sinding KS; Nielsen TG; Hvid LG; Lind M; Dalgas | 2020        |
|     |                                  | U                                               |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 25  | 10.1016/j.arthro.2020.01.048     | Smith PA; Cook CS; Bley JA                      | 2020        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 4   | 10.1016/j.lanepe.2025.101561     | Sonnery-Cottet B; Carrozzo A; Poilvache H;      | 2026        |
|     |                                  | Fayard JM; Freychet B; Thaunat M; Vieira TD;    |             |
|     |                                  | Saithna A                                       |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 23  | 10.1177/2325967120918490         | Sonnery-Cottet B; Pioger C; Vieira TD; Franck   | 2020        |
|     |                                  | F; Kajetanek C; Fayard JM; Thaunat M; Saithna A |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 12  | 10.1177/23259671241292604        | Sumanont S; Jaruwanneechai K; Wittayapairoj A;  | 2024        |
|     |                                  | Apiwatanakul P; Boonrod A                       |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 17  | 10.1007/s00590-023-03636-5       | Tang N; Eren M; Gurpinar T; Ozturkmen Y         | 2024        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 64  | 10.1177/0363546509339577         | Taylor DC; DeBerardino TM; Nelson BJ; Duffey M; | 2009        |
|     |                                  | Tenuta J; Stoneman PD; Sturdivant RX;           |             |
|     |                                  | Mountcastle S                                   |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 85  | 10.1055/s-2003-42153             | Tibesku CO; Springer J; Mastrokalos DS; Pässler | 2003        |
|     |                                  | HH                                              |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 3   | 10.1002/ksa.70275                | Vendrig T; Keizer MNJ; Brouwer RW; Houdijk H;   | 2026        |
|     |                                  | Hoogeslag RAG                                   |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 34  | 10.1016/j.arthro.2016.05.043     | Wasserman BR; Singh BC; Kaplan DJ; Weinberg M;  | 2017        |
|     |                                  | Meislin R; Jazrawi LM; Strauss EJ               |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 94  | 10.1007/s001670100191            | Webster KE; Feller JA; Hameister KA             | 2001        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 55  | 10.1016/j.arthro.2011.01.015     | Wipfler B; Donner S; Zechmann CM; Springer J;   | 2011        |
|     |                                  | Siebold R; Paessler HH                          |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 6   | 10.1007/s00590-025-04510-2       | Yadav AK; Sharma A; Paul N; Bhakhar A; Sarkar   | 2025        |
|     |                                  | B; Azam MQ                                      |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 1   | 10.1007/s00264-019-04417-8       | Yang, Xiong-gang; Wang, Feng; He, Xin; Feng,    | 2020        |
|     |                                  | Jiang-tao; Hu, Yong-cheng; Zhang, Hao; Yang,    |             |
|     |                                  | Li; Hua, Kunchi                                 |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 39  | 10.1007/s00167-015-3955-3        | Yoo SH; Song EK; Shin YR; Kim SK; Seon JK       | 2017        |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 57  | 10.1007/s00167-010-1225-y        | Zaffagnini S; Bruni D; Marcheggiani Muccioli    | 2011        |
|     |                                  | GM; Bonanzinga T; Lopomo N; Bignozzi S;         |             |
|     |                                  | Marcacci M                                      |             |
+-----+----------------------------------+-------------------------------------------------+-------------+
| 74  | 10.1007/s00167-006-0130-x        | Zaffagnini S; Marcacci M; Lo Presti M; Giordano | 2006        |
|     |                                  | G; Iacono F; Neri MP                            |             |
+-----+----------------------------------+-------------------------------------------------+-------------+

Full-text screening
===================

+----+-----+----------------------+-----------+-------------+-----------------------------------+
|    | id  | study                | screening | subgroups   | outcomes                          |
+====+=====+======================+===========+=============+===================================+
| 0  | 1   | ageberg_2009         | Included  | patellar,   | Tegner                            |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 1  | 2   | aglietti_2004        | Included  | patellar,   | Lachman, Pivot shift,             |
|    |     |                      |           | hamstring   | Instrumental laxity               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 2  | 3   | ahldén_2009          | Included  | patellar,   | Tegner, Lysholm, Lachman,         |
|    |     |                      |           | hamstring   | Instrumental laxity               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 3  | 4   | akelman_2016         | Included  | patellar,   | Instrumental laxity               |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 4  | 5   | anderson_2001        | Included  | patellar,   | IKDC, Instrumental laxity, Pivot  |
|    |     |                      |           | hamstring   | shift                             |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 5  | 6   | anz_2023             | Included  | patellar,   | Graft rupture                     |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 6  | 7   | aune_2001            | Included  | patellar,   | Instrumental laxity               |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 7  | 8   | barenius_2010        | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 8  | 9   | barenius_2014        | Included  | patellar,   | IKDC, Lysholm, Lachman, Pivot     |
|    |     |                      |           | hamstring   | shift, Instrumental laxity        |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 9  | 10  | barié_2020           | Included  | patellar,   | IKDC, Lysholm, Tegner,            |
|    |     |                      |           | quadriceps  | Instrumental laxity, Graft        |
|    |     |                      |           |             | rupture                           |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 10 | 11  | beynnon_2002         | Included  | patellar,   | IKDC, Tegner, Instrumental        |
|    |     |                      |           | hamstring   | laxity, Pivot shift, Lachman      |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 11 | 12  | bi_2018              | Included  | hamstring,  | IKDC, Instrumental laxity, Pivot  |
|    |     |                      |           | peroneus    | shift, Graft rupture              |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 12 | 13  | björnsson_2016       | Included  | patellar,   | Instrumental laxity, IKDC,        |
|    |     |                      |           | hamstring   | Tegner, Lysholm                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 13 | 14  | bottoni_2015         | Included  | hamstring,  | IKDC, Tegner                      |
|    |     |                      |           | tibialis    |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 14 | 15  | brand_2000           | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 15 | 16  | breker_2025          | Included  | patellar,   | Instrumental laxity               |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 16 | 17  | buescu_2017          | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 17 | 18  | butt_2024            | Included  | hamstring,  | Lysholm, IKDC, Lachman, Pivot     |
|    |     |                      |           | peroneus    | shift                             |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 18 | 19  | calvert_2025         | Included  | hamstring,  | IKDC, Instrumental laxity         |
|    |     |                      |           | quadriceps  |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 19 | 20  | carter_edinger_1999  | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 20 | 21  | covey_2018           | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 21 | 22  | cruz_2022            | Included  | hamstring,  | Graft rupture                     |
|    |     |                      |           | tibialis    |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 22 | 23  | ejerhed_2003         | Included  | patellar,   | Tegner, Lysholm, Instrumental     |
|    |     |                      |           | hamstring   | laxity, Lachman                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 23 | 24  | eriksson_2001        | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 24 | 25  | eriksson_2006        | Included  | patellar,   | Instrumental laxity, Pivot shift  |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 25 | 26  | feller_webster_2003  | Included  | patellar,   | IKDC, Instrumental laxity, Pivot  |
|    |     |                      |           | hamstring   | shift, Lachman                    |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 26 | 27  | garcia-linage_2025   | Excluded  | nan         | Non-English.                      |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 27 | 28  | gerber_2007          | Included  | patellar,   | Instrumental laxity               |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 28 | 29  | ghalayini_2010       | Excluded  | nan         | Did not compare at least two of   |
|    |     |                      |           |             | the specified subgroups.          |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 29 | 30  | gifstad_2013         | Included  | patellar,   | Tegner, Lysholm, Instrumental     |
|    |     |                      |           | hamstring   | laxity, Lachman                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 30 | 31  | gobbi_francisco_2006 | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 31 | 32  | guglielmetti_2021    | Included  | patellar,   | IKDC, Lysholm, Pivot shift,       |
|    |     |                      |           | hamstring   | Lachman                           |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 32 | 33  | harilainen_2006      | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity, Pivot shift  |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 33 | 34  | heijne_werner_2010   | Included  | patellar,   | Tegner, Instrumental laxity,      |
|    |     |                      |           | hamstring   | Pivot shift                       |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 34 | 35  | holm_2010            | Included  | patellar,   | Instrumental laxity, Tegner       |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 35 | 36  | horstmann_2022       | Included  | hamstring,  | IKDC, Lysholm, Instrumental       |
|    |     |                      |           | quadriceps  | laxity                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 36 | 37  | ibrahim_2005         | Included  | patellar,   | Lachman, Lysholm, Instrumental    |
|    |     |                      |           | hamstring   | laxity, Pivot shift               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 37 | 38  | iliopoulos_2017      | Included  | patellar,   | IKDC, Lysholm, Pivot shift,       |
|    |     |                      |           | hamstring   | Lachman                           |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 38 | 39  | irrgang_2021         | Excluded  | nan         | Did not compare at least two of   |
|    |     |                      |           |             | the specified subgroups.          |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 39 | 40  | jansson_1999         | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 40 | 41  | jansson_2003         | Included  | patellar,   | Lachman, Pivot shift,             |
|    |     |                      |           | hamstring   | Instrumental laxity, Lysholm,     |
|    |     |                      |           |             | Tegner                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 41 | 42  | johns_2026           | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 42 | 43  | kautzner_2015        | Included  | patellar,   | Lysholm, Instrumental laxity      |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 43 | 44  | komzak_2022          | Included  | patellar,   | IKDC, Lysholm                     |
|    |     |                      |           | quadriceps  |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 44 | 45  | konrads_2016         | Included  | patellar,   | Instrumental laxity, Pivot shift, |
|    |     |                      |           | hamstring   | Lachman, IKDC, Tegner, Lysholm    |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 45 | 46  | laoruengthana_2009   | Included  | patellar,   | Instrumental laxity, Pivot shift, |
|    |     |                      |           | hamstring   | IKDC, Lysholm                     |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 46 | 47  | lawhorn_2012         | Included  | hamstring,  | IKDC, Instrumental laxity, Pivot  |
|    |     |                      |           | tibialis    | shift                             |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 47 | 48  | laxdal_2004          | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 48 | 49  | laxdal_2005          | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 49 | 50  | leitgeb_2014         | Included  | patellar,   | Lachman, Instrumental laxity      |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 50 | 51  | li_2015              | Included  | hamstring,  | Instrumental laxity, Pivot shift, |
|    |     |                      |           | tibialis    | Lachman, IKDC, Tegner, Lysholm    |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 51 | 52  | lidén_2007           | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity, Lachman      |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 52 | 53  | lind_2020            | Included  | hamstring,  | IKDC, Tegner, Instrumental        |
|    |     |                      |           | quadriceps  | laxity, Pivot shift               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 53 | 54  | lucidi_2025          | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity, Pivot shift, |
|    |     |                      |           |             | Graft rupture                     |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 54 | 55  | lui_2012             | Included  | patellar,   | IKDC, Lysholm, Instrumental       |
|    |     |                      |           | hamstring   | laxity, Lachman                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 55 | 56  | lund_2014            | Included  | patellar,   | Instrumental laxity, IKDC         |
|    |     |                      |           | quadriceps  |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 56 | 57  | maletis_2007         | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 57 | 58  | malik_2026           | Included  | hamstring,  | Instrumental laxity, Pivot shift, |
|    |     |                      |           | peroneus    | Lachman, IKDC, Lysholm, Tegner    |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 58 | 59  | martin_2024          | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 59 | 60  | martin-alguacil_2018 | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 60 | 61  | martin-alguacil_2019 | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 61 | 62  | matsumoto_2006       | Included  | patellar,   | IKDC, Instrumental laxity         |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 62 | 63  | mccormack_2006       | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 63 | 64  | mohammadi_2013       | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 64 | 65  | mohtadi_2016a        | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 65 | 66  | mohtadi_2016b        | Included  | patellar,   | Instrumental laxity, Lachman,     |
|    |     |                      |           | hamstring   | Graft rupture                     |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 66 | 67  | mohtadi_chan_2019    | Included  | patellar,   | IKDC, Pivot shift, Lachman,       |
|    |     |                      |           | hamstring   | Instrumental laxity, Graft        |
|    |     |                      |           |             | rupture                           |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 67 | 68  | moraiti_2010         | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity, Lachman,     |
|    |     |                      |           |             | Graft rupture                     |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 68 | 69  | mouzopoulos_2015     | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 69 | 70  | noh_2011             | Included  | hamstring,  | Lachman, IKDC, Tegner, Lysholm,   |
|    |     |                      |           | Achilles    | Instrumental laxity, Pivot shift, |
|    |     |                      |           |             | Graft rupture                     |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 70 | 71  | nurmi_2004           | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 71 | 72  | oneill_1996          | Included  | patellar,   | IKDC, Lysholm, Instrumental       |
|    |     |                      |           | hamstring   | laxity                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 72 | 73  | papalia_2015         | Included  | patellar,   | IKDC, Lysholm                     |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 73 | 74  | pässler_2015         | Excluded  | nan         | Non-English.                      |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 74 | 75  | pigozzi_2004         | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 75 | 76  | pinczewski_2007      | Included  | patellar,   | IKDC, Lysholm, Lachman, Pivot     |
|    |     |                      |           | hamstring   | shift, Instrumental laxity        |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 76 | 77  | popovic_2024         | Included  | patellar,   | Lysholm, Tegner, Instrumental     |
|    |     |                      |           | hamstring   | laxity, Pivot shift, Lachman      |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 77 | 78  | röpke_2001           | Excluded  | nan         | Non-English.                      |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 78 | 79  | sajovic_2006         | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 79 | 80  | sajovic_2008         | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 80 | 81  | sajovic_2011         | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 81 | 82  | sajovic_2018         | Included  | patellar,   | IKDC, Lysholm, Instrumental       |
|    |     |                      |           | hamstring   | laxity, Pivot shift, Lachman      |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 82 | 83  | sato_2005            | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 83 | 84  | sinding_2020         | Included  | hamstring,  | IKDC                              |
|    |     |                      |           | quadriceps  |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 84 | 85  | smith_2020           | Included  | patellar,   | IKDC, Instrumental laxity, Graft  |
|    |     |                      |           | hamstring,  | rupture                           |
|    |     |                      |           | quadriceps  |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 85 | 86  | sonnery-cottet_2020  | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity, Pivot shift, |
|    |     |                      |           |             | Lachman                           |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 86 | 87  | sonnery-cottet_2026  | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity, Pivot shift, |
|    |     |                      |           |             | Graft rupture                     |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 87 | 88  | sumanont_2024        | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 88 | 89  | tang_2023            | Included  | hamstring,  | IKDC                              |
|    |     |                      |           | quadriceps  |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 89 | 90  | taylor_2009          | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity, Pivot shift  |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 90 | 91  | tibesku_2003         | Excluded  | nan         | Non-English.                      |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 91 | 92  | vendrig_2026         | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 92 | 93  | vilchez-cavazos_2020 | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | quadriceps  | Instrumental laxity               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 93 | 94  | wasserman_2017       | Excluded  | nan         | Did not report any of the         |
|    |     |                      |           |             | specified outcomes.               |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 94 | 95  | webster_2001         | Included  | patellar,   | IKDC, Instrumental laxity         |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 95 | 96  | wipfler_2011         | Included  | patellar,   | IKDC, Tegner, Lysholm,            |
|    |     |                      |           | hamstring   | Instrumental laxity, Pivot shift, |
|    |     |                      |           |             | Lachman, Graft rupture            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 96 | 97  | yadav_2025           | Included  | hamstring,  | Lysholm, Instrumental laxity,     |
|    |     |                      |           | quadriceps  | Pivot shift, Lachman              |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 97 | 98  | yoo_2017             | Included  | hamstring,  | Tegner, Lysholm, Instrumental     |
|    |     |                      |           | tibialis    | laxity, Pivot shift, Lachman      |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 98 | 99  | zaffagnini_2006      | Excluded  | nan         | Duplicate report of the same      |
|    |     |                      |           |             | study.                            |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
| 99 | 100 | zaffagnini_2011      | Included  | patellar,   | IKDC, Instrumental laxity         |
|    |     |                      |           | hamstring   |                                   |
+----+-----+----------------------+-----------+-------------+-----------------------------------+
