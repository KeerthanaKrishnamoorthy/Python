#variables in python
first_name = "keerthana"
last_name = "krishna"
age = 23
country = "India"
state = "Tamilnadu"
skills = ["html" , "css" , "python"]
personal_information = {
                          "name":"keerthana",
                          "age":23,
                          "country":"india"
                       }
is_married = True
print(first_name)
print("first_name:",len(first_name))
print(last_name)
print("last_name:",len(last_name))
print(age)
print(country)
print(state)
print(skills)
print("personal_information:",personal_information)
print(len(personal_information))
print(is_married)

#casting in python
#int to float
a = 52
print(float(a))
#float to int
b = 52.6
print(int(b))
#int to str
c = 10
print(str(c))
#str to int or float
str = 25
print(int(str))
print(float(str))
#str to list
str = "keerthana"
print(list(str))

#multiple variable in one line
name , age ,country , gender , phone = "keerthana" , 23 , "india" , "female" , 6345924
print(name , age ,country , gender , phone)


#practice
a1 = 5
a2 = 4
total = a1 + a2
print(total)
a = 40
b = 2
print(a%b)
print(a//b)
print(a**b)

a = input("enter your name")
b = input("enter your country")
c = input("enter your age")
print("name : ",a)
print("country:",b)
print("age:",c)