#user input
#username = input("Enter username:")
#print("Username is: " + #username)

# Initialize an empty list
list1 = []
#Accept user input to create a list of integers
for list1 in range(5):
    try:
        num = int(input("Enter an integer: "))
        list1.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Compute the sum of all integers in the list
# Print the list and its sum

#simple program for adding two numbers
a=10.1
b=20
a=float(input("a:"))
b=float(input("b:"))
sum=(a+ b)
print("sum: "+ str(sum))

#simple program for adding two lists
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a=int(input("a:"))
b=int(input("b:"))
sum=(a + b)
print("sum: "+ int(sum))

#list of comprehension
numbers=[number*number for number in range(1,6)]
print(numbers) #1,4,9,16,25

numbers=[number+number for number in range(1,6)]
print(numbers) #2,4,6,8,10


#nums=[1,2,3,4,5,6]
#results=[i*2 for i in nums]
#print("results!!",results)
strings = []
strings=["good","nice","love","band"]
results=[i.lower()+"y" for i in strings]
print("results!!", results) #goody, nicey,lovey, bandy


a=[1,2,4,6,8,10]
n=int(input("sum of integers="))
for i in range(n):
  sum=0
for i in list :
  sum=a+i
print("a:",sum)


a=[1,2,4,6,8,10]
n=int(input("number of elements="))
for i in range(n):
  a.append(int(input("value=")))
print("sum of LIST is:",sum)
for i in a:
  print(i)

