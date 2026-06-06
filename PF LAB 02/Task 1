# TASK 1
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

def permutation(n, r):
    return factorial(n) // factorial(n - r)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


print("=== Permutation and Combination Calculator ===\n")

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

if r > n or n < 0 or r < 0:
    print("Error: r cannot be greater than n or negative values not allowed!")
else:
    print(f"\nPermutation P({n}, {r}) = {permutation(n, r)}")
    print(f"Combination C({n}, {r}) = {combination(n, r)}")
