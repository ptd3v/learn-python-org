#This is a summary of content and completed test exercise from learnpython.org

#Lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) #Prints 1
print(mylist[1]) #Prints 2
print(mylist[2]) #Prints 3

#Prints out 1,2,3
for x in mylist:
    print(x)

#Exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

#Write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

#This code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)