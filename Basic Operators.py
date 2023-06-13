#This is a summary of content and completed test exercise from learnpython.org

#Arithmetic Operators
number = 1 + 2 * 3 / 4.0
print(number)

#Modulo - The remainder
remainder = 11 % 3
print(remainder)

#Power of
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#Using Operators with Strings
helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

#Using Operators with Lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

#Exercise
x = object()
y = object()

#Change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = [x] * 10 + [y] * 10

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

#Testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")