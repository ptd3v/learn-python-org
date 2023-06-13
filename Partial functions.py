#This is a summary of content and completed test exercise from learnpython.org

#Partial functions
from functools import partial

#Multiplicaton Example
from functools import partial

def multiply(x, y):
        return x * y

#Create a new function that multiplies by 2
dbl = partial(multiply, 4)
print(dbl(4))

#Code Completed
from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7)
print(p(8))