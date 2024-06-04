class Employee:
    def __init__(self, name, id): 
        self.name = name 
        self.id = id 
        
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang 
    
rohan = Employee("Rohan Das", 4200)
harry = Programmer("Harry Khan", 2345, "Python")

print(harry.name)
print(harry.id)
print(harry.lang)
