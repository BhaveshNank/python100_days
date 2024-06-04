# 1. map 

def cube(x):
    return x*x*x

print(cube(2))

# Q. Given a list l, create a new list which has the cube of numbers present in list l 
l = [1, 2, 4, 6, 4, 3]
newl = []  # creates empty list first

# to solve this problem we simply iterate over the values in the list using for loop
for item in l:
    # print(item)
    newl.append(cube(item))

print(newl)
     
'''We have solved the problem using for loop and a new list
but we can solve this problem much easier by using the map function
see below'''

newl2 = list(map(cube, l))
# newl2 = list(map(lambda x: x**3, l)) # can also use lambda function here
print(newl2)

'''we have solved this problem using map function in only two lines of code
whereas for the first way of solving we created an empty list then 
iteraring over the items and appending it to newl so this way was 
more convenient'''

# see part 2 of where filter function is explained
