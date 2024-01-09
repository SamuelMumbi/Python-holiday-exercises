courses = ["History", "Math", "Physics", "Computer", "Business"]
#courses.append("Business") add
courses.remove("History")
print(courses)

Fruits = ["apple", "banana", "cherry"]
Fruits.append("orange")
print(Fruits) #add orange

Fruits = ["apple", "banana", "cherry","mangoes","oranges","melons"]
Fruits.append("Grapes") #add 
print(Fruits) 

Thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(Thislist) #duplicate items in the list

Thislist = ["apple", "banana", "cherry"]
print(len(Thislist)) #length 3

Thislist = ["apple", "banana", "cherry"] #strings
print(len("apple")) #length of an apple in the list 5
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #list type 'str'

list2 = [1, 5, 7, 9, 3]  #intengers
print(list2)
list3 = [True, False, False] #boolean
print(list3)

list4 = ["abc", 34, True, 40, "male"] #complex
print(list4)


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5]) #range

Fruits = ["apple", "banana", "cherry"]
Fruits.append("orange")
print(Fruits) #add 

Fruits = ["apple", "banana", "cherry"]
Fruits.remove("apple")
print(Fruits) #remove  

Fruits = ["apple", "banana", "cherry"]
Fruits[1] = "Grapes"#change bananas to grapes
print(Fruits)

Fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(Fruits[:4]) #return except Kiwi


fruits = ["apple", "banana", "cherry"] #counts from the start
print(fruits[0])
fruits = ["apple", "banana", "cherry"] #position
print(fruits[1])
fruits = ["apple", "banana", "cherry"] #counts from the start
print(fruits[2])
fruits = ["apple", "banana", "cherry"] #counts from last
print(fruits[-1])
fruits = ["apple", "banana", "cherry"] #counts from second last
print(fruits[-2])
print(len(fruits))


#red_bucket= input("What is inside?")  variable
#print(red_bucket)
