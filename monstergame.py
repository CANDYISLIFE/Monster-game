"""
the map of this gameis in the outside pocket of my bag
"""

openingStory = input("""You are in a network of caves filled with monsters, locked doors, and one final boss.
You are armed with only the clothes on your back, a small folding knife, and your wits.
The room you are currently in has tunnel entrances in the south, east and west.
Your job is to make it to the room with the final boss, which contains the door to the outside world and freedom. 
But beware, the boss is a very challenging opponent who should not be taken lightly.
If you try to attack it or any other monsters with a weapon that is not strong enough, the monster will take your weapon and kill you.
If you type in N, S, E, or W, you will leave the room in the direction you type. 
In some rooms you cannot go in every direction because there is a wall or locked door. 
The boss room is in the south-east corner of the map. 
In some rooms there are key which can be used to open locked doors or weapons to kill monsters. 
Good Luck!""")

bluePossesion = 0
goldPossesion = 0
bronzeSword = 0
steelSword = 0

if openingStory == "N":
    openingStory = input("There is a solid stone wall. You cannot go North.")
if openingStory == "S":
    weaponRoom1 = input("""You travel through a tunnel and eventually come to a room with a chest in one corner. 
    The chest is banded in gold and has a large padlock holding it closed. Fortunately, the padlock is haging open,
    unlocked. Press O to open the box.""")
    if weaponRoom1 == "O":
        weaponRoom1 = input("""You pull off the lock and throw back the lid of the chest. 
        It is richly upholstered in velvet, but is completly empty. 
        The people who broke the lid off also took everything inside of it.
        Just before closing the chest and continuing in your search, you notice a strange bulge in the lining.
        You pull out your knife and cut around it. 
        The looters missed something! There is a bronze sword hidden in the lining!
        This will help you defend yourself against monsters or looters if they come back.""")
        bronzeSword = 1
if openingStory == "E":
    emptyRoom1 == input("""There is a tunnel in the west and a locked blue door in the south. 
    Press O to try to open the door""")
if openingStory == "W":
    blueKey = input("""You pass through the tunnel and end up in a room with a blue key on a pedestal in the center or the room.
    Press O to pick up blue key.""")
    if blueKey == "O":
        blueKey = input("You now have the blue key in your inventory.")
        bluePossesion = 1
if openingStory != "N" or "S" or "E" or "W":
    openingStory = input("That is not an option. Please enter a command.")
if weaponRoom1 == "N":
    openingStory = input("You are back in the room where you started. Please choose N, S, E or W.")
if weaponRoom1 == "S":
    weaponRoom1 = input("There is a solid stone wall in the way. That is not an option. Please enter a command.")
if weaponRoom1 == "E":
    weaponRoom1 = input("There is a solid stone wall in the way. That is not an option. Please enter a command.")
if weaponRoom1 == "W":
    emptyRoom2 = input("You are in an empty room with tunnel entrances to the north and east.")
if weaponRoom1 != "N" or "S" or "E" or "W" or "O":
    weaponRoom1 = input("That is not an option. Please enter a command.")
if blueKey == "E":
    openingStory = input("You are back in the room where you started. Please choose N, S, E or W.")
if blueKey == "W":
    blueKey = input("There is a solid stone wall in the way. That is not an option. Please enter a command.")
if blueKey == "N":
    blueKey = input("There is a solid stone wall in the way. That is not an option. Please enter a command.")
if blueKey == "S":
    emptyRoom2 = input("You are in an empty room with tunnel entrances to the north and east.")
if emptyRoom2 == "N":
    if bluePossesion == 1:
        blueKey = input("You are in a room with an empty pedestal and entrances to the east and south.")
    else:
        blueKey = input("""You pass through the tunnel and end up in a room with a blue key on a pedestal in the center or the room.
    Press O to pick up blue key.""")
    if blueKey == "O":
        blueKey = input("You now have the blue key in your inventory.")
        bluePossesion = 1
        
if emptyRoom2 == "S":
    emptyRoom2 = input("There is a solid stone wall in the way. That is not an option. Please enter a command.")
if emptyRoom2 == "E":
    if bronzeSword == 0:
        weaponRoom1 = input("""You travel through a tunnel and eventually come to a room with a chest in one corner. 
    The chest is banded in gold and has a large padlock holding it closed. Fortunately, the padlock is haging open,
    unlocked. Press O to open the box.""")
    if weaponRoom1 == "O":
        weaponRoom1 = input("""You pull off the lock and throw back the lid of the chest. 
        It is richly upholstered in velvet, but is completly empty. 
        The people who broke the lid off also took everything inside of it.
        Just before closing the chest and continuing in your search, you notice a strange bulge in the lining.
        You pull out your knife and cut around it. 
        The looters missed something! There is a bronze sword hidden in the lining!
        This will help you defend yourself against monsters or looters if they come back.""")
        bronzeSword = 1
    else:
        weaponRoom1 = input("You are in a room with an open empty chest in one corner. There are entrances to the north and west.")
            
if emptyRoom2 == "W":
     emptyRoom2 = input("There is a solid stone wall in the way. That is not an option. Please enter a command.")
