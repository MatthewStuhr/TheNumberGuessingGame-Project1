"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------



"""

import random


def start_game():
    print("""
    *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
    Welcome to the Number Guessing Game! Have fun!
    *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
    """)
    
    answer = random.randint(1, 10)
    
    guess_count = 0
    
    best_score = 0
    
    play_count = 1
    
    while True:
        try:
            new_guess = input("Pick a number between 1 and 10:  ")
            new_guess = int(new_guess)
            if new_guess < 1 or new_guess > 10:
                raise ValueError("Your guess needs to be within the 1-10 range")
        except ValueError as err:
            print("Oh no, we ran into an issue. {}. Please enter a number between 1 and 10!".format(err))
            continue
        
            
        
        else:
            if new_guess < answer:
                print("It is higher!")
                guess_count += 1
            elif new_guess > answer:
                print("It is lower!")
                guess_count += 1
            elif new_guess == answer:
                guess_count += 1
                print("You got it! It took you {} attempts.".format(guess_count))
                
                if guess_count < best_score or play_count == 1:
                    best_score = guess_count
                    
                
                    
                continue_game = input("Would you like to play another round? Y/N : ")
                if continue_game.lower() == "y":
                    guess_count = 0
                    answer = random.randint(1, 10)
                    play_count += 1
                    print("Your best score is {}!".format(best_score))
                    
                elif continue_game.lower() == "n":
                    print("Have a great day!")
                    break
                
            
            
    
    


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
