# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random 
import sys
number = random.randint(1,20)
print(number)
tries = 3

guess = input("Enter number: ")
guess = int(guess)

while guess != number:
    tries-=1
    if tries > 0:
        guess = input("Enter number: ")
        guess = int(guess)
    else:
        print("You lost!") 
        sys.exit()  
        
print("You guessed the number, you won!") 
