def eligibility_criteria():
    P = f"""Adult patients with post-traumatic grade III (complete tear) of unilateral anterior cruciateligament are included. Both genders are included, and upper limit in age is unrestricted. Only studies with mean age greater than or equal to 18 years old across all patients will be presumed to have targeted a population that is considered skeletally-mature."""
    I = f"""Primary anterior cruciate ligament reconstruction (ACLR) surgeries are included. ACLRs performed simultaneously on both knees, in conjunction with other ligamental reconstructions aside from meniscal, and revision ACLRs were excluded."""
    C = f"""Autologous grafts: bone-patellar tendon-bone, hamstring tendon, quadriceps tendon,and peroneus longus tendon are included. Allogenic grafts: Achilles tendon and tibialis anterior and posterior are also included. All other graft types, such as synthetic grafts and allogenic versions of commonly used autologous ones are excluded (the Achillesand tibialis tendon grafts are included despite being allogenic because autologous versions cannot be grafted in patients due to the important roles the muscle from whichthe tendon is attached plays in normal physiologic biomechanics)."""
    O = f"""The outcomes of interest were measures of (1) patient-reported outcome measures(PROMs) of patient satisfaction as surrogate measure for subjective quality oflife—answering the question of how much is the patient able to live as close to preinjury state; (2) Objective measures of translational and rotational knee stability; and(3) Adverse events and complications. In (1), the primary (most commonly reported) outcomes were included: IKDC subjective knee form (SKF), Lysholm and Tegner. For(2), instrumental laxity (side-to-side difference in millimeters) of antero-posterior translation by the anterior drawer test, pivot shift and Lachman tests were included. For(3) graft failure, including re-re-rupture of graft (confirmed via imaging), clinical failure(defined by clinical failure during objective measures) and revision surgeries(arthroscopic confirmation of tears).Other outcomes that were excluded were due to their deemed incompatibility forcomparisons across all grafts. For example, hamstring and quadriceps muscle strength recovery is not a relevant outcome measure for determining effectiveness of ACLR when comparing across grafts in which some were not taken from the patients' hamstring or quadriceps muscle, or is a component that disrupts such biomechanicalphysiology. Donor site morbidity is another example of an outcome that may be out ofrange in scope, due to the variety of definitions for consistent applicability incomparisons. Other outcomes such as Marx, KOOS, VAS, were excluded due to thelow number of studies that reported these outcome measures, in comparison to theother ones that surrogatively measure the same thing."""
    S = f"""Only randomized controlled trials will be included into the qualitative and quantitative portions of the review."""
    
    description = [P, I, C, O, S]
    inclusion = ["Adult patients", "Primary ACLR", "Bone-patellar tendon-bone, hamstring tendon, quadriceps, or peroneus longus tendon autologous grafts, or Achilles tendon or tibialis anterior/posterior tendon allogenic grafts.", "Primary outcomes of interest: IKDC subjective, Lysholm, Tegner, pivot shift, Lachman, instrumental laxity, graft rupture, graft failure, revision rate", "Randomized controlled trials"]
    exclusion = ["Pediatric patients", "Revision ACLR or ACL repair (BEAR)", "All other graft types (LET)", "Secondary outcomes of interest", "Non-randomized clinical trials and observational studies"]
    
    import pandas as pd
    df = pd.DataFrame({
        " ": ["P", "I", "C", "O", "S"],
        "Categories": ["Population", "Intervention", "Comparators", "Outcomes", "Study Design"],
        "Description": description,
        "Inclusion criteria": inclusion,
        "Exclusion criteria": exclusion,
    #    "Key words": ["","","","",""],
    })
    from IPython.display import display, HTML, Markdown, Latex
    display(Markdown(df.to_markdown(index = False)))
