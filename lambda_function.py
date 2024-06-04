'''This is a small anonymous function without a name and are 
often used in sitations where a small function is required for
a short period of time'''


# lets define a function:
def double(x):
    return x*2

print(double(5)) # output 10 

# but instead of writing a small function consisting two lines only
# we can rather decide to write a small one line function using lamda

double2 = lambda x: x*2
print(double2(5))  # output 10

# The main role of lambda function is when you are passing a function 
# as an argument into another function, see example below 

def apply(fx, value):
    return 6 + fx(value)

print(apply(lambda x: x**3, 3))

# Therefore, in the above example we are passing a function which has no name


# lambda functions can also include multiple statements 
avg = lambda x,y,z: (x+y+z)/3

print(avg(3, 4, 5))