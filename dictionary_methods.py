ep1 = {122:45, 123:89, 567:69, 670:69}
ep2 = {222:67, 566:90}

ep1.update(ep2) #updates ep1 with the dictionary ep2 
print(ep1)

ep1.pop(122) # removes the key-value pair whose key is passed as parameter (122 in this case)
print(ep1)

ep1.popitem() # removes last key-value pair from dictionary
print(ep1)

ep1.clear()   # deletes all elements from the dictionary
print(ep1)

del ep1  # deletes the dictionary ep1 
# print(ep1) #throws error when printing dict that is deleted 


