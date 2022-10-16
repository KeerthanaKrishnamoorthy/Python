#Operators in python
#Arithmetic operators
print("add :",2+3)
print("sub:",3-5)
print("mul:",3*5)
print("div:",6/2)
print("mod:",2%3)
print("exp:",2**6)
print("floor div:",5//2)

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 3j) * (2 - 1j))
print('div complex numbers:',(1+3j) / (2-3j))

#declaring variable at the top
a = 20
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#to calculate mass , gravity , weight , area , volume
#area of a circle
radius = 6
area_of_circle = 3.14 * radius**2   #(pi*r**2)formulae
print("area of circle:",area_of_circle)

#calculate area of rectangle
l = 10
w = 6
area_of_rect = l * w
print("area of rect:",area_of_rect)

#calculate weight of an object
mass = 20
gravity = 9.81
weigth_of_an_object = mass * gravity
print("weight of an object :",weigth_of_an_object)

#calculate density of a liquid
mass = 70 #in kg
volume = 0.075 #in cubic meter
density = mass / volume
print(density)

#Comparison operator
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print(3>5)
print(5>10)
print(3==3)
print("mango"=="mango")
print(len("tree") == len("apple"))
print(len("pig") != len("lion"))
print(3!=5)
print(6==8)

#exercise
int = 20
float = 3.5
print(complex(int))
print(complex(float))

base = 20
height = 15
area_of_triangle = 0.5*base*height
print(area_of_triangle)

a = input("side a")
b = input("side b")
c = input("side c")
print("perimeter of triangle :", a+b+c)

#Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = 10
width = 20
area = length * width
print(area)
perimeter = 2 * (length + width)
print(perimeter)

#Get radius of a circle using prompt.
#Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
r = 10
area = 3.14*10**10
circumference = 2*3.14*10
print("area:",area)
print("circumference:",circumference)

#Check if int('9.8') is equal to 10
int = 9.8
if (9.8 == 10):
    print(True)
else:
    print(False)

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
a = 7//3
b = 2.7
print(a)
if (a == b):
    print("yes")
else:
    print("No")

#Find the length of the text python and convert the value to float and convert it to string
print(len("python"))
a = "python"
print(float(6))
print(str("python"))





