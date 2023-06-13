#This is a summary of content and completed test exercise from learnpython.org

#Lambda Functions
def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)

#Function Summary
your_function_name = lambda inputs : output

#Code Completed
l = [2,4,7,3,14,19]
for i in l:
    # your code here
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))