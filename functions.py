#print function, syntax and Indentation in python
print("hello world")

if 5 == 4:
  print("This is new Math!")#false
if 5!=4 :
  print("Alright!")#true


def print_samuel():
  text="mumbi"
  print(text)
  print(text)
  print(text)
print_samuel()

def print_samuel(text):
  print(text)
  print(text)
  print(text)
print_samuel("Samuel the Genius guy")

def school_age_calculator( age, name ):
  if age < 5:
    print("Enjoy the time!", name, "is only", age )
  elif age ==5:
    print("Grade1,", name )
  else:
    print("They are genius!")
school_age_calculator( 10, "Thomas" )

def school_age_calculator( age, name ):
  if age < 5:
    print("Enjoy the time!", name, "is only", age )
  elif age ==5:
    print("Grade1,", name )
  else:
    print("They are genius!")
school_age_calculator( 5, "Thomas" )

def school_age_calculator( age, name ):
  if age < 5:
    print("Enjoy the time!",name, "is only",age)
  elif age ==5:
    print("Grade1,",name)
  else:
    print("They are genius!")
school_age_calculator( 3, "Thomas" )

x = 5      # x is of type int
y = "John" # y is now of type str
print(x)
print(y)