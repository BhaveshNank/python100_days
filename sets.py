s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# Union and Update
print(s1.union(s2)) # This creates a new set and s1 an s2 remain unchanged
print(s1, s2) # showing s1 and s2 remains unchanged
s3 = s1.union(s2) # creating a new variable and storing the new union set is the same as above
print(s3) # Now stored the union set into s3 and printing s3 

''' since s1 and s2 remains unchanged how do we change them?
so we use the update method to do this, see below '''

s1.update(s2)  # merges s2 into s1 however s2 still remains the same
print(s1, s2)
print()

# intersection and intersection_update
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
# print(cities)

cities.intersection_update(cities2) #update cities this time
print(cities)
print()

# Symmetric difference 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2) #all (union) exluding the intersection -> ones which are not common
print(cities3)


# Difference and difference update
'''
These methods prints only items that are present in the original
set and not in both sets. difference() returns new set while 
difference_update updates the original set 
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2) 
print(cities3)

# Note run one at a time, comment all the set methods and only
# run the one you want to run at the moment 



