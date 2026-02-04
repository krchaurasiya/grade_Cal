def calculate_grade(marks):
    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return avg, grade


if __name__ == "__main__":
    marks = [float(input(f"Enter marks of Subject {i}: ")) for i in range(1, 6)]
    average, grade = calculate_grade(marks)

    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
    
