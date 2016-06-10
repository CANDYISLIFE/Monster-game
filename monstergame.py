"""
the map of this gameis in the outside pocket of my bag
credit: Mr DEnnison, My dad, Ryan, sff chronicles, stack overflow
"""

bluePossesion = False
goldPossesion = False
bronzeSword = False
steelSword = False
monsterDead = False

roomNumber = 2          # Starting room
endKey = False
while not endKey:
    print("Top of loop")
    print(roomNumber)
    print(bronzeSword)
    if roomNumber == 1:
        exitRoom = False
        if bluePossesion:
            question = "You are in a room with an empty pedestal"
        else:
            question = "You pass through the tunnel and end up in a room with a blue key on a pedestal in the center or the room. Press O to pick up blue key."
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "S":
                roomNumber = 4
                exitRoom = True
            if x == "E":
                roomNumber = 2
                exitRoom = True
            if x == "W":
                question = "You are blocked by a wall; try another direction." 
               # roomNumber = 
                # exitRoom = True
            if x == "O":
                roomNumber = 1
                bluePossesion = True
                print("Hi there")
                exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True
                
    elif roomNumber == 2:
        exitRoom = False
        question = """You are in a network of caves filled with monsters, locked doors, and one final boss.
        You are armed with only the clothes on your back, a small folding knife, and your wits.
        The room you are currently in has tunnel entrances in the south, east and west.
        Your job is to make it to the room with the final boss, which contains the door to the outside world and freedom. 
        But beware, the boss is a very challenging opponent who should not be taken lightly.
        If you try to attack it or any other monsters with a weapon that is not strong enough, the monster will take your weapon and kill you.
        If you type in N, S, E, or W, you will leave the room in the direction you type. 
        In some rooms you cannot go in every direction because there is a wall or locked door. 
        The boss room is in the south-east corner of the map. 
        In some rooms there are key which can be used to open locked doors or weapons to kill monsters. 
        Press Q to quit.
        Good Luck!"""
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                question = "You are blocked by a wall; try another direction."
                roomNumber = 2 
                exitRoom = True
            if x == "S":
                roomNumber = 5
                exitRoom = True
            if x == "E":
                roomNumber = 3
                exitRoom = True
            if x == "W":
                roomNumber = 1
                exitRoom = True
            #if x == "O":
                #roomNumber = 
                #exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True
   
    elif roomNumber == 3:
        exitRoom = False
        question = "You are in a room with a blue door to the south."
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                question = "You are blocked by a wall; try another direction."
                #roomNumber == 
                #exitRoom = True
            if x == "S":
                if bluePossesion:
                    roomNumber = 6
                    exitRoom = True
                else:
                    question = "The door is locked, you need the blue key; try another direction."
            if x == "E":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "W":
                roomNumber = 2
                exitRoom = True
            #if x == "O":
                #roomNumber = 
                #exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True

               
    elif roomNumber == 4:
        exitRoom = False
        question = "Enter a direction: N, S, E, W."
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                roomNumber = 1
                exitRoom = True
            if x == "S":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 7 
                #exitRoom = True
            if x == "E":
                roomNumber = 5
                exitRoom = True
            if x == "W":
                "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            #if x == "O":
                #roomNumber = 
                #exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True    
                
    elif roomNumber == 5:
        exitRoom = False
        if bronzeSword:
            question = "There is a open chest where you previously got your sword. Where do you want to go?"
        else:
            question = """You travel through a tunnel and eventually come to a room with a chest in one corner. 
        The chest is banded in gold and has a large padlock holding it closed. Fortunately, the padlock is haging open,
        unlocked. Press O to open the box."""
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                #question = "You are blocked by a wall; try another direction."
                roomNumber = 2
                exitRoom = True
            if x == "S":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "E":
                question = "You are blocked by a wall; try another direction."
                roomNumber = 6
                exitRoom = True
            if x == "W":
                roomNumber = 4
                exitRoom = True
            if x == "O":
                question = """You pull off the lock and throw back the lid of the chest. 
            It is richly upholstered in velvet, but is completly empty. 
            The people who broke the lid off also took everything inside of it.
            Just before closing the chest and continuing in your search, you notice a strange bulge in the lining.
            You pull out your knife and cut around it. 
            The looters missed something! There is a bronze sword hidden in the lining!
            This will help you defend yourself against monsters or looters if they come back."""
                roomNumber = 5
                exitRoom = True
                bronzeSword = True
            if x == "Q":
                endKey = True
                exitRoom = True

    elif roomNumber == 6:
        exitRoom = False
        question = """There is a hideous monster in the room. You need a strong weapon to kill her.
        Press O to attack her."""
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                #question = "You are blocked by a wall; try another direction."
                roomNumber = 3
                exitRoom = True
            if x == "S":
                question = "You cannot get around the monster."
                roomNumber = 6 
                exitRoom = True
            if x == "E":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "W":
               question =  "You are blocked by a wall; try another direction."
                #roomNumber =
                #exitRoom = True
            if x == "O":
                if bronzeSword:
                    question = """You charge forward into the room. In the center is a hideous beast.
            It has huge bat wings curled around it and it long, gnarly fingernail scraped the ground as it stood.
            It appeared female from the long tangled hair that sprouted from her wrinkled skull. 
            At her full height she was pushing nine feet. You charge forward, swinging your sword. 
            She roars and attacks. You duck under her arm and thrust your sword up at her throat.
            Somehow you connect, and she sags over, yellow blood gushing from her throat.
            As she dies, the door at the other end of the room swings open. """
                    roomNumber = 9
                    exitRoom = True
                else:
                    question = """You charge forward into the room. In the center is a hideous beast.
            It has huge bat wings curled around it and it long, gnarly fingernail scraped the ground as it stood.
            It appeared female from the long tangled hair that sprouted from her wrinkled skull. 
            At her full height she was pushing nine feet. You charge forward, unfolding your swiss army knife.
            Before you can even reach her, her arm swings down at your head.
            You raise your knife to parry, but it snaps at the force of her blow and everything goes black.
            You wake up in the opening room again."""
                    roomNumber = 2 
                    exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True
               
    elif roomNumber == 7:
        exitRoom = False
        question = "There is a monster in the center of the room. The creature dropped its cloak, revealing it’s scaly body. It stood to its full height, slightly taller than a grown man. It blue-green skin and yellow abdomen reflected the sunlight, but people didn’t tend to notice this. They looked at either its long claws or its head, which was elongated and the long mouth had dozens of sharp teeth protruding from it. Press o to attack."
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "S":
                if monsterDead:
                    roomNumber = 10
                    exitRoom = True
                else:
                     question = "The monster is in your way. You have to kill him to get through."
                     roomNumber = 7
                     exitRoom = True
            if x == "E":
                roomNumber = 8
                exitRoom = True
            if x == "W":
               question = "You are blocked by a wall; try another direction."
               # roomNumber = 
                #exitRoom = True
            if x == "O":
                question = "You attack, and after a long battle, eventually kill the monster. A door to the south swings open."
                roomNumber = 7
                monsterDead = True
               # exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True
                
    elif roomNumber == 8:
        exitRoom = False
        question = "Enter a direction: N, S, E, W."
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "S":
                roomNumber = 11
                exitRoom = True
            if x == "E":
                roomNumber = 9
                exitRoom = True
            if x == "W":
                roomNumber = 7
                exitRoom = True
            #if x == "O":
               # roomNumber = 
                #exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True
                
    elif roomNumber == 9:
        exitRoom = False
        question = "Enter a direction: N, S, E, W."
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                #question = "You are blocked by a wall; try another direction."
                roomNumber = 6
                exitRoom = True
            if x == "S":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 5
                #exitRoom = True
            if x == "E":
                question = "You are blocked by a wall; try another direction."
                #roomNumber =
                #exitRoom = True
            if x == "W":
                roomNumber = 8
                exitRoom = True
            #if x == "O":
                #roomNumber = 
                #exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True
                
    elif roomNumber == 10:
        exitRoom = False
        if goldPossesion:
            question = "You are in a room with an empty pedestal"
        else:    
            question = "There is a gold key on a pedestal. Press o to pick up."
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                #question = "You are blocked by a wall; try another direction."
                roomNumber = 7
                exitRoom = True
            if x == "S":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "E":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "W":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "O":
                question = "You now have the gold key. Where do you want to go?"
                roomNumber = 10
                exitRoom = True
                goldPossesion = True
            if x == "Q":
                endKey = True
                exitRoom = True
                
    elif roomNumber == 11:
        exitRoom = False
        question = "There is a golden door east of you."
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                roomNumber = 8
                exitRoom = True
            if x == "S":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "E":
                if goldPossesion:
                    question = "In room with boss"
                    roomNumber = 12
                    exitRoom = True
                else:
                    question = "The gold door is locked, you need the gold key to enter."
                    roomNumber = 11
                    
            if x == "W":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            #if x == "O":
                #roomNumber = 
                #exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True

    elif roomNumber == 12:
        exitRoom = False
        question = "Enter a direction: N, S, E, W."
        while not exitRoom:
            validInput = False
            while not validInput:
                x = input(question)
                x = x.upper()
                if x == "N" or x == "E" or x == "S" or x == "W" or x == "O" or x == "Q":
                    validInput = True
                else:
                    question = "That is not a valid entry, bozo. " + question
            if x == "N":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "S":
                endKey = True
                exitRoom = True
            if x == "E":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            if x == "W":
                question = "You are blocked by a wall; try another direction."
                #roomNumber = 
                #exitRoom = True
            #if x == "O":
                #roomNumber = 
                #exitRoom = True
            if x == "Q":
                endKey = True
                exitRoom = True
        endKey = True
   





'''

# endKey = False
# while not endKey:
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
    Press Q to quit.
    Good Luck!""")
 '''
 
'''

    emptyRoom5 = " "
    emptyRoom4 = " "
    weaponRoom1 = " "
    blueKey = " "
    emptyRoom2 = " " 
    emptyRoom1 = " "
    monsterRoom1 = " "
    bluePossesion = 0
    goldPossesion = 0
    bronzeSword = 0
    steelSword = 0
    if weaponRoom1 or blueKey or emptyRoom2 or emptyRoom1 or monsterRoom1 or openingStory == "Q":
        print("Goodbye!")
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
    if openingStory != "N" or "S" or "E" or "W" or "Q":
        openingStory = input("That is not an option. Please enter a command.")
    if weaponRoom1 == "N":
        openingStory = input("You are back in the room where you started. Please choose N, S, E or W.")
    if weaponRoom1 == "S":
        weaponRoom1 = input("There is a solid stone wall in the way. That is not an option. Please enter a command.")
    if weaponRoom1 == "E":
        weaponRoom1 = input("There is a solid stone wall in the way. That is not an option. Please enter a command.")
    if weaponRoom1 == "W":
        emptyRoom2 = input("You are in an empty room with tunnel entrances to the north and east.")
    if weaponRoom1 != "N" or "S" or "E" or "W" or "O" or "Q":
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
    if emptyRoom1 == "O":
        if bluePossesion == 1:
            monsterRoom1 = input("""You insert the key into the door on the south wall and turn. 
        There is a clanking inside the door and it slowly swings open.
        Echoing from the tunnel is a scraping noise. As the door opens, the scraping stops.
        Then you hear a roar from whatever lurks in the next room. 
        Proceed with caution. Press O to attack whatever lies ahead.""")
        else:
            emptyRoom1 = input("""The door is locked. You try to jimmy the handle but it doesn't budge.
        Then you try to break it by running into it. Nothing works. It looks like you need to find the key.""")
    if emptyRoom1 == "W":
        openingStory = input("You are back in the room where you started")
    if monsterRoom1 == "O":
        if bronzeSword == 1:
            emptyRoom4 = input("""You charge forward into the room. In the center is a hideous beast.
            It has huge bat wings curled around it and it long, gnarly fingernail scraped the ground as it stood.
            It appeared female from the long tangled hair that sprouted from her wrinkled skull. 
            At her full height she was pushing nine feet. You charge forward, swinging your sword. 
            She roars and attacks. You duck under her arm and thrust your sword up at her throat.
            Somehow you connect, and she sags over, yellow blood gushing from her throat.
            As she dies, the door at the other end of the room swings open. """)
        if bronzeSword != 1:
            openingStory = input("""You charge forward into the room. In the center is a hideous beast.
            It has huge bat wings curled around it and it long, gnarly fingernail scraped the ground as it stood.
            It appeared female from the long tangled hair that sprouted from her wrinkled skull. 
            At her full height she was pushing nine feet. You charge forward, unfolding your swiss army knife.
            Before you can even reach her, her arm swings down at your head.
            You raise your knife to parry, but it snaps at the force of her blow and everything goes black.
            You wake up in the opening room again.""")
    if emptyRoom4 == "N":
        emptyRoom4 = input("The door slams closed behind you. Can't go that way.")
    if emptyRoom4 == "W":
        emptyRoom5 = input("You enter a room with entrances on the south, east and west walls.")
    if emptyRoom4 == "S":
        emptyRoom4 = input("There is a stone wall.")
    if emptyRoom4 == "E":
        emptyRoom4 = input("There is a stone wall.")
    if emptyRoom4 != "N" or "S" or "E" or "W":
        emptyRoom4 = input("THat is not an option. Plaese enter a viable command.")
    
        

D = ' ' 
while D != "Done":    
    A = ' '
    B = ' '
    C = input("C")
    if C == "N":
        B = input("B")
    if B == "N":
        A = input("A")
    if B == "S":
        C = input("C")
    if A == "S":
        B = input("B")
'''
