from typing import Any


class Employee:

    def __init__(self, name):
        self.name = name 

    def __len__(self):
        i = 0 
        for char in self.name:
            i += 1
        return i  

    def __str__(self):
        return f"The name of the employee is {self.name}"
    
    def __repr__(self):
        return f"Employee('{self.name}')"
    
    def __call__(self):
        print("Hey I am good")

    
e1 = Employee('Harry')
print(len(e1))
# print(e1.__len__()) # the above is the same as this one 

# if you run this function without __str__ method above it will return the address like this <__main__.Employee object at 0x102896ba0>
# but if you run this with the magic method __str__ it will return what is inside the str function, i.e The name of ....
print(e1) 
e1()
print()

print(str(e1))
print(repr(e1))