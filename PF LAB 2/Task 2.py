# TASK 2

larger = lambda a, b: a if a > b else b

def print_table(num, start, end):
    print(f"\nTable of {num} from {start} to {end}:")
    for i in range(start, end + 1):
        print(f"{num} x {i} = {num * i}")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

large_num = larger(a, b)
print(f"Larger number is: {large_num}")

start = int(input("Enter start of table range: "))
end = int(input("Enter end of table range: "))
print_table(large_num, start, end)
