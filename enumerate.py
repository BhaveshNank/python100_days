marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("I'm Awesome")
#     index+=1

'''Use this instead '''

# for index, mark in enumerate(marks):
for index, mark in enumerate(marks, start = 1):
    print(index, mark)
    if index == 3: 
        print("Im awesome")
