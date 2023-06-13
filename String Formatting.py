#This is a summary of content and completed test exercise from learnpython.org

#String Formatting
#Prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

#Prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

#Exercise Solution
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)