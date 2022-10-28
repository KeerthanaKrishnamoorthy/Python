#Conditionals
#IF condition
a = 200
b = 30
if a < b:
    print("a is less than b")
else:
    print("b is less than a")

#elif condition
a = 50
b = 50
if a < b :
    print("a is greater")
elif a == b:
    print("both are equal")

#else condition
#we can use else condition without using elif
a = 25
b = 30
if a > b:
    print("a is greater")
else:
    print("b is greater")

a = 22
b = 0
if a < b:
    print("b is big")
elif a == b:
    print("both")
else:
    print("a is greater")

#short hand-if
a = 200
b = 33
if a > b : print("a is greater")
#short hand else
print("b") if b < a else print("a")

#using logical operators AND , OR
a = 200
b = 300
c = 20
if a>c and b>c:
    print("True")
if a>c or a<b:
    print("atleast one condition is true")

#nested if
a = 200
if a > 20 :
    print("yes greater than 20")
    if a < 300:
        print("ofcourse")
    else:
        print("nothing")

#pass is used for no error
a = 9
b = 8
if a > b:
    pass

a = int(input("Enter your age"))
if a == 18:
    print("your allowed to drive")
elif a < 18:
    print("wait for some more years to reach 18")

my_age = int(input("my age"))
your_age = int(input("your age"))
if my_age > your_age :
    print("you are younger than me")
elif my_age < your_age:
    print("you are older tha me")
else:
    print("Nothing")

scores = int(input("Enter your score: "))
if scores >= 90 and scores <= 100:
    print('A')
elif scores >= 80 and scores <= 89:
    print('B')
elif scores >= 70 and scores <= 79:
    print('C')
elif scores >= 60 and scores <= 69:
    print('D')
elif scores >= 50 and scores <= 59:
    print('E')
else:
    print('F')


month = str(input("Enter a month : "))
if month in ("september","october","november"):
    print("Autumn")
elif month in ("December", "January" ," February"):
    print("winter")
elif month in ("march","april","may"):
    print("spring")
elif month in ("june","july","august"):
    print("summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
if 'mango' in fruits:
    print("fruit exist in the list")