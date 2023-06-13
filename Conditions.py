#This is a summary of content and completed test exercise from learnpython.org

#Conditions
x = 2
print(x == 2) #Prints out True
print(x == 3) #Prints out False
print(x < 3) #Prints out True

#Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
    print("Your name is either John or Rick.")

#The 'in' operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    #Do something
    pass
elif another_statement is True: # else if
    #Do something else
    pass
else:
    #Do another thing
    pass

statement = False
another_statement = True
if statement is True:
    print("do something")
    pass
elif another_statement is True: #Else if
    print("do something else")
    pass
else:
    print("do another thing")
    pass

x = 1
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

#The 'is' operator
x = [1,2,3]
y = [1,2,3]
print(x == y) #Prints out True
print(x is y) #Prints out False

#The 'not' operator
print(not False) #Prints out True
print((not False) == (False)) #Prints out False

#Exercise
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")