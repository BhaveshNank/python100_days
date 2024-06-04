# you need to develop a calculator in which you will first ask the user what 
# operation they want to perform, whether it be +, -, *, / or //. note you cannot use 
# if else conditional to solve the problem 

print("""In this calculator we have 5 operations
      1) Addition '+'
      2) Subtraction '-'
      3) Multiplication '*'
      4) Division '/'
      5) Modulo '//' """)

print("Choose two integers")
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

Add = num1 + num2 
Sub = num1 - num2 
Mul = num1 * num2 
Div = num1 / num2 
Mod = num1 // num2 

print("Addition of the two numbers are ", Add)
print("Subtraction of the two numbers are", Sub)
print("Multiplication of the two numbers are ", Mul)
print("Division of the two numbers are", Div)
print("Modulos of the two numbers are", Mod)