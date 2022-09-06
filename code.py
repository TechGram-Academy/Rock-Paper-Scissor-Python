# Create Rock Paper Scissor game
# Play with Computer (Where Computer will choose randomely, not conditionally).
# Get the input from user and print the result. 
import random

user_choice = input("Enter your move (Rock, Scissor, Paper): ")
computer_choice = random.choice(["Rock", "Scissor", "Paper"])


if user_choice == computer_choice:
    print("Match Tie")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers Rock, Computer wins")
    else:
        print("Rock smashes Scissor, You won")
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cuts paper, Computer wins" )
    else:
        print("Paper covers Rock, You won.")
elif user_choice == 'Scissor':
    if computer_choice == "Rock":
        print("Rock smashes scissor, Computer won")
    else:
        print("Scissor cuts Paper, You won")



