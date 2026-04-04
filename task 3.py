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