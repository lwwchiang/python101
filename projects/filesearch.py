# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.
import pathlib
path = pathlib.Path("C:\\Users\\laney\\OneDrive\\Documents\\CodingNomads")

for item in path.iterdir():
    if item.suffix == '.jpg':  # Filter for screenshots only
        print(item.name) 
    elif item.is_dir():
        for item2 in item.iterdir():
            if item2.suffix == '.jpg':
                print(item2.name)