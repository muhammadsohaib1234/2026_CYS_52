# TASK 5

try:
    num = int(input("Number: "))
    data = [1, 2, 3]
    print(data[num])
except ValueError:
    print("Number hi likhna tha")
except IndexError:
    print("List mein itne item nahi hain")
