class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
e1 = Employee("Bhavesh", "1200")
print(e1.name)
print(e1.salary)

# for employee 2 parse the below string into the object instance
string = ("John-2000")

e2 = Employee(string.split("-")[0], string.split("-")[1]) # but instead of doing this we can create a method with class name
print(e2.name)
print(e2.salary)
e3 = Employee.fromStr(string)
print(e3.name)
print(e3.salary)
