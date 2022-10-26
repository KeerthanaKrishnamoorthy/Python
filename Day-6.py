#Tuples
Tuple = ("amir","john","jack","jill")
print(len(Tuple))
print(Tuple)
print(len(Tuple)-1)
print(Tuple[2])
if "jill" in Tuple:
    print("Yes")
else:
    print("No")
print(Tuple[-1])
print(Tuple[-3:-1])
print(Tuple[2:])
print(Tuple[:3])
#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
x = ("apple","bat"," cat","dog")
y = list(x)
y[1] = "banana"
y.append("lion")
x = tuple(y)
print(y)

sisters = ("amm","jmm","lily")
brothers = ("joh","mamm","kim")
family_members = ("father","mother")
siblings = sisters + brothers
print(siblings)
print(len(siblings))
print(siblings)
for family_members in siblings:
    print(family_members)
thistuple = (1,1,2,8,6,8,3,6,4,7,5)
x = thistuple.count(8)
y = thistuple.index(6)
print(x)
print(y)

