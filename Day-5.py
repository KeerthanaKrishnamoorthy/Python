#List: is a collection which is ordered and changeable(modifiable). Allows duplicate members
list = list()
print(list)
print(len(list))

fruits_list = ["apple","orange","banana","kiwi","mango"]
veg_list = ["brinjal","carrot","potato","tomato","drumstick"]
print(fruits_list)
print(len(fruits_list))
print(veg_list)
print(len(veg_list))
print(fruits_list[0:3])
print(veg_list[-1])
print(fruits_list[:3])
print(veg_list[0:])
fruits_list[1] = "papaya"
print(fruits_list)
fruits_list[1:3] = ["strawberry"]
print(fruits_list)
veg_list.insert(2,"mangoos")
print(veg_list)
veg_list.append("oil")
print(veg_list)
fruits_list.insert(1,"goose")
print(fruits_list)
fruits_list.remove("apple")
print(fruits_list)
del veg_list[0:2]
print(veg_list)
thislist = ["apple", "banana", "cherry"]
del thislist
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
a = ["apple","cat","dog","ball","monkey","mom","dad"]
first,second,third,*rest = a
print(first)
print(second)
print(third)
print(rest)
print(a[::2]) #leave every second element in the list
print(a[::-1])#-ve indicates the reverse order
item_in_the_list = "dog" in a
print(item_in_the_list)
itm_in_list = "money" in a
print(itm_in_list)
a.pop()
print(a)
a.pop(2)
print(a)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )
print(fruits.count("lemon"))
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)


num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print(num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print(negative_numbers)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["name","age","height","marital status","address"]
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Faceboob","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(mixed_data_types)
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[1:6])
print(it_companies[-1])
it_companies[1] = "HCL"
print(it_companies)
it_companies.append("IT")
print(it_companies)
it_companies.insert(3,"IT")
print(it_companies)
string = "#".join(it_companies)
print(string)
it_companies.sort()
print(it_companies)
