# Private variables

class Employee:
    def __init__(self):
        self.__name = "Bhavesh"

a = Employee()
# print(a.__name) # cannot be accessed directory
# print(a._Employee__name) #therefore we use the class name to access
# this indirectly 
print(a.__dir__())

'''There is no concept of private and protected in python it 
is just name mangling that happens -> see harry's video on access
modifies for more information'''