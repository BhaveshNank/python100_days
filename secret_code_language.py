'''Rules to encode
1) if string contains atleast 3 characters (>= 3), remove 1st letter and 
append it at the end
2) now append 3 random characters at the start and at the end 

else
reverse the string

    Rules to decode 
1) If word is less than 3 characters reverse it
2) Remove 3 characters from start and end. now remove last letter
and append it to the beginning'''


def encode(string):
    words = string.split(" ")
    word_list = []
    for word in words: 
        if len(word) >= 3:
            new_word = word[1:] + word[0]
            encoded_string = 'qwe' + new_word + 'iop'
            word_list.append(encoded_string)
            # print(word_list) # debug statement
        else:
            word_list.append(word[::-1])
    return " ".join(word_list)


def decode(string):
    words = string.split(" ")
    word_list = []
    for word in words: 
        if len(word) < 3:
            encoded_string = word[::-1]
            word_list.append(encoded_string)
        else:
            new_word = word[3:-3]
            encoded_string = new_word[-1:] + new_word[:-1] # instead of new_word[-1:], new_word[-1] will also
            word_list.append(encoded_string)
    return " ".join(word_list)

ask = input("Do you want to encode or decode: ")
if ask == 'encode':
    print(encode(input('Enter the string you want to encode: ')))
    # print(encode('Bhavesh')) # or simply print the function call
elif ask == 'decode':
    print(decode(input("Enter the message you want to decode: ")))
else:
    print("Sorry, this feature is not available")




'''This program was purely done by Bhavesh'''