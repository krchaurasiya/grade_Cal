# student_grade.py

def get_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return average, "A+"
    elif average >= 75:
        return average, "A"
    elif average >= 60:
        return average, "B"
    elif average >= 50:
        return average, "C"
    else:
        return average, "Fail"
