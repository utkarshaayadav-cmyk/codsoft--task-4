#Rock,Paper,Scissors Game

import random
user_score = 0
computer_score =  0
choices = ["rock", "paper","scissors"]

print("Welcome To rock paper scissors Game")
while True:
    user_choice = input("\nChoose rock,paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid Choice! Please try again.")
        continue
    computer_choice = random.choice(choices)
    print("Your choice:",user_choice)
    print("computer choice:", computer_choice)
    if user_choice == computer_choice:
        print("Result: It's a tie!")
    elif (
        (user_choice == "rock" and
computer_choice == "scissors") or
        (user_choice == "scissors" and
computer_choice == "paper") or
        (user_choice == "paper" and
computer_choice == "rock")
        ):
            print("Result:You Win!")
            user_score += 1
    else:
        print("Result:You loose!")
        computer_score += 1
    print(f"score -> you: {user_score}| computer: {computer_score} ")
    play_again = input("\nDo you want to play again? (yes/no):").lower()
    if play_again != "yes" :
        print("Thanks for playing!")
        break
        
            