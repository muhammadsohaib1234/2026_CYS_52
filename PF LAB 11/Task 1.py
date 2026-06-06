# TASK 1

students = {}

num = int(input("Enter number of students: "))

for i in range(num):

    name = input("Enter student name: ")

    total = int(input("Enter total marks: "))

    while total <= 0:
        print("Total marks cannot be zero or negative")
        total = int(input("Enter total marks again: "))

    obtained = int(input("Enter obtained marks: "))

    while obtained > total:
        print("Obtained marks cannot be greater than total marks")
        obtained = int(input("Enter obtained marks again: "))

    percentage = (obtained / total) * 100

    if percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
        grade = "D"

    else:
        grade = "F"

    students[name] = {
        "Total Marks": total,
        "Obtained Marks": obtained,
        "Percentage": percentage,
        "Grade": grade
    }

print("\nStudent Record")

for key, value in students.items():
    print("\nName:", key)
    print("Total Marks:", value["Total Marks"])
    print("Obtained Marks:", value["Obtained Marks"])
    print("Percentage:", value["Percentage"])
    print("Grade:", value["Grade"])
