
def school_age_calculator( age, name ):
  if age < 5:
    print("Enjoy the time!",name, "is only",age)
  elif age ==5:
    print("Grade1,",name)
  else:
    print("They are genius!")
school_age_calculator( 3, "Thomas" )