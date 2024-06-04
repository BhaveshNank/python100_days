# Match case with conditionals 

x = int(input("Enter the value of x: "))

match x: 
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _: 
        print(x)
