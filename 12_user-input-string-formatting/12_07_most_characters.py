# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

no_of_lines = 3
lines = ""
for i in range(no_of_lines):
    lines+=input()+"\n"
print(lines)

longest = max(lines.split(), key=len)
print(len(longest),longest)


# x, y, z = input("Values: \n ").split()

#lines = []

##   user_input = input()

    # 👇️ if the user presses Enter without a value, break out of the loop
  #  if user_input == '':
   #     break
   # else:
    #    lines.append(user_input + '\n')


# 👇️ prints list of strings
#print(lines)

# 👇️ join list into a string
#print(''.join(lines))