#This is a summary of content and completed test exercise from learnpython.org

#Decorators
def functions(arg):
    return "value"

#Works the same as
def function(arg):
    return "value"
function = decorator(function)
#This passes the function to the decorator, and reassigns it to the functions

#We have to return the new_function, or it wouldn't reassign it to the value
def repeater(old_function):
    def new_function(*args, **kwds):
        old_function(*args, **kwds) #We run the old function
        old_function(*args, **kwds) #We do it twice
    return new_function

#This makes a function run twice
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 3)
6
6

#You can also make it change the output
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) #Modify the return value
    return new_function

#And even the input
def double_Ii(old_function):
    def new_function(arg): #Only works if the old function has one argument
        return old_function(arg * 2) #Modify the argument passed
    return new_function

#Check the function
def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument") #This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function

def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

#Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

#Now return_num is decorated and reassigned into itself
return_num(5) # should return 15

#Code Completed
def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])