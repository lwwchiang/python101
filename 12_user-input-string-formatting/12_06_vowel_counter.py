# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

script = input("Enter sentence: ")
vowels = "aeiou"
for v in vowels:
    print(v, script.lower().count(v))