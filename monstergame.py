openingStory = input("""You are in a network of caves filled with monsters, locked doors, and one final boss. 
Your job is to make it to the room with the final boss, which contains the door to the outside world and freedom. 
But beware, the boss is a very challenging opponent who should not be taken lightly.
If you try to attack it or any other monsters with a weapon that is not strong enough, the monster will take your weapon and kill you.
If you type in N, S, E, or W, you will leave the room in the direction you type. 
In some rooms you cannot go in every direction because there is a wall or locked door. 
The boss room is in the south-east corner of the map. 
In some rooms there are key which can be used to open locked doors or weapons to kill monsters. 
Good Luck!""")

bluePossesion = 0
if openingStory == "N":
    openingStory = input("There is a solid stone wall. You cannot go North.")
if openingStory == "S":
    weaponRoom1 = input("""You travel through a tunnel and eventually come to a room with a chest in one corner. 
    The chest is banded in gold and has a large padlock holding it closed. Fortunately, the padlock is haging open,
    unlocked. Press O to open the box.""")
    #if weaponRoom1 == 