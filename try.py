class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee (name={self.name!r}, salary={self.salary!r}) str"
    
    def __repr__(self):
        return f"Employee (name={self.name!r}, salary={self.salary!r}) repr"
    
e1 = Employee("Bhavesh", 1200)
print(e1)