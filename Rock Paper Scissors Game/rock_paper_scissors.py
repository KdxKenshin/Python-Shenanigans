import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_choice == 'q':
        break
    
    if user_choice not in choices:
        continue

    random_number = random.randint(0, 2)
    # 0 - rock, 1 - paper, 2 - scissors
    computer_choice = choices[random_number]
    print("Computer picked", computer_choice + ".")

    if user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")

