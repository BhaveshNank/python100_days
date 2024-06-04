def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i 
    print(f"Average is {sum/len(numbers)}")
    # print("Average is {}".format(sum/len(numbers), 4)) # can also be used 


average(5,6)
