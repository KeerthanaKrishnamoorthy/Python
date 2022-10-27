#Set
set = {"apple" , "orange" , "mango" , "beetroot"}
print(type(set))
print(len(set))
print(set)
for x in  set :
    print(x)
print("mango" in set)
set.add("Lion")
print(set)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)
thisset.remove("banana")
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

x = {"ball","cat","cow"}
y = {20,30,"cow"}
z = x.difference(y)
print(z)
y.discard("cow")
print(y)
x = {"ball","cat","cow"}
y = {20,30,"cow"}
z = x.union(y)
print(z)





