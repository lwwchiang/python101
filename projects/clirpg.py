# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
print(input("Enter your name: "))
# Display a message that greets them and introduces them to the game world.
print("Welcome to CLI RPG game workd!")
# Present them with a choice between two doors.
sword = ""
# If they choose the left door, they'll see an empty room.
while True: 
    doors= input("choose the door(left/right): ")   
    if doors == "left":
        print("empty room")
        look = input("look around or go back: ") 
        if look == "look around":
            print("sword")
            sword = input("take it or leave it: ")                
        elif look == "go back":
            continue    
# If they choose the right door, then they encounter a dragon.
    elif doors == "right":
        print("encouter a dragon")
        fight = input("fight yes or no: ")
        if fight == "yes":
            if sword == "take":
                print("defeat the dragon: ")
            else:
                print("you got eaten by the dragon! ")   
            break
        else:
            continue         
            
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.
