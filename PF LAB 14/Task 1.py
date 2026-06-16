# TASK 1

def welcome():
    global x
    x = 10
    print(x)
welcome()


def a():
    x = 25
    print(x)
    print(globals()["x"])
a()
