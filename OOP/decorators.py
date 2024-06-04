def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")


# greet(hello)() # instead of this you can use decorator on hello by writing @greet
hello()