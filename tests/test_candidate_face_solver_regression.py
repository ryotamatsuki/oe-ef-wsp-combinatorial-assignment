from src.candidate_face_solver import known_good_witness_is_accepted, solve_six_type_baseline


def test_six_type_explicit_mechanism_is_accepted_by_solver():
    ok, failure = known_good_witness_is_accepted()
    assert ok, failure


def test_candidate_solver_six_type_sat():
    result = solve_six_type_baseline()
    assert result["status"] == "SAT"
    assert result["profiles"] == 216
