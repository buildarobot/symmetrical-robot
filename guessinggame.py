
import random

def ask_guess():
    n = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess it? ")
    guess = None
    while guess != n:
        guess = int(input("Enter your guess: "))
        if guess > n:
            print("Too high! Try again. ")
        elif guess < n:
            print("Too low! Try again. ")
        else:
            print(f"Congratulations, you guessed the number {n}! ")



ask_guess()
    



    
