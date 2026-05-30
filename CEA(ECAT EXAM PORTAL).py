#================================

#||||||- ECAT EXAM PORTAL -||||||

#================================

#  QUESTION BANK

questions=[
{"subject": "physics",
"question": "what is unit of force?",
"A": "kg",
"B": "N",
"C": "Ns",
"D": "J",
"correct": "B"
},
{"subject": "physics",
"question": "mass per unit volume is called?",
"A": "force",
"B": "density",
"C": "current",
"D": "inertia",
"correct": "B"

},
{
    "subject": "physics",
    "question": "newton 1st law of motion is also called the law of ?",
    "A": "acceleration",
    "B": "inertia",
    "C": "action and reaction",
    "D": "gravitation",
    "correct": "B"

},
{
    "subject": "chemistry",
    "question": "what is the most abundant gas in atmosphere?",
    "A": "oxygen",
    "B": "carbon dioxide",
    "C":"nitrogen",
    "D":"argon",
    "correct": "C"
},
{
    "subject": "chemistry",
    "question": "what is the PH of neutral solution at 25 degree celsius?",
    "A":"0",
    "B":"7",
    "C":"14",
    "D":"1",
    "correct": "B"
},
{
    "subject": "chemistry",
    "question": "rust is chemically known as ?",
    "A": "iron oxide ",
    "B":"iron sulfide",
    "C":"iron chloride",
    "D": "iron carbonate",
    "correct": "A"

 },
{
    "subject": "biology",
    "question": "what is the power house of the cell?",
    "A": "nucleus",
    "B": "ribosome",
    "C": "mitochondria",
    "D": "chloroplast",
    "correct": "C"
},
{
    "subject": "biology",
    "question": "which blood cells are responsible for fighting infections?",
    "A": "plasma",
    "B": "platelets",
    "C":"red blood cells",
    "D":"white blood cells",
    "correct": "D"

},
{
    "subject": "biology",
    "question": "which part of plant conducts photosynthesis?",
    "A": "root",
    "B": "stem",
    "C":"flower",
    "D": "leaf",
    "correct": "D"
},
{
    "subject": "english",
    "question": "the correct synonym of rapid is?",
    "A":" slow",
    "B":" quick",
    "C":" lazy",
    "D":" heavy",
    "correct": "B"
}

]

#---------------------------

# RESULT STORAGE SYSTEM

#---------------------------

results=[]

#---------------------------

# MAIN MENU STRUCTURE

#---------------------------

def main_menu():
    while True:
        print("---------------------------")
        print("||||||ECAT EXAM SYSTEM||||||")
        print("---------------------------")

        print("1.  ADMIN PORTAL ")
        print("2.  STUDENT PORTAL")
        print("3.  EXIT")
        choice=int(input("Enter your choice: "))
        if choice==1:
            admin_login()
        elif choice==2:
            student_login()
        elif choice==3:
            print("Program Closed")
            break
        else:
            print("Invalid Choice")

#--------------------

# ADMIN LOGIN

#--------------------

def admin_login():
    admin_username="$OH@!B46"
    admin_password="SHABY2026"

    attempts=0
    while attempts<3:
        print(" ---ADMIN LOGIN--- ")
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        if username==admin_username and password==admin_password:
            print("Login Successful")
            admin_menu()
            return
        else:
            attempts+=1
            remaining_attempts=3-attempts
            print("Invalid Username or Password")
            print("Remaining Attempts: ",remaining_attempts)

    print("ADMIN PORTAL LOCKED")

#-------------------------

# STUDENT LOGIN

#-------------------------

def student_login():
    student_username="Z@!FU21"
    student_password="21122021"

    attempts=0
    while attempts<3:
        print(" ---STUDENT LOGIN--- ")
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        if username==student_username and password==student_password:
            print("Login Successful")
            name=input("Enter your name: ")
            roll_number=input("Enter your roll number: ")
            student_menu(name,roll_number)
            return
        else:
            attempts+=1
            remaining_attempts=3-attempts
            print("Invalid Username or Password")
            print("Remaining Attempts: ",remaining_attempts)

    print("STUDENT PORTAL LOCKED")

#-----------------------

# ADMIN MENU

#-----------------------

def admin_menu():
    while True:

        print("------ADMIN MENU------")

        print("1. View Questions ")
        print("2. Add Question ")
        print("3. Delete Question ")
        print("4. View All Results")
        print("5. View Detailed Result")
        print("6. View Statistics")
        print("7. Logout ")

        choice=int(input("Enter your choice: "))
        if choice==1:
            view_question()

        elif choice==2:
            add_question()

        elif choice==3:
            delete_question()

        elif choice==4:
            view_results()

        elif choice==5:
            detailed_results()

        elif choice==6:
            view_statistics()

        elif choice==7:
            print("ADMIN LOGGED OUT")
            break
        else:
            print("Invalid Choice")

#-----------------------

# STUDENT MENU

#-----------------------

def student_menu(name,roll_number):
    while True:
        print(" ---STUDENT MENU--- ")

        print("1. View Rules ")
        print("2. Start Exam ")
        print("3. Logout")

        choice=int(input("Enter your choice: "))

        if choice==1:
            show_rules()

        elif choice==2:
            start_exam(name ,roll_number)

        elif choice==3:
            print("Student Logged Out")
            break

        else:
            print("Invalid Choice")

#-----------------------

# VIEW RULES

#-----------------------

def show_rules():

    print("-------EXAM RULES-------")

    print("1. Correct Answer = +4 Marks")
    print("2. Wrong Answer = -1 Marks")
    print("3. Skip = 0 Marks")
    print("4. Type S to Skip")
    print("5. Type SUBMIT to End Exam")

#------------------------

# VIEW QUESTIONS

#------------------------

def view_question():

        if len(questions)==0:
            print("No Questions Available")

        print("--------QUESTION BANK--------")

        number =1
        for q in questions:
            print("Question Number: ", number)
            print("Subject:",q["subject"])

            print(q["question"])

            print("A.",q["A"])
            print("B.",q["B"])
            print("C.",q["C"])
            print("D.",q["D"])

            print("Correct Answer: ",q["correct"])

            number +=1

#------------------------

# ADD QUESTION

#------------------------

def add_question():

        print("--------ADD QUESTION --------")

        subject=input("Enter your subject: ")
        question=input("Enter your question: ")

        option_a=input("Enter your option A: ")
        option_b=input("Enter your option B: ")
        option_c=input("Enter your option C: ")
        option_d=input("Enter your option D: ")

        while True:

            correct=input("Enter your correct answer (A/B/C/D):").upper()

            if correct in ["A","B","C","D"]:
                break

            else:
                print("Invalid Choice")

        new_question={
            "subject":subject,
            "question":question,
            "A":option_a,
            "B":option_b,
            "C":option_c,
            "D":option_d,
            "correct":correct
        }

        questions.append(new_question)

        print("Question Added")

#-------------------------

# DELETE QUESTION

#-------------------------

def delete_question():
    if len(questions)==0:
        print("No Questions Available")
        return

    print("--------DELETE QUESTION --------")

    for i in range(len(questions)):

        print(i+1,".",questions[i]["question"])

    number=int(input("Enter question number to delete: "))

    if number >=1 and number <=len(questions):

        questions.pop(number-1)

        print("Question Deleted")

    else:
        print("Invalid Choice")

#--------------------

# START EXAM

#--------------------

def start_exam(name,roll_number):

    if len(questions)==0:

        print("No Questions Available")
        return

    print("-------- EXAM STARTED --------")

    score=0

    answers_review=[]

    question_number=1

    for q in questions:
        print("Question Number: ", question_number)
        print("Subject:",q["subject"])
        print("Question:",q["question"])

        print("A.",q["A"])
        print("B.",q["B"])
        print("C.",q["C"])
        print("D.",q["D"])

        while True:

            answer=input("Enter your answer(A/B/C/D/S/SUBMIT):").upper()

            if answer in ["A","B","C","D","S","SUBMIT"]:
                break
            else:
                print("Invalid input")

        if answer=="SUBMIT":
            print("EXAM SUBMITTED")
            break

        elif answer=="S":
            status="Skipped"
            marks=0

        elif answer==q["correct"]:
            score+=4
            status="Correct"
            marks=4

        else:
            score-=1
            status="Wrong Answer"
            marks=-1

        review={
            "question":q["question"],
            "student_answer":answer,
            "correct_answer":q["correct"],
            "status":status,
            "marks":marks,

        }

        answers_review.append(review)

        question_number+=1

    total_marks=len(questions)*4
    percentage=(score/total_marks)*100

    if percentage>=90:
        grade="A"
    elif percentage>=80:
        grade="B"
    elif percentage>=70:
        grade="C"
    elif percentage>=60:
        grade="D"
    elif percentage>=50:
        grade="E"
    else:
        grade="F"

    result={
        "name":name,
        "roll_number":roll_number,
        "score":score,
        "percentage":percentage,
        "grade":grade,
        "answers":answers_review
    }

    results.append(result)

    print("========= FINAL RESULT ==========")

    print("Name:",name)
    print("Roll Number:",roll_number)
    print("Score:",score)
    print("Percentage:",percentage)
    print("Grade:",grade)

#----------------------

# VIEW RESULTS

#----------------------

def view_results():

    if len(results)==0:
        print("No Results Available")
        return

    print("==========  ALL RESULTS ==========")

    for r in results:
        print("Name:",r["name"])
        print("Roll Number:",r["roll_number"])
        print("Score:",r["score"])
        print("Percentage:",r["percentage"])
        print("Grade:",r["grade"])

#--------------------------

# DETAILED RESULTS

#--------------------------

def detailed_results():

    if len(results)==0:

        print("No Results Available")
        return

    print("==========  DETAILED RESULTS ==========")

    for i in range(len(results)):

        print(i+1,".",results[i]["name"])

    number=int(input("Enter student number:"))

    if number>=1 and number<=len(results):

        student=results[number-1]

        print("Name:",student["name"])
        print("Roll Number:",student["roll_number"])

        for ans in student["answers"]:

            print("Question:",ans["question"])

            print("Student Answer:",ans["student_answer"])

            print("Correct Answer:",ans["correct_answer"])

            print("Status:",ans["status"])

            print("Marks:",ans["marks"])

    else:
        print("Invalid Number")

#--------------------

# STATISTICS

#--------------------

def view_statistics():

    if len(results)==0:
        print("No Results Available")
        return

    scores=[ ]

    pass_students = 0
    fail_students = 0

    for r in results:

        scores.append(r["score"])

    highest=max(scores)
    lowest=min(scores)

    average=sum(scores)/len(scores)

    if r["grade"]=="F":
        fail_students+=1
    else:
        pass_students+=1

    grade_a=0
    grade_b=0
    grade_c=0
    grade_d=0
    grade_e=0
    grade_f=0

    for r in results:

        if r["grade"]=="A":
            grade_a+=1
        elif r["grade"]=="B":
            grade_b+=1
        elif r["grade"]=="C":
            grade_c+=1
        elif r["grade"]=="D":
            grade_d+=1
        elif r["grade"]=="E":
            grade_e+=1
        else:
            grade_f+=1

    print("======= CLASS STATISTICS =======")

    print("Highest Score:",highest)
    print("Lowest Score:",lowest)
    print("Average Score:",average)

    print("Pass Students:",pass_students)
    print("Fail Students:",fail_students)

    print("====== GRADE DISTRIBUTION ======")

    print("Grade A:",grade_a)
    print("Grade B:",grade_b)
    print("Grade C:",grade_c)
    print("Grade D:",grade_d)
    print("Grade E:",grade_e)
    print("Grade F:",grade_f)

#========================================================================

# PROGRAM START

#========================================================================
main_menu()