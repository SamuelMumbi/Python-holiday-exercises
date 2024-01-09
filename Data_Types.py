#data_types in python
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.
       #EXAMPLES
#tupple unchageable(cant remove or add items),unordered,
tuple = ("apple", "banana", "cherry")
print(tuple) #Tuples are written with round brackets.The first item has index [0], the second item has index [1] etc.
tuple1 = ("apple", "banana", "cherry") #string
tuple2 = (1, 5, 7, 9, 3) #intenger
tuple3 = (True, False, False) #boolean

#list
mylist = ["apple", "banana", "cherry"] #Lists are created using square brackets:The first item has index [0], the second item has index [1] etc.

#set
myset = {"apple", "banana", "cherry"} # Set items are unordered, unchangeable, and do not allow duplicate values.Note: Set items are unchangeable, but you can remove items and add new items.True and 1 is considered the same value:Sets are written with curly brackets.
myset2 = {"apple", "banana", "cherry", True, 1, 2}
print(myset2)

#dictionary(dict)
#Dictionaries have keys and values and are written with curly brackets.
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict["brand"])

mydict2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(mydict2["colors"])


