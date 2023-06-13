#This is a summary of content and completed test exercise from learnpython.org

#Closures
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    data_transmitter()

print(transmit_to_space("Test message"))

#Nonlocal keyword (Result 3, 3)
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)

#Nonlocal keyword (Result 3, 9)
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
#Removed the Nonlocal
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)

#Return Nested Function
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter

#Calling the Function
def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()

#Code Completed
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))