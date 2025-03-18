# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

guess = input("Enter number: ")
guess = int(guess)
while guess in range(1,1000000000):
    print(guess)
    break

