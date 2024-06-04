# look for module_information.txt text file where the necessary information
# about modules used in this game are 

'''rules of the game 
Details of the game: 

snake vs water => snake wins (as it drinks the water)
water vs gun => water wins, gun will drown in water therefore
gun vs snake => gun wins as it kills the snake

Instructions: 

anyone who wins the game will gain 1 point. 
there will be two players one is the player himself (human) and the
other is computer, for computer you have to use random function
to choose between the three (snake, water or gun) and for human
you have to take input from the user.  '''

'''solution 
1) lets create a list for computer and human including the three moves
2) computer uses random module to get the move from list while human is prompted to choose move
3) use if else conditions to create rules of the game i.e try playing game for one time only
4) trying giving human/computer a point when they play the game and print that point
4) now that you can play the game one time with computer try implementing the game 
such that it works more that one time (lets try 3-5 times playing the game)
5) now that your program works for small input (for about 3-5 times do with 10 times)
6) announce the final winner
7) thats it - thats the game
8) to make the game more robust you can add error handling as well, for invalid moves you print invalid move
9) furthermore you can also add this: for any invalid move count will not be increased and ask you to enter your move'''

import random 

computer = ['snake', 'water', 'gun']

computer_choice = random.choice(computer)
print(f"Computer: {computer_choice}")

human = ['snake', 'water', 'gun']

computer_point = 0
human_point = 0
count = 0 

while count < 10:
    human_choice = input("Which move do you want to make: ")

    if computer_choice == 'snake' and human_choice == 'snake':
        print("Its a draw") 
        computer_point += 1
        human_point += 1

    elif computer_choice == 'gun' and human_choice == 'gun':
        print("Its a draw")
        computer_point += 1
        human_point += 1

    elif computer_choice == 'water' and human_choice == 'water':
        print("It is a draw")
        computer_point += 1
        human_point += 1

    elif computer_choice == 'snake' and human_choice == 'gun':
        print("You are the winner! ")
        human_point += 1

    elif computer_choice == 'snake' and human_choice == 'water':
        print("Computer is the winner! ")
        computer_point += 1

    elif computer_choice == 'gun' and human_choice == 'snake':
        print("Computer is the winner! ")
        computer_point += 1

    elif computer_choice == 'gun' and human_choice == 'water':
        print("Human is the winner")
        human_point += 1

    elif computer_choice == 'water' and human_choice == 'gun':
        print("Computer is the winner")
        computer_point += 1
        
    elif computer_choice == 'water' and human_choice == 'snake':
        print("Human is the winner!")
        human_point += 1
    else:
        print("Invalid move")

    print(f"Computer: {computer_point}, You: {human_point}")

    count += 1

if human_point > computer_point:
    print("You won the game")
elif human_point == computer_point:
    print("This match is a draw")
else:
    print("Computer won the game")
