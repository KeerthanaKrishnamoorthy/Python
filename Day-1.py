#hello world
print("Hello,World")

#Data types
print(2+3)    #addition
print(2-1)    #subtraction
print(2*5)    #multiplication
print(10/2)   #division
print(10**2)  #exponential
print(2%6)    #modulus
print(5//6)   #floor division

# To check the data types
print(type(10))                                  #int
print(type(10.2))                                #float
print(type(10+4j))                               #complex
print(type("elonmusk"))                          #string
print(type([1,5,6]))                             #list
print(type({"name": "kiki", "age": 24}))         #dictionary
print(type(("apple",)))                          #tuple
print(type({52,"kiki",True}))                    #set

#Text Type:str
x = "Hello world"
print(x)
print(type(x))
#numeric type
#int,float,dict
x = int(50)
y = float(20.5)
z = complex(56j)
print(x)
print(y)
print(z)
#sequence type
#list,tuple,range
list = ["apple",20,True]
print(list)
tuple = ("orange",)
print(tuple)
print(type(tuple))
x = range(8)
print(x)
#mapping type
#dictionary
x = {"name" : "john",
     "age" : 28
     }
print(x)
#set types
#sets
x = {"apple" , "carrot" , "ball"}
print(x)
print(type(x))
#frozenset
x = frozenset({"apple" , "carrot" , "ball"})
print(x)
print(type(x))
#Boolean type
#boolean
x = ("apple","ball")
if "ball" in x:
    print(True)
else:
    print(False)
#Binary types
#bytes
x = b"hello"
print(x)
print(type(x))
#bytearray(5)
x = bytearray(6)
print(x)
print(type(x))
#memoryview(bytes(5))
x = memoryview(bytes(6))
print(x)
print(type(x))


