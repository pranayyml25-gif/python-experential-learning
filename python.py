import random

def get_guess(player):
    while True:
        try:
            guess = int(input(f"{player}, enter your guess (1-100): "))

            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def number_guessing_race():
    secret_number = random.randint(1, 100)

    print("🎯 NUMBER GUESSING RACE")
    print("You vs. Computer")
    print("First one to guess the secret number wins!")
    print("Guess a number between 1 and 100.\n")

    while True:
        # Player's turn
        player_guess = get_guess("You")

        if player_guess == secret_number:
            print("🎉 You guessed the number!")
            print("🏆 YOU WIN!")
            break
        elif player_guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        # Computer's turn
        computer_guess = random.randint(1, 100)
        print(f"💻 Computer guessed: {computer_guess}")

        if computer_guess == secret_number:
            print("💻 Computer guessed the number!")
            print("😔 COMPUTER WINS!")
            break

        print()


number_guessing_race()