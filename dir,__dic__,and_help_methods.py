class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)
# print(help(Person))

print(p.__dir_)

x = [1, 2, 3, 4, 5]
print(x.__dir__())