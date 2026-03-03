from random import randint

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number\n")

def difficulty_message():
    print("Please select the difficulty level: ")
    print("1. Easy (10 Chances)")
    print("2. Medium (5 Chances)")
    print("3. Hard (3 Chances)\n")


def start_game():
    difficulty_message()
    choice = int(input("Enter your choice: "))
    diff = ""
    max_guesses = 0
    if choice == 1:
        diff = "Easy"
        max_guesses = 10
    elif choice == 2:
        diff = "Medium"
        max_guesses = 5
    elif choice == 3:
        diff = "Hard"
        max_guesses = 3
    else:
        print("Invalid choice. Please try again.")
        return
    
    print(f"Great! You have selected the {diff} level.")
    print("Let's start the game!\n")

    is_running = True
    answer = randint(1, 100)
    attempts = 0

    while is_running:
        print(answer)
        if attempts == max_guesses:
            print(f"\nYou have reached the maximum number of attempts. The correct number was {answer}.")
            again = input("\nPress q to quit or any other key to play again: ")
            if again == "q":
                is_running = False
            else:
                start_game()
        else:
            guess = int(input("Enter your guess: "))
            
            if guess == answer:
                attempts += 1
                print("\n********************************")
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                print("********************************\n")
                again = input("Press q to quit or any other key to play again.\n")
                if again == "q":
                    is_running = False
                else:
                    start_game()
            elif guess < answer:
                attempts += 1
                print(f"Incorrect! The number is greater than {guess}.")
                continue
            elif guess > answer:
                attempts += 1
                print(f"Incorrect! The number is less than {guess}.")
                continue
            else:
                print("Please enter a valid number from (1-100).")
                continue