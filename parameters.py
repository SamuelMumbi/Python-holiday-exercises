#There are 5 parameters where four(4) are optional
#object - value(s) to be printed
#sep (optional) - allows us to separate multiple objects inside print().
#end (optional) - allows us to add add specific values like new line "\n", tab "\t"
#file (optional) - where the values are printed. It's default value is sys.stdout (screen)
#flush (optional) - boolean specifying if the output is flushed or buffered. Default: False

#Example1 
#In the above example, the print() statement only includes the object to be printed. Here, the value for end is not used. Hence, it takes the default value '\n'.
print('good morning')
print('it is rainy today')
#good morning
#it is rainy today

#Example2
#notice, we get the output in a single line separated by space.
print('good morning', end='')
print('it is rainy today')
#good morningit is rainy today

#Example3
#Notice, the output includes items not separated by commas
print('New year','2024','see you soon!', sep='')
#New year2024see you soon!

#Example4
#print literals
number = -10.6
name = "power Lp"
print(5)      #5
#print variables
print(number)  #-10.6
print(name)    #power Lp

#Example5
#Print Concatenated Strings
print('PowerLP is' + 'Awsome') # PowerLP isAwsome
#the + operator joins two strings 'PLP is ' and 'awesome.'
#the print() function prints the joined string

#Example6
#formating
x=5
y=10
print('The value of x is{} and y is{}'.format(x,y))
#The value of x is5 and y is10











