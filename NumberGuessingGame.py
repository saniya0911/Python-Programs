import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num=random.randint(1,100)

difficulty = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
attempts = {
    "hard":5,
    "easy":10
}
attempt = attempts[difficulty]

while(attempt>0):
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if(guess ==num):
        print(f"You got it! The answer was {num}.")
        attempt=0
    elif guess>num:
        print("Too high.")
        attempt-=1
        if attempt ==0:
         print("You lose!")
        else:
         print("Guess again.")
    else:
        print("Too low.")
        attempt-=1
        if attempt ==0:
         print("You lose!")
        else:
         print("Guess again.")
