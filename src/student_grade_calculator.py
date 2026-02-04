# Function to calculate grade
def calculate_grade():
    # Take marks of 5 subjects
    m1 = float(input("Enter marks of Subject 1: "))
    m2 = float(input("Enter marks of Subject 2: "))
    m3 = float(input("Enter marks of Subject 3: "))
    m4 = float(input("Enter marks of Subject 4: "))
    m5 = float(input("Enter marks of Subject 5: "))

    # Calculate average
    average = (m1 + m2 + m3 + m4 + m5) / 5

    # Display average
    print("Average Marks:", average)

    # Decide grade
    if average >= 90:
        print("Grade: A+")
    elif average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")


# Function call
if __name__ == "__main__":
    calculate_grade()
