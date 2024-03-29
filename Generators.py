#This is a summary of content and completed test exercise from learnpython.org

#Generators
import random

def lottery():
    #Returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    #Returns 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

#Fibonacci
a = 1
b = 2
a, b = b, a
print(a, b)

#Exercise Solution
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break