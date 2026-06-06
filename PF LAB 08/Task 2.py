# Task 2

# if elif statement

# EXAMPLE 1

obtained_marks=int(input("enter the number of obtained marks:"))
if obtained_marks>=90:
    print("Grade A+:")
elif obtained_marks>=85:
    print("Grade A:")
elif obtained_marks>=80:
    print("Grade A-:")
elif obtained_marks>=75:
    print("Grade B+:")
elif obtained_marks>=70:
    print("Grade B:")
elif obtained_marks>=65:
    print("Grade B-:")
elif obtained_marks>=60:
    print("Grade C+:")
elif obtained_marks>=55:
    print("Grade C:")
elif obtained_marks>=50:
    print("Grade C-:")
elif obtained_marks<<50:
    print("Grade F:")

# EXAPMLE 2

obtained_marks = int(input("Enter obtained marks:"))
total_marks = 300
if obtained_marks<0 or obtained_marks>300:
    print("invalid choice:")
else:
    percentage = (obtained_marks/total_marks)*100
    print(percentage)
    if percentage >= 90:
        print("Grade A+:")
    elif percentage >= 85:
        print("Grade A-:")
    elif percentage >= 80:
        print("Grade B+:")
    elif percentage >= 75:
        print("Grade B-:")
    elif percentage >= 70:
        print("Grade C+:")
    elif percentage >= 65:
        print("Grade C-:")
    elif percentage >= 60:
        print("Grade D+:")
    elif percentage <60:
        print("Grade F:")
