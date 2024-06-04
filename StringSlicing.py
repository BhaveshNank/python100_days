a = 'mango'
print(a[-1])
print(a[:-1])

'''
Question for ChatGPT
On line 2 i have tried to print the letter from the string that is present in the index
-1 the output is o from mango, on the next line line 3, i have tried to print a range of
letters from the string and the output was mang. my question is if the output for the first 
line was o at the index -1 then why when i am printing a range till -1 the output excludes 
the number at index -1.
'''

#Answer 

# the difference lies in how the indexing and slicing work. When you access a specific
# index (a[-1]), you get the character at that index. But when you slice (a[:-1]), the
# range specified is inclusive of the starting index but exclusive of the ending index.
