# TASK 3

to_upper = lambda s: s.upper()

def invert(text):
    print("Reversed Uppercase String:", text[::-1])


text = input("Enter a string: ")
upper_text = to_upper(text)
print("Uppercase:", upper_text)
invert(upper_text)
