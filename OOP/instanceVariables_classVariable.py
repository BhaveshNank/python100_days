class Employee:
    companyName = 'Apple' # class variable
    noOfEmployee = 0

    def __init__(self, name):
        self.name = name    # instance variable
        self.raise_amount = 0.02  
        Employee.noOfEmployee += 1

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Bhavesh")
emp2 = Employee("Rohan")

emp1.showDetails() # you can either use this OR 
emp1.raise_amount = 0.3 # this changes the value stored in the instance variable raise amount
Employee.showDetails(emp1) # you can use this 
print(emp1.raise_amount)

print(emp1.companyName) # prints the company name that is associated with the class

emp1.companyName = 'Apple India' # assuming this employee works in Apple India we will set the company name to Apple India
print(emp1.companyName) # this changes the company name of emp1 employee to Apple India because we choose to change it
print(emp2.companyName) #however since we did not change for emp2 employee it returns the company name that is available in the class variable


print("The below lines of code changes the class variable company name but not the instance variable company name is there is one")
Employee.companyName = 'Apple International'
print(emp1.companyName) # this changes the company name of emp1 employee to Apple India because we choose to change it
print(emp2.companyName) 

# emp3 = Employee('Rahul')
# emp3.showDetails()