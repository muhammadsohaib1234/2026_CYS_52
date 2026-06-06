#TASK 11
t1={"dgk","sohaib","uet"}
t2={"qaisrani","city school","uet"}
t3={"luqman","danish school","uet"}
t1.update(t2,t3)
t1.discard("uet")
print(t1)

#TASK 12
t1={"dgk","sohaib","uet"}
t2={"qaisrani","city school","uet","dgk"}
t1.difference_update(t2)
print(t1)

#TASK 13
t1={"dgk","sohaib","uet"}
t2={"qaisrani","city school","uet"}

t1.isdisjoint(t2)
print(t1)

# TASK 14
t1={1,2,3}
t2={4,5,6}
print(t1.issubset(t2))

#TASK 15
t1={4,5,6,3}
t2={1,2,3,4,5,6}
print(t1.issubset(t2))
