# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script
word = "caramel"
# Print an explanation to the user
print("Guess the word!")
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
guessword = " "
# Ask for user input
#guess = input("Enter a letter:")
# Allow only single-character alphabetic input

# Create a counter for how many tries a user has
max_guess = 10
# Keep asking them for their guess until they won or lost
while max_guess > 0:
    fail = 0
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
    for char in word:
        if char in guessword:
            print (char,end="") 
        else: 
            print ("_",end="")
            fail += 1
    
    if fail == 0:        
        print ("You won")
        break
    guess = input("guess a character:")
    guessword += guess  
    
    if guess not in word:   
     # turns counter decreases with 1 (now 9)
        max_guess -= 1        
    # print wrong
        print ("Wrong")   
    # how many turns are left
        print ("You have", + max_guess, 'more guesses' )
 
    # if the turns are equal to zero
        if max_guess == 0:              
        # print "You Lose"
            print ("You Lose"  )   
# Display a winning message and the full word if they win
