# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:

# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

str_in = input("String input: ")
symbol = input("Symbol input: ")
new = str_in.replace(str_in[0], symbol)
print(f"Result:{new}")


