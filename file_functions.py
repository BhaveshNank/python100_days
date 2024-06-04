with open('filefunctions.txt', 'r') as f:
    print(type(f))

    # move the current position within this file to the 10th position
    f.seek(10)


    print(f.tell()) # this tells us where the current postion is, i.e returns 10 in this case
    # now read the next 5 bytes from where the current position is right now, i.e 10
    data = f.read(5)
    print(data)
    print()

'''Truncate method'''

with open('sample.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(5) # truncate method reduces the file to a specified number, in this case 5 so our file is 5 characters only

with open('sample.txt', 'r') as f:
    print(f.read())