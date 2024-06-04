'''
you have to create a program like kaun banega crorepati.
you have to use lists to store your questions and answers
you will ask the user do you want to play, if they say yes then
you have to display the questions one and allow them to answer.
if there answer is correct, it should show them the answer is correct
and move to the next question otherwise it should stop the program
and tell the user that their answer was wrong and tell them the amount
they will be going with. if at all the user chooses no when asked to 
play simply exit the program
'''


ask = input("Welcome to Kaun Banega Crorepati\nDo you want to play the game (Yes/No) ")

qa_list = [
    ["Q1. Who is prime minister of India", "Narendra Modi".lower()],
    ["Q2. What is capital City of India", "New Delhi".lower()],
    ["Q3. Python is an interpreted language True or False", "True".lower()],
    ["Q4. There is no array data structure in python True or False", "True".lower()],
    ["Q5. Is Java an object oriented language", "Yes".lower()],
]

sum = 0

if ask == "Yes".lower():
    print("The game begins\n") 
    for qa in qa_list:
        question = qa[0]
        print(question)
        user_response = input("Your answer: ")
        if user_response == qa[1]:
            print("Correct Answer")
            sum = sum + 5000
            print(f"You have won {sum} rupees")
        else:
            print("YOUR ANSWER IS NOT CORRECT")
            print(f"Your final amount you will take home is {sum}")
            break
else:
    print(f"You are the winner of this game, you won {sum} in total")
    exit()
