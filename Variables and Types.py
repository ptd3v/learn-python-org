#This is a summary of content and completed test exercise from learnpython.org

#Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals)
#Variable and Types
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

#The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)
mystring = "Don't worry about apostrophes"
print(mystring)

#Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#Assignments can be done on more than one variable "simultaneously"
a, b = 3, 4
print(a, b)

#Exercise solution
mystring = "hello"
myfloat = 10.0
myint = 20

#Testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)