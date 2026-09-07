# Candidate-face solver status

The historical candidate-face source code is not available in this repository or recovered artifacts. Do not infer its line-level bug.

`src/candidate_face_solver.py` is deliberately a **baseline acceptance gate**, not a replacement general solver. It returns SAT by exhibiting the known-good explicit witness and verifies feasibility, EF, and the analytic OE characterization.

Any future generic face enumerator / WSP branch solver must be added here only after it passes the known-good witness regression test.
