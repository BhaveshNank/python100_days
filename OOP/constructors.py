'''constructor is a unique function that gets called automatically
when an object is created of a class'''

class Person:

    def __init__(self, name, occ):
        print("Hey I am a person")
        self.name = name 
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")
        

a = Person('Bhavesh', 'Developer')
a.info()
b = Person('Divya', 'HR')
b.info()

