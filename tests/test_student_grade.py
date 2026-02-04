from src.student_grade_calculator import get_grade

def test_A_plus():
    _, grade = get_grade([95, 92, 90, 93, 94])
    assert grade == "A+"

def test_A():
    _, grade = get_grade([80, 78, 76, 75, 77])
    assert grade == "A"

def test_B():
    _, grade = get_grade([65, 62, 60, 63, 61])
    assert grade == "B"

def test_C():
    _, grade = get_grade([52, 55, 50, 53, 54])
    assert grade == "C"

def test_Fail():
    _, grade = get_grade([40, 45, 48, 42, 44])
    assert grade == "Fail"
