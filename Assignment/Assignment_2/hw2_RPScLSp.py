#Lauren Song
#U79789182
#Rock Paper Scissors Lizard Spock

import random

print("Let's play Rock, Paper, Scissors, Lizard, Spock!")
user_choice = input("Enter your choice: ").lower()
choices = ["rock", "scissors", "paper", "lizard", "spock"]
data_choice = random.choice(choices)
print("Computer chose " + data_choice.capitalize())

if user_choice == data_choice:
    print("It\'s a tie")
    print("Thanks for playing!")
    
elif user_choice == "scissors":
    if data_choice == "rock":
        print("Rock crushes Scissors! Computer wins!\nThanks for playing!")
    elif data_choice == "paper":
        print("Scissors cuts Paper! You win!\nThanks for playing!")
    elif data_choice == "lizard":
        print("Scissors decapitates Lizard! You win!\nThanks for playing")
    elif data_choice == "spock":
        print("Spock smashes Scissors! Computer wins!\nThanks for playing" )
        
elif user_choice == "rock":
    if data_choice == "scissors":
        print("Rock crushes Scissors! You win!\nThanks for playing")
    elif data_choice == "paper":
        print("Paper covers Rock! Computer wins!\nThanks for playing")
    elif data_choice == "lizard":
        print("Rock crushes Lizard! You win!\nThanks for playing")
    elif data_choice == "spock":
        print("Spock vaporizes Rock! Computer wins!\nThanks for playing")
        
elif user_choice == "paper":
    if data_choice == "rock":
        print("Paper covers Rock! You win!\nThanks for playing")
    elif data_choice == "scissors":
        print("Scissors cuts Paper! Computer wins!\nThanks for playing")
    elif data_choice == "lizard":
        print("Lizard eats Paper! Computer wins!\nThanks for playing")
    elif data_choice == "spock":
        print("Paper disproves Spock! You win!\nThanks for playing")
        
elif user_choice == "lizard":
    if data_choice == "rock":
        print("Rock crushes Lizard! Computer wins!\nThanks for playing")
    elif data_choice == "scissors":
        print("Scissors decapitates Lizard! Computer wins!\nThanks for playing")
    elif data_choice == "paper":
        print("Lizard eats Paper! You win!\nThanks for playing")
    elif data_choice == "spock":
        print("Lizard poisons Spock! You win!\nThanks for playing")
        
elif user_choice == "spock":
    if data_choice == "rock":
        print("Spock vaporizes Rock! You win!\nThanks for playing")
    elif data_choice == "paper":
        print("Paper disproves Spock! Computer wins!\nThanks for playing")
    elif data_choice == "scissors":
        print("Spock smashes Scissors! You win!\n Thanks for playing")
    elif data_choice == "lizard":
        print("Lizard poisons Spock! Computer wins!\n Thanks for playing")
else:
    print('Invalid choice')
    
