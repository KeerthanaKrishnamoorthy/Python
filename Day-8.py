#Dictionaries
dict = {
    "name" : "Keerthana",
    "last_name" : "Krishnamoorthy",
     "age" : 22,
    "skills" : ["pyhton","html","css","java"],
    "nationality" : "indian"
}
print(len(dict))
print(dict)
print(dict["skills"])
print(type(dict))
x = dict.keys()
dict["marital status"] = "Single"
print(x)
y = dict.values()
print(y)
z = dict.items()
print(z)
if "skills" in dict:
    print("yes")
dict.update({"age" : 25})
print(dict)
dict["name"] = "KEEERTHANA"
print(dict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("year")#pop specified item in dict
print(thisdict)
thisdict.popitem() #pop last item
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#looping in dict
for x in thisdict:
    print(x)
for x in thisdict.keys():
    print(x)
    for x in thisdict.values():
        print(x)
        for x,y in thisdict.items() :
            print(x,y)
z = thisdict.copy()
print(z)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#nested dict
myfamily = {
  "child1" : {
    "name" : "Emma",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tom",
    "year" : 2007
  },
  "child3" : {
    "name" : "Lilly",
    "year" : 2011
  }
}

print(myfamily)

