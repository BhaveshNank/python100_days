marks = [3, 5, 6, 9, 10, 12, 14]

# what value is stored in index -3 
print(marks[-3])
# convert the negative index on line 4 to positive index 
print(marks[len(marks)-3]) # this converts negative to positive index

print(marks[1:-3])
print(marks[1:len(marks)-3])

marks.sort(reverse=True)
print(marks)