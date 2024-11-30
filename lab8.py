# Write a program that will store a user's game stats into a file.
#From the game.py we defined the following functions:

# charCreation()
# showStats()
# roll4D6
# Use these methods to prompt the user for their name, determine their stats using the given functions, and write their information in a file. 
# From a main function create a new file that the user's stats will be written to. Then get the information from the given functions.
# Finally write the information into the file and close the file. Let the user know their information was successfully written.

# Submit a .py file containing your code. No screenshot is needed for this assignment.


# modules that will be used
import random
import time
import os

castle = """
                    |>>>                        |>>>
                    |                           |
                _  _|_  _                   _  _|_  _
               | |_| |_| |                 | |_| |_| |
               \  .      /                 \ .    .  /
                \    ,  /                   \    .  /
                 | .   |_   _   _   _   _   _| ,   |
                 |    .| |_| |_| |_| |_| |_| |  .  |
                 | ,   | .    .     .      . |    .|
                 |   . |  .     . .   .  ,   |.    |
     ___----_____| .   |.   ,  _______   .   |   , |---~_____
_---~            |     |  .   /+++++++\    . | .   |         ~---_
                 |.    | .    |+++++++| .    |   . |              ~-_
              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_
     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~
"""

"""
- text based game
- have rooms that contain items and other doors
- player to have stats
"""

# global variables - rooms + player

player = {"name" : "null",
          "Inventory" : {},
          "stats" : {}}

# items have a weight attribute
# currently the value of the weaponry is the quantity of that weapon

weapons = {
    "shield" : random.randint(15, 30),
    "sword" : random.randint(10, 25),
    "dagger" : random.randint(2, 7),
    }


rooms = {
    "inside_start" : {
        "items" : { "shield" : 1,
                    "sword" : 1},
        "directions" : {"left" : "hallway_left",
                        "right" : "door_right",
                        "up" : "stairs"}
        },
    
    "hallway_left" : {},
    "door_right" : {},
    "stairs" : {},
    }

def roll4D6():
    """
    roll a 6 sided die, drop the lowest value
    sum the remaining values
    return sum
    """
    arr = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    arr.remove(min(arr))
    return sum(arr)

def showStats():
    # show each stat to the player
    for stat in player["stats"]:
        print(stat, ": ", player["stats"][stat])
    
    
def charCreation():
    player["name"] = input("Enter your name: ")

    player["stats"] = {"str" : roll4D6(),
                       "dex" : roll4D6(),
                       "cons" : roll4D6(),
                       "int" : roll4D6(),
                       "char" : roll4D6(),
                       "weight" : 0}

    player["stats"]["weight"] = player["stats"]["str"] * 15

def moveIntoRoom(room):
    # let the user 'see' around the room
    # let user pick up items
    # let user choose where to go next
    print("you are now in room: ", room)
    print("A. See around the room")
    print("B. Show items in room")
    print("C. Go into another room")
    choice = input("What would you like to do: ")

    if choice.upper() == "A":
        print("There is a room to", end=" ")
        for direction in room["directions"]:
            print(direction, end=" ")
    elif choice.upper() == "B":
        print("Here are the items in the room: ")
        for item in room["items"]:
            print(item)
    elif choice.upper() == "C":
        room_choice = input("Which direction would you like to go: ")
        # room_choice; user said "left"
        if room_choice.lower() in room["directions"]:
            #            rooms["hallway_left"]
            moveIntoRoom(rooms[room["directions"][room_choice]])
            pass
        else:
            print("Invalid direction")

            
            
    

def startGame():
    time.sleep(2)
    os.system('cls')
    print("\n\n\nYou awaken in front of a castle on an island.")
    print("You can go <INSIDE> or <EAST>")
    nextMove = input("Where do you want to go: ")

    while True:
        if nextMove.upper() == "INSIDE":
            moveIntoRoom(rooms["inside_start"])
            break
        elif nextMove.upper() == "EAST":
            print("There is a garden. Not much to see.")
            # later: implement garden
            break
        else:
            print("Invalid input.")

def save_player_stats():
    fileOut = open("stats.txt", "w")
    fileOut.write("did this work")
    fileOut.close()

def main():
    print(castle)
    save_player_stats()
    start_point = input("Enter your load file key or type <START> to begin: ")

    if start_point.upper() == "START":
        charCreation()
        input("***Hit any key to begin***")
        startGame()
    else:
        print("Unavailble")
    pass



main()