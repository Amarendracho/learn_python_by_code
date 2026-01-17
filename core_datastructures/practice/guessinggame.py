import random

def guessing_game():

    guess = random.randint(1,25)
    number_of_attempts = 0

    while True:
        number = int(input("Guess the Number : "))
        number_of_attempts += 1

        if number > guess:
            print("Too High")
        elif number < guess:
            print("Too Low")
        else:
            print("Congratulations 🎉🍾🥳! You guessed the number")
            print(f"You guessing in {number_of_attempts} attempts")
            break

guessing_game()
