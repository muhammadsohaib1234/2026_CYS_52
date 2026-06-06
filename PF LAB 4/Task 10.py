# TASK 10

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
choice = int(input("Enter your choice: "))
if choice == 1:
    print((add(num1,num2)))
elif choice == 2:
    print((sub(num1,num2)))
elif choice == 3:
    print((mul(num1,num2)))
elif choice == 4:
    print((div(num1,num2)))
else:
    print("Invalid choice")
