# functions
# syntax
#  def function_name():
#      code
#  calling a function
#  function_name()

def my_function():
    x = 5
    y = 10
    print(x*y)
my_function()

#using arguments
def func(fname):
    print(fname + "musk")
func("andra")
func("john")

def my_funct(fname,lastname):
    print(fname + " " + lastname)
my_funct("aman","vinky")

def argu(*kids):
    print("The youngest child is "+ kids[2])
argu("emma","lilly","john")

def my_argu(child1,child2,child3):
    print("The elder child is " + child2)
my_argu(child1 = "lara" , child2= "emma" , child3= "lilly")

def check(num):
    if num == 0:
        print("Either Positive or Negative")
    elif num < 0:
        print("Negative")
    else:
        print("Positive")
num = int(input("Enter a number"))
check(num)

def display(day,month,year):
    print("Day : " +str(day))
    print("month : " +str(month))
    print("year : " +str(year))

display(1,12,2000)

def display(day,month,year=2020):
    print("Day : " + str(day))
    print("month : " + str(month))
    print("year : " + str(year))

display(1, 12, 2000)

#arbitary function
def sum(*input):
    ans = 0
    for d in input:
        ans += d
        print("sum : ", ans)

sum(10,20)
sum(10,30,80)

#return statement
def fun():
    return 10
a = fun()
print(a)

def empty(x,y):
    return x == y
flag = empty(10,20)
print(flag)
flag = empty(2,2)
print(flag)

def value(a,b):
    return a+b
ans = value(5,90)
print(ans)
