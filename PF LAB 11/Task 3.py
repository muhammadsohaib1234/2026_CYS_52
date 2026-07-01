students = (
    ("Ali", 85, 90, 78),
    ("Ahmed", 70, 88, 92),
    ("Sara", 95, 91, 89)
)

for name, m1, m2, m3 in students:
    avg = (m1+m2+m3)/3
    print(name, "Average:", avg)
