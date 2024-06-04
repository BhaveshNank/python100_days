from functools import reduce

# list of numbers 
numbers = [1, 2, 3, 4, 5]

def mysum(x, y):
    return x + y

sum = reduce(mysum, numbers)
# sum = reduce(lambda x, y: x+y, numbers) # you can use this instead for one line of code 
print(sum)