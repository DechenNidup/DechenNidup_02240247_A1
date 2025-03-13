import random

def guess_number():
    print("\nWelcome to Guess the Number!")
    print("I have picked a number between 1 and 20. Try to guess it!")

    number = random.randint(1, 20)
    
    while True:
        guess = input("Enter your guess: ")
        
        if not guess.isdigit():
            print("Please enter a number!")
            continue

        guess = int(guess)

        if guess < 1 or guess > 20:
            print("Out of range! Pick between 1 and 20.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congrats! You got it right!")
            break

def rock_paper_scissors():
    print("\nWelcome to Rock-Paper-Scissors!")
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'back' to return): ").lower()

        if user_choice == "back":
            break
        if user_choice not in choices:
            print("Invalid choice, try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer picked: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

def main():
    while True:
        print("\n----- Game Menu -----")
        print("1. Play Guess the Number")
        print("2. Play Rock-Paper-Scissors")
        print("3. Exit")

        choice = input("Pick an option (1-3): ")

        if choice == "1":
            guess_number()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            print("Thanks for playing! Bye!")
            break
        else:
            print("Invalid choice! Try again.")

main()

