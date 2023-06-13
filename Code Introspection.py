#This is a summary of content and completed test exercise from learnpython.org

#Code Introspection
help()
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance() 
__doc__ 
__name__

#Code Completed
#Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

#Print a list of all attributes of the Vehicle class.
print(dir(Vehicle))