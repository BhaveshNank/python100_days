# Strings are mutable 
a = "!!!!Bhavesh !!!!!!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.strip("!")) #removes leading and trailing characters
print(a.rstrip("!")) #removes only the trailing characters and not the leading 
str1 = "Welcome to the console !!!"
print(str1.endswith("to", 4, 10)) #checks if the string ends with to within a given range of index (4,10 is the slicing here)

# find vs index method 

print(str1.find("ishhh")) #finds where your desired substring is in the string, but returns -1 if substring not present
# print(str1.index("ishhh")) #does the same as the find method but throws an error if the string is not found

#istitle method 
str2 = "World Health Organization"
print(str2.istitle()) # checks whether 1st letter of each word of the string is capitalized. 

#swapcase 
str3 = "Python is an Interpreted Language"
print(str3.swapcase()) # coverts upper case to lower case and vice versa 

#title() method 
str4 = "His name is dan. Dan is a honest man"
print(str4.title())