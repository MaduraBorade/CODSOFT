
import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

def play_game():
    global user_score, computer_score

    print("\nChoose one:")
    print("ROCK")
    print("PAPER")
    print("SCISSORS")

    user_choice = input("ENTER YOUR CHOICE: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        return

    computer_choice = random.choice(choices)

    print(f"\nYOU CHOOSE: {user_choice}")
    print(f"COMPUTER CHOOSE: {computer_choice}")

    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: You Lose!")
        computer_score += 1

    print(f"\nScore → You: {user_score} | Computer: {computer_score}")

def menu():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("\nThanks for playing!")
            break

menu()
