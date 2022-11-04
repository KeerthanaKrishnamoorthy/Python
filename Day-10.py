#Loops

#while loop
i = 3
while i < 10:
    print(i)
    i += 1

count = 0
while count < 10:
    print(count)
    count += 1
else:
    print(count)

x = 0
while x < 100:
    print(x)
    x += 1
else:
    print(x)

y = "apple"
while y != "apple":
    print(y)
    y += 1
else:
    print("nothing")

y = 1
while y < 20:
    y += 1
    if y == 10:
        continue
    print(y)

#for loop
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

x = "keerthana"
for i in x:
    print(i)

fruits = ("apple","banana","cherry","blums")
for x in fruits:
    print(x)

#break statement
fruits = ("apple","banana","cherry","blums")
for i in fruits:
   if i == "cherry":
       break
   print(i)

fruits = ("apple", "banana", "cherry", "blums")
for i in fruits:
    print(i)
    if i == "cherry":
        break
    print(i)

#continue statement
name = ("jack","jill","jim","kim")
for x in name:
    if x == "jim":
        continue
    print(x)


person = {
    "name" : "Keerthana",
    "age" : 22,
    "country" : "India",
    "state" : "Tamilnadu",
    "ismarried" : "no",
    "address" : {
    "street" : "taj hotel",
    "postal_pin" : "62005"
}
}
for key in person:
    print(key)
for key,value in person.items():
    print(key,value)

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

numbers = [1,2,3,5,6,8]
for x in numbers:
    print(x)
    if x == 3:
       break

num = [1,2,3,4,5,6,7,8,9]
for i in num:
    if i == 5:
       continue
    print(i)

for x in range(11):
    print(x)
else:
    print("the loop will at",x)

for y in range(11):
    print(y)

#patterns
n = 8
for i in range(n):
    for j in range(n):
     print("#",end="")
    print()

#* pattern
m = 7
for i in range(7):
    for j in range(i):
        print("*",end="")
    print()

#reverse * pattern
m = 7
for i in range(7):
    for j in range(m-1-i):
        print("*",end="")
    print()

#number pattern
a = 5
for i in range(1, a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

