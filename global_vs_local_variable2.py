'''Part 2 -> in part 1 we saw what is global and local variable
here we will see how we will change the global variable from within
the function'''

x = 10 # global variable 

def my_function():
    global x
    # global y 
    x = 5 # local variable 
    y = 6 # local variable 

my_function()
print(x) # this now prints x = 5 and not 10

# print(y)  # this will throw error as y in defined in the function and is not accessible outside
# however if you make y global by the keyword used above for x then you can print this y here
