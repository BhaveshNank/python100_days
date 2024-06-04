# convention: class name should be pascal case, i.e PascalCase
class Person: 
    name = "Bhavesh"
    occupation = "Software Engineer"
    networth = 10 

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()

print(a.name)

# now we will change the name from here 
a.name = 'rohit'
print(a.name)
