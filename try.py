class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def getname(cls, name):
        cls.name = name
        print(f"The name is {cls.name}")

e1 = Employee("bhavesh", 1200)
e1.getname('bhavesh')
Employee.getname("Bhavesh")