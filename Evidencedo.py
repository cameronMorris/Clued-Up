import os
import random 
import socket
import time

def characterSelection():
    characterLoop = 1
    while characterLoop == 1:
        print("")
        print("=============================")
        print("Character Selection")
        print("=============================")
        print("")
        print("1. Cameron Morris")
        print("2. Sam Forrester")
        print("3. Archie Waldron")
        print("4. Matthew Fearnley")
        print("5. Amber Languille")
        print("6. Nathan Hopper")
        print("")
        characterSelection = input("Select your character: ")
        if not characterSelection in ["1","2","3","4","5","6"]:
            print("")
            print("This is not a valid option")
            time.sleep(1)
            os.system("cls")
            continue
        if characterSelection == "1":
            characterLoop = 0
            playerAvatar = ("Cameron Morris")
        if characterSelection == "2":
            characterLoop = 0
            playerAvatar = ("Sam Forrester")
        if characterSelection == "3":
            characterLoop = 0
            playerAvatar = ("Archie Waldron")
        if characterSelection == "4":
            characterLoop = 0
            playerAvatar = ("Matthew Fearnley")
        if characterSelection == "5":
            characterLoop = 0
            playerAvatar = ("Amber Languille")
        if characterSelection == "6":
            characterLoop = 0
            playerAvatar = ("Nathan Hopper")
        continue       
    print("")
    print("You are " + playerAvatar)
    time.sleep(1.5)
    return playerAvatar

def makeFinalAccusation(killer, murderLocation, murderWeapon):
    print("")
    print("=============================")
    print("Final Accusation")
    print("=============================")
    print("")
    print("I think it was...")
    print("")
    print("1. Cameron Morris")
    print("2. Sam Forrester")
    print("3. Archie Waldron")
    print("4. Matthew Fearnley")
    print("5. Amber Languille")
    print("6. Nathan Hopper")
    print("")
    finalKiller = input("Enter your option here: ")
    if not finalKiller in ["1","2","3","4","5","6"]:
        print("")
        print("This is not a valid option")
        time.sleep(1)
        os.system("cls")
    if finalKiller == "1":
        finalKillerGuess = ("Cameron Morris")
    if finalKiller == "2":
        finalKillerGuess = ("Sam Forrester")
    if finalKiller == "3":
        finalKillerGuess = ("Archie Waldron")
    if finalKiller == "4":
        finalKillerGuess = ("Matthew Fearnley")
    if finalKiller == "5":
        finalKillerGuess = ("Amber Languille")
    if finalKiller == "6":
        finalKillerGuess = ("Nathan Hopper")
    os.system("cls")
    print("")
    print("=============================")
    print("Final Accusation")
    print("=============================")
    print("")
    print(killer)
    print(murderLocation)
    print(murderWeapon)
    print("")
    print("I think it was " + finalKillerGuess)
    print("In the...")
    print("1. Lobby")
    print("2. Dining Room")
    print("3. Living Room")
    print("4. Master Bedroom")
    print("5. Kitchen")
    print("6. Library")
    print("7. Attic")
    print("8. Basement")
    print("9. Home Theatre")
    print("10. Bathroom")
    print("")
    finalLocation = input("Enter your option here: ")
    if not finalLocation in ["1","2","3","4","5","6","7","8","9","10"]:
        print("")
        print("This is not a valid option")
        time.sleep(1)
        os.system("cls")
    if finalLocation == "1":
        finalLocationGuess = ("Lobby")
    if finalLocation == "2":
        finalLocationGuess = ("Dining Room")
    if finalLocation == "3":
        finalLocationGuess = ("Living Room")
    if finalLocation == "4":
        finalLocationGuess = ("Master Bedroom")
    if finalLocation == "5":
        finalLocationGuess = ("Kitchen")
    if finalLocation == "6":
        finalLocationGuess = ("Library")
    if finalLocation == "7":
        finalLocationGuess = ("Attic")
    if finalLocation == "8":
        finalLocationGuess = ("Basement")
    if finalLocation == "9":
        finalLocationGuess = ("Home Theatre")
    if finalLocation == "10":
        finalLocationGuess = ("Bathroom")
    os.system("cls")
    print("")
    print("=============================")
    print("Final Accusation")
    print("=============================")
    print("")
    print("I think it was " + finalKillerGuess)
    print("In the " + finalLocationGuess)
    print("")
    print("With the...")
    print("")
    print("1. Revolver")
    print("2. Knife")
    print("3. Rope")
    print("4. Poision")
    print("5. Baseball Bat")
    print("6. Statue")
    print("7. Hammer")
    print("8. Cheese Grater")
    print("")
    finalWeapon = input("Enter your option here: ")
    if not finalWeapon in ["1","2","3","4","5","6","7","8"]:
        print("")
        print("This is not a valid option")
        time.sleep(1)
        os.system("cls")
    if finalWeapon == "1":
        finalWeaponGuess = ("Revolver")
    if finalWeapon == "2":
        finalWeaponGuess = ("Knife")
    if finalWeapon == "3":
        finalWeaponGuess = ("Rope")
    if finalWeapon == "4":
        finalWeaponGuess = ("Poison")
    if finalWeapon == "5":
        finalWeaponGuess = ("Baseball Bat")
    if finalWeapon == "6":
        finalWeaponGuess = ("Statue")
    if finalWeapon == "7":
        finalWeaponGuess = ("Hammer")
    if finalWeapon == "8":
        finalWeaponGuess = ("Cheese Grater")
    os.system("cls")
    print("")
    print("=============================")
    print("Final Accusation")
    print("=============================")
    print("")
    print("I think it was " + finalKillerGuess)
    print("In the " + finalLocationGuess)
    print("With the " + finalWeaponGuess)
    print("")
    time.sleep(3)
    if finalKillerGuess == killer:
        print("")
        print(finalKillerGuess + " is the Killer")
    else:
        print("")
        print(finalKillerGuess + " is not the Killer")
    if finalLocationGuess == murderLocation:
        print("")
        print("The " + finalLocationGuess + " is the Murder Location")
    else:
        print("")
        print("The " + finalLocationGuess + " is not the Murder Location")
    if finalWeaponGuess == murderWeapon:
        print("")
        print("The " + finalWeaponGuess + " is the Murder Weapon")
    else:
        print("")
        print("The " + finalWeaponGuess + " is not the Murder Weapon")
    print("")
    print("There isn't a game to win yet")
    time.sleep(1)
    print("")
    goBack = input("Press enter to return to the main menu: ")
    time.sleep(1)
    gameLoop = 1 

def playerCardSelection(playerAvatar, killer, murderLocation, murderWeapon):
    allCards = ["Cameron Morris", "Sam Forrester", "Archie Waldron", "Matthew Fearnley", "Amber Languille",
                "Nathan Hopper", "Lobby", "Dining Room", "Living Room", "Master Bedroom", "Kitchen", "Library",
                "Attic", "Basement", "Home Theatre", "Bathroom", "Revolver", "Knife", "Rope", "Poison",
                "Baseball Bat", "Statue", "Hammer", "Cheese Grater"]
    allCards.remove(killer)
    allCards.remove(murderLocation)
    allCards.remove(murderWeapon)
    playerCards = []
    for i in range(7):
        cardChoice = (random.choice(allCards))
        playerCards.append(cardChoice)
        allCards.remove(cardChoice)
    print("=============================")
    if playerAvatar == str("Cameron Morris"):
        print(playerAvatar + "' Cards")
    else:
        print(playerAvatar + "'s Cards")
    print("=============================")
    print("")
    print("Your dealt cards are: \n")
    for playerCard in playerCards:
        print(playerCard)
    numberOfCards = 7
    time.sleep(3)
    return playerCards

def playerGuess(currentLocation, killer, murderLocation, murderWeapon):
    if currentLocation == ("Outside The House"):
            print("")
            print("You must enter the house before you can take a guess")
            time.sleep(2)
            os.system("cls")
    else:
        locationGuess = (currentLocation)
        print("")
        print("=============================")
        print(currentLocation)
        print("=============================")
        print("")
        print("I think it was...")
        print("")
        print("1. Cameron Morris")
        print("2. Sam Forrester")
        print("3. Archie Waldron")
        print("4. Matthew Fearnley")
        print("5. Amber Languille")
        print("6. Nathan Hopper")
        print("")
        killerChoice = input("Enter your option here: ")
        if not killerChoice in ["1","2","3","4","5","6"]:
            print("")
            print("This is not a valid option")
            time.sleep(1)
            os.system("cls")
        if killerChoice == "1":
            killerGuess = ("Cameron Morris")
        if killerChoice == "2":
            killerGuess = ("Sam Forrester")
        if killerChoice == "3":
            killerGuess = ("Archie Waldron")
        if killerChoice == "4":
            killerGuess = ("Matthew Fearnley")
        if killerChoice == "5":
            killerGuess = ("Amber Languille")
        if killerChoice == "6":
            killerGuess = ("Nathan Hopper")
        os.system("cls")
        print("")
        print("=============================")
        print(currentLocation)
        print("=============================")
        print("")
        print("I think it was " + killerGuess)
        print("In the " + locationGuess)
        print("")
        print("With the...")
        print("")
        print("1. Revolver")
        print("2. Knife")
        print("3. Rope")
        print("4. Poision")
        print("5. Baseball Bat")
        print("6. Statue")
        print("7. Hammer")
        print("8. Cheese Grater")
        print("")
        weaponChoice = input("Enter your option here: ")
        if not weaponChoice in ["1","2","3","4","5","6","7","8"]:
            print("")
            print("This is not a valid option")
            time.sleep(1)
            os.system("cls")
        if weaponChoice == "1":
            weaponGuess = ("Revolver")
        if weaponChoice == "2":
            weaponGuess = ("Knife")
        if weaponChoice == "3":
            weaponGuess = ("Rope")
        if weaponChoice == "4":
            weaponGuess = ("Poison")
        if weaponChoice == "5":
            weaponGuess = ("Baseball Bat")
        if weaponChoice == "6":
            weaponGuess = ("Statue")
        if weaponChoice == "7":
            weaponGuess = ("Hammer")
        if weaponChoice == "8":
            weaponGuess = ("Cheese Grater")
        os.system("cls")
        print("")
        print("=============================")
        print(currentLocation)
        print("=============================")
        print("")
        print("I think it was " + killerGuess)
        print("In the " + locationGuess)
        print("With the " + weaponGuess)
        if killerGuess == killer:
            print("")
            print(killerGuess + " is the Killer")
        else:
            print("")
            print(killerGuess + " is not the Killer")
        if locationGuess == murderLocation:
            print("")
            print("The " + locationGuess + " is the Murder Location")
        else:
            print("")
            print("The " + locationGuess + " is not the Murder Location") 
        if weaponGuess == murderWeapon:
            print("")
            print("The " + weaponGuess + " is the Murder Weapon")
        else:
            print("")
            print("The " + weaponGuess + " is not the Murder Weapon")
        # This needs to properly update the suspect list
        print("")
        goBack = input("Press enter to return to the turn menu: ")
        #Eventually needs to return the player guesses

def roomTraversal(currentLocation):
    roomLoop = 1
    while roomLoop == 1:
        print("")
        print("=============================")
        print(currentLocation)
        print("=============================")
        print("")
        print("Which room would you like to go to?")
        print("")
        print("1. Lobby")
        print("2. Dining Room")
        print("3. Living Room")
        print("4. Master Bedroom")
        print("5. Kitchen")
        print("6. Library")
        print("7. Attic")
        print("8. Basement")
        print("9. Home Theatre")
        print("10. Bathroom")
        print("")
        newRoom = input("Enter your option here: ")
        if not newRoom in ["1","2","3","4","5","6","7","8","9","10"]:
            print("")
            print("This is not a valid option")
            time.sleep(1)
            os.system("cls")
            continue
        if newRoom == "1":
            roomLoop = 0
            currentLocation = ("Lobby")
        if newRoom == "2":
            roomLoop = 0
            currentLocation = ("Dining Room")
        if newRoom == "3":
            roomLoop = 0
            currentLocation = ("Living Room")
        if newRoom == "4":
            roomLoop = 0
            currentLocation = ("Master Bedroom")
        if newRoom == "5":
            roomLoop = 0
            currentLocation = ("Kitchen")
        if newRoom == "6":
            roomLoop = 0
            currentLocation = ("Library")
        if newRoom == "7":
            roomLoop = 0
            currentLocation = ("Attic")
        if newRoom == "8":
            roomLoop = 0
            currentLocation = ("Basement")
        if newRoom == "9":
            roomLoop = 0
            currentLocation = ("Home Theatre")
        if newRoom == "10":
            roomLoop = 0
            currentLocation = ("Bathroom")
    print("")
    print("You are now in the " + currentLocation)
    print("")
    time.sleep(1.5)
    goBack = input("Press enter to return to the turn menu: ")
    return currentLocation

def rules():
    print("")
    print("If you were really good at computing, you could bend the rules to your will")
    print("")
    goBack = input("Press enter to return to the turn menu: ")

def solutionCardSelection():
    possibleKillers = ["Cameron Morris", "Sam Forrester", "Archie Waldron",
                       "Matthew Fearnley", "Amber Languille", "Nathan Hopper"]
    killer = random.choice(possibleKillers)
    possibleLocations = ["Lobby", "Dining Room", "Living Room", "Master Bedroom",
                         "Kitchen", "Library", "Attic", "Basement", "Home Theatre",
                         "Bathroom",]
    murderLocation = random.choice(possibleLocations)
    possibleWeapons = ["Revolver", "Knife", "Rope", "Poison", "Baseball Bat",
                       "Statue", "Hammer", "Cheese Grater"]
    murderWeapon = random.choice(possibleWeapons)
    print("")
    print("=============================")
    print("Single-Player Game")
    print("=============================")
    print("")
    print("The Killer has been selected")
    time.sleep(1)
    print("")
    print("The Murder Location has been selected")
    time.sleep(1)
    print("")
    print("The Murder Weapon has been selected")
    time.sleep(1.5)
    return killer, murderLocation, murderWeapon

def viewPlayerCards(playerCards):
    print("")
    print("Your dealt cards are: \n")
    for i in range(0,len(playerCards)):
        print(playerCards[i])
    print("")
    goBack = input("Press enter to return to the turn menu: ")

def viewSuspectList():
    print("")
    print("Insert cleverly-written code here")
    print("")
    goBack = input("Press enter to return to the turn menu: ")
      
def actualGame():
    gameLoop = 1
    while gameLoop == 1:
        print("")
        print("\t\t\t******************************************")
        print("\t\t\t*\t\tEvidencedo\t\t *")
        print("\t\t\t******************************************")
        print("\t\t\t* 1.Single-Player Game\t\t\t *")
        print("\t\t\t* 2.Multi-Player Game\t\t\t *")
        print("\t\t\t* 3.Game Rules\t\t\t         *")
        print("\t\t\t* 4.Exit the Program\t\t\t *")
        print("\t\t\t******************************************")
        print("")
        mainMenu = input("Enter your option here: ")
        if not mainMenu in ["1","2","3","4"]:
            print("")
            print("This is not a valid option")
            time.sleep(1)
            os.system("cls")
        if mainMenu == "1":
            os.system("cls")
            gameLoop = 0
            killer, murderLocation, murderWeapon = solutionCardSelection()
            os.system("cls")
            playerAvatar = characterSelection()
            os.system("cls")
            playerCards = playerCardSelection(playerAvatar, killer, murderLocation, murderWeapon)
            playerCards = str(playerCards)
            os.system("cls")
            currentLocation = ("Outside The House")
            turnLoop = 1
            while turnLoop == 1:
                os.system("cls")
                print("")
                print("=============================")
                if playerAvatar == str("Cameron Morris"):
                    print(playerAvatar + "' Turn")
                else:
                    print(playerAvatar + "'s Turn")
                print("=============================")
                print("")
                print("Current Location: " + currentLocation)
                print("")
                print("1. Move to another Room")
                print("2. Take a Guess")
                print("3. Make a Final Accusation")
                print("")
                print("Press C to view your dealt cards")
                print("Press S to view your full suspect list")
                print("")
                playerAction = input("Enter your option here: ").upper()
                if not playerAction in ["1","2","3","C","S"]:
                    print("")
                    print("This is not a valid option")
                    time.sleep(1)
                    os.system("cls")
                    continue
                if playerAction == "1":
                    os.system("cls")
                    turnLoop = 0
                    currentLocation = roomTraversal(currentLocation)
                    turnLoop = 1
                    continue
                if playerAction == "2":
                    os.system("cls")
                    turnLoop = 0
                    playerGuess(currentLocation, killer, murderLocation, murderWeapon)
                    turnLoop = 1
                    continue
                if playerAction == "3":
                    os.system("cls")
                    turnLoop = 0
                    makeFinalAccusation(killer, murderLocation, murderWeapon)
                    turnLoop = 1
                    continue  
                if playerAction == "C":
                    os.system("cls")
                    turnLoop = 0
                    viewPlayerCards(playerCards)
                    turnLoop = 1
                    continue
                if playerAction == "S":
                    os.system("cls")
                    turnLoop = 0
                    viewSuspectList()
                    turnLoop = 1
                    continue

# 1. Fix the makeFinalaccusation function so that it actually works
# 2. Fix the viewSuspectlist function so that it actually works
# 3. Move the actualGame function to the top of the screen so that my OCD doesn't kill me
# 4. Might want to write the rules at some point, could be helpful
# 5. Go to the Winchester, have a nice cold pint, and wait for all this to blow over

        if mainMenu == "2":
            gameLoop = 0
            os.system("cls")
            print("")
            print("=============================")
            print("Multi-Player Game")
            print("=============================")
            print("")
            print("Like you have friends")
            time.sleep(2)
            
        if mainMenu == "3":
            gameLoop = 0
            os.system("cls")
            rules()
            gameLoop = 1
            os.system("cls")
            
        if mainMenu == "4":
            gameLoop = 0
            os.system("cls")
            print("")
            killCode = input("Press enter to quit the program: ")

actualGame()
