# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
import pathlib
from pathlib import Path
# Find the path to my Desktop C:\Users\laney\OneDrive\Desktop
desktop = Path().home().joinpath("OneDrive").joinpath("Desktop")
print(desktop)
# Create a new folder
# Filter for screenshots only
for f in desktop.iterdir():
    if f.suffix == ".png":
        print(f.name)


# Create a new path for each file
desktop.joinpath("screenshots").mkdir(exist_ok = True)

# Move the screenshot there
for f in desktop.iterdir():
    if f.suffix == ".png":
        f.replace(desktop.joinpath("screenshots").joinpath(f.name))