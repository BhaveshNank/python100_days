# Example 1 
condition = True

# if condition:
#     result = 1
# else:
#     result = 0


# the above can be written as: 
result = 1 if condition else 0 
print(result)


# Example 2 
a = 300 
b = 400 

print("A") if a > b else print("=") if a==b else print("B")


# This and the above line is the same 

# if a >b :
#     print("A")
# elif a == b:
#     print("=")
# else:
#     print("B")