def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


def main():
    students = {}

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("\nEnter student name: ")
        marks = int(input("Enter marks: "))

        students[name] = marks

    print("\n--- Grade Report ---")

    for name, marks in students.items():
        grade = get_grade(marks)
        print(name, ":", marks, "-", grade)


main()
