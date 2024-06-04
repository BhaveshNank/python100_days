'''static methods belong to a class rather than an instance of 
a class. They are called on the class itself and not on any instance
of a class'''

class Math: 
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n
        # return self.num

    @staticmethod
    def add(a, b): # as you have seen when we have using @staticmethod we dont need to give self as an argument
        return a + b
    
a = Math(10)
# print(Math.add(7, 2))
print(a.add(2, 3))