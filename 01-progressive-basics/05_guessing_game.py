import random

secretNumber = 7
userAttempts = 0

while userAttempts < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secretNumber:
        print("Congratulations! You guessed the number!")
        break
    else:
        if guess < secretNumber:
            print("Your guess is too low.")
        elif guess > secretNumber:
            print("Your guess is too high.")
        userAttempts += 1

if userAttempts == 5:
    print("Game Over!")