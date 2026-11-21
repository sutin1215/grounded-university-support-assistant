# Blind hand-label check of the LLM judge

- Sample: 30 answers to answerable pilot questions, 10 each from S1, S2, S3 (random, seed 2026), labelled by hand without seeing the system, judge or reference label.

- Judge vs my blind labels: 26/30 agree (87%), Cohen's kappa 0.75
- Reference labels vs my blind labels: 26/30 agree (87%), Cohen's kappa 0.75
- S1: judge agrees with me on 10/10
- S2: judge agrees with me on 6/10
- S3: judge agrees with me on 10/10

Disagreements: Q03/S2 (me CORRECT, judge PARTIAL, reference WRONG); Q18/S2 (me CORRECT, judge WRONG, reference PARTIAL); Q10/S2 (me CORRECT, judge PARTIAL, reference CORRECT); Q19/S2 (me CORRECT, judge CORRECT, reference PARTIAL); Q08/S2 (me CORRECT, judge PARTIAL, reference WRONG)

Small sample: indicative only.
