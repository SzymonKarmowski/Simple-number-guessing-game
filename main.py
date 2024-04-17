import random


print("Welcome to Number Guessing Game")
max_choice = int(input("Enter number which will be maximum number in your game"))
lives = int(input("Enter how many lives fo you want")) +1
number = random.randrange(0, stop=max_choice)

game_is_on = True


def check_answer(guess):
    if guess == number:
        print("You Win")
        quit()

    if guess > number:
        print("Too high \n")

    if guess < number:
        print("Too low \n")


while game_is_on:
    lives -= 1

    print(f"Lives remaining: {lives}")
    guess = int(input("Your Guess: "))

    check_answer(guess)

    if lives == 0:
        print(f"You ran out of lives \n Correct answer was {number}")
        quit()
