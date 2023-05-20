#Number guessing game
import random

low = 1
high = 100
answer = random.randint(1,100)
is_running = True

print("---------------------------------------")
print("----Welcome to number guessing game----")
print("---------------------------------------")

while is_running:
    guess = int(input(f"Guess a number between {low}-{high}: "))
    if guess < 1 or guess > 100:
        print("Your number is not in the range")
    elif guess < answer:
        print("Too low! try again")
    elif guess > answer:
        print("Too high! try again")
    else:
        print("Correct answer!!!!!!")
        is_running = False
