# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

x = input("String input: ")
y = input("letter input: ")
z = x.find(y)

print(f"Result: {z}")
