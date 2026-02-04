# test_student_grade.py

from src.student_grade_calculator import calculate_grade
from tests.student_grade import get_grade


def test_grade_A_plus():
    avg, grade = get_grade([95, 92, 90, 93, 94])
    assert grade == "A+"

def test_grade_A():
    avg, grade = get_grade([80, 78, 76, 75, 77])
    assert grade == "A"

def test_grade_B():
    avg, grade = get_grade([65, 62, 60, 63, 61])
    assert grade == "B"

def test_grade_C():
    avg, grade = get_grade([52, 55, 50, 53, 54])
    assert grade == "C"

def test_grade_Fail():
    avg, grade = get_grade([40, 45, 48, 42, 44])
    assert grade == "Fail"
