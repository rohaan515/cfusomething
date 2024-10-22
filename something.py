# Rohaan and Rafeal
# 22/10/24
# CFU 10 extensions challenge

import random
import time

def guessing_game():
    rounds = int(input("How many rounds would you like to play? "))
    difficulty = int(input("Choose difficulty level (1-10, 1-50, 1-1000): "))
   
    total_attempts = 0
   
    for _ in range(rounds):
        if difficulty == 10:
            secret_number = random.randint(1, 10)
        elif difficulty == 50:
            secret_number = random.randint(1, 50)
        elif difficulty == 1000:
            secret_number = random.randint(1, 1000)
        else:
            print("Invalid difficulty level. Please choose from 1-10, 1-50, or 1-1000.")
            return
       
        attempts = 0
        start_time = time.time()
       
        while True:
            guess = int(input(f"Guess the number (1-{difficulty}): "))
            attempts += 1
           
            if guess < secret_number:
                print("Too Low!")
            elif guess > secret_number:
                print("Too High!")
            else:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Correct! It took you {attempts} attempts and {elapsed_time:.2f} seconds.")
                break
       
        total_attempts += attempts
   
    average_attempts = total_attempts / rounds
    print(f"\nAverage attempts per round: {average_attempts:.2f}")

# Start the game
guessing_game()
