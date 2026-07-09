import random
import time

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
draws = 0

def show_menu():
    print("\n==============================")
    print(" ROCK PAPER SCISSORS GAME")
    print("==============================")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    print("==============================")

def get_user_choice():
    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            return "rock"
        elif choice == "2":
            return "paper"
        elif choice == "3":
            return "scissors"
        elif choice == "4":
            return "quit"
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

def get_winner(user, computer):
    if user == computer:
        return "draw"

    if user == "rock" and computer == "scissors":
        return "user"
    elif user == "paper" and computer == "rock":
        return "user"
    elif user == "scissors" and computer == "paper":
        return "user"
    else:
        return "computer"

def show_result(user, computer, winner):
    print("\nYou chose:", user)
    print("Computer chose:", computer)

    if winner == "draw":
        print("Result: Draw!")
    elif winner == "user":
        print("Result: You win this round!")
    else:
        print("Result: Computer wins this round!")

def show_score():
    print("\n--------- SCORE ---------")
    print("Your score:", user_score)
    print("Computer score:", computer_score)
    print("Draws:", draws)
    print("-------------------------")

print("Welcome to Rock Paper Scissors!")

while True:
    show_menu()

    user_choice = get_user_choice()

    if user_choice == "quit":
        print("\nThanks for playing!")
        show_score()
        break

    print("\nComputer is choosing", end="")
    for i in range(3):
        print(".", end="")
        time.sleep(0.5)

    computer_choice = random.choice(choices)
    winner = get_winner(user_choice, computer_choice)

    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    else:
        draws += 1

    show_result(user_choice, computer_choice, winner)
    show_score()

    play_again = input("\nDo you want to play another round? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score:")
        show_score()

        if user_score > computer_score:
            print("Congratulations! You won the game.")
        elif computer_score > user_score:
            print("Computer won the game. Better luck next time!")
        else:
            print("The game ended in a draw.")

        break