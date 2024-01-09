#https://youtu.be/Z17sMiY_Cqg 
#Dictionaries Key and value, add value, change value, delete,
#Methods# .any, .all , .len, .sorted, .clear,.

my_dict = {"a":1,"b":2,"c":3}
results = my_dict["b"]
print(results)

my_dict = {"a":1,"b":2,"c":3}
results = my_dict["b"]
print(my_dict)

mydict3 = dict(name = "John", age = 36, country = "Norway")
print(mydict3)

#example
capital_city = {"Napel":"Kathmandu", "Italy":"Rome", "England":"London" } 
print(capital_city)
print(capital_city.keys())
print(capital_city.values())

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict["brand"])

#accessing items
x = mydict["model"]
#changing items
mydict["year"] = 2018
#adding items
mydict["color"] = "red"
print(mydict)
#removing items
mydict.pop("model")
print(mydict)
#deleting keys
print(mydict)
#Printing all items
for x in mydict:
  print(mydict[x])
#using Methods to return value
#for loop
for x in mydict.values():
  print(x)
for x in mydict.keys():
  print(x)
for x in mydict.copy():
  print(mydict)
  
  #example
x={}
x[2]=10
x[1]=[20,30,40]
print(x[1][2])  #40

mydict2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(mydict2["colors"])


#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Jane",
    "year" : 2004
  },
  "child2" : {
    "name" : "Janet",
    "year" : 2007
  },
  "child3" : {
    "name" : "Joy",
    "year" : 2011
  }
}
print(myfamily)

#example
capital_city = {"Napel":"Kathmandu", "Italy":"Rome", "England":"London" } 
print(capital_city)
print(capital_city.keys())
print(capital_city.values())

#can also be integers
capital_city = {"1":"Kathmandu", "2":"Rome", "3":"London" } 
print(capital_city)
print(capital_city.keys())
print(capital_city.values())

student_id={2000:"Sam",2001:"Samy",2002:"Samuel",2003:"Simon",2004:"Samson", }
print("initial dictionary:",student_id)
del student_id[2001]
print("updated dictionary:",student_id)

mydict3 = dict(input)(name = "", age = '', favourite_color = "")
for x in mydict3():
  print(x)
print(mydict3.keys())
print(mydict3.values())
print("initial dictionary:",mydict3)
mydict3["Name"] = "John"
mydict3["Age"] = 36
mydict3["favourite_color"] = "blue"
print("updated dictionary:",mydict3)

d={}  
size=int(input("Enter the size:"))
for i in range(size):
  Key=input("Enter your name:")
  value=input("Enter your name:")
  Key=input("Enter your Age:")
  value=input("Enter your age:")
  Key=input("Enter your favourite_color:")
  value=input("Enter your favourite_color:")
  d[Key]=value
print("The dictionary is")
print(d)






