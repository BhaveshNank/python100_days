'''Part 1 '''

x = 10 # global variable 

def my_function():
    x = 5 # local variable 
    y = 6 # local variable 

my_function()
print(x) # this prints x = 10 
# print(y)  # this will throw error as y in defined in the function and is not accessible outside

'''please see the next file of this same topic '''