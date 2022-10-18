#Variables are containers for storing data values
x = 5
y = "john"
print(x)
print(y)

#Python has no command for declaring a variable.
x = 50
y = 30.5
z = 25j
print(type(x))
print(type(y))
print(type(z))

#Variable names are case-sensitive
a = 50
A = "john"
print(a,A)

#variable names are same means it will take the last value
a = 5
a = 4
print(a)

#variable names does not start with a number ,it should be in underscore , alphates and number can be used in center but not in first
myvariable = 20
MYVARIABLE = 50
My_variable = "tree"
my2variable = 400
print(myvariable)
print(MYVARIABLE)
print(My_variable)
print(my2variable)

#Python allows you to assign values to multiple variables in one line
(x , y , z) = ("apple","orange","cat")
print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line
x = y = z = "goodbye"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
items = ("apple","orange","cat")
(x, y, z) = items
print(x)
print(y)
print(z)

#In the print() function, you output multiple variables, separated by a comma:
x = "python"
y = "is"
z = "awesome"
print(x,y,z)

x = "python"
y = "is"
z = "awesome"
print(x + y + z)

#For numbers, the + character works as a mathematical operator
x = 50
y = 50
print(x + y)

#we cannot add a number and a str in python
#but The best way to output multiple variables in the print() function is to
# separate them with commas, which even support different data types
x = 50
y = 50
print(x , y)

#Global variable
x = "water"
def myfunc():
    print("cold",x)
myfunc()

#also;
x = "water"#global variable
def myfunc():
    x = "icecream"#local variable
    print("cold",x)
myfunc()
print("im in",x)

#to use global inside use global() keyword
x = "water"#global variable
def myfunc():
    global x
    x = "icecream"#local variable

myfunc()
print("im in",x)



#string
first_name = "keerthana"
last_name = "krishnamoorthy"
space = " "
full_name = first_name + space + last_name
print(first_name + space + last_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) < len(last_name))
print(full_name)

#Escape Sequences in Strings
sentence = "I hope everyone gets irritated when starting any language.\nis it right?"
print(sentence)
using_tab = "days\ttopic\texercise"
print(using_tab)
print("day 1\t\t3\t\t8")
print("day 2\t\t3\t\t8")
print("day 3\t\t3\t\t8")
print("day 4\t\t3\t\t8")
print("day 5\t\t3\t\t8")
print("to use a single quotes in a double quotes\'hello pikachu\'")
print('to use double quotes in a single quotes \"hello jinglee\"')

#formating string %s
first_name = "keerthana"
last_name = "krishnamoorthy"
intrest = "python"
format = ("I am {} {}. I am intrested in {}".format(first_name,last_name,intrest))
print(format)


int = 5   #%d
float = 6  #%f
num_str_format = ("I am going to add %d and %f"%(int,float))
print(num_str_format)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.3f.' %(radius, area) # 3 refers the 3 decimal point after float
print(formated_string)

#new string format
a = 6
b = 4
print('{} + {} = {} '.format(a,b,a+b))
print('{} - {} = {} '.format(a,b,a-b))
print('{} * {} = {} '.format(a,b,a*b))
print('{} / {} = {} '.format(a,b,a/b))
print('{} // {} = {} '.format(a,b,a//b))
print('{} ** {} = {} '.format(a,b,a**b))
# innew str :.2f indicates the 2 decimal value after the output
radius = 20
pi = 3.14
area = 25
area_of_circle = pi * radius ** 2
print("the area of a circle ,radius is {} and area is {:.2f}".format(radius,area))

#String Interpolation / f-Strings
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a**b}')

string = "PYTHON"
print(string[0])
#Reversing a String
a = "keerthanakrishnamoorthy"
print(a[::-1])
#various methods in string
a = "i feel hungry everytime"
print(a.capitalize())
print(a.count("e"))
print(a.endswith("me"))
print(a.endswith("mes"))
print(a.find("r"))

a = "everthing is temporary in our lives"
b = "nothingispermanent"
c = "IM30YEARSOLD"
print(a.islower())
print(a.isalpha())
print(b.isalpha())
print(c.isalnum())
print(a.upper())
print(b.upper())
print(c.lower())

A = "CODING"
B = "FOR"
C = "ALL"
space = " "
D = A+space+B+space+C
print(D)
company = "coding for all"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.strip("coding"))
print(company.find("ing"))
print(company.replace("coding","goding"))
print(company.index("l"))
print(company.rindex("c"))
print(company[6:-1])
a = "   coding  is  nothing  "
print(a.strip())
b = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join = "#".join(b)
print(join)
sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)

det = "name\tage\t\tcountry"
print(det)
print("keerthana\t20\tindia")

