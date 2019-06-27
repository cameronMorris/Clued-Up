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
            playerCharacter = ("Cameron Morris")
        if characterSelection == "2":
            characterLoop = 0
            playerCharacter = ("Sam Forrester")
        if characterSelection == "3":
            characterLoop = 0
            playerCharacter = ("Archie Waldron")
        if characterSelection == "4":
            characterLoop = 0
            playerCharacter = ("Matthew Fearnley")
        if characterSelection == "5":
            characterLoop = 0
            playerCharacter = ("Amber Languille")
        if characterSelection == "6":
            characterLoop = 0
            playerCharacter = ("Nathan Hopper")
        continue       
    print("")
    print("You are " + playerCharacter)
    time.sleep(1.5)
    return playerCharacter

def makeFinalaccusation():
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
    if finalKiler == "1":
        finalKillerguess = ("Cameron Morris")
    if finalKiller == "2":
        finalKillerguess = ("Sam Forrester")
    if finalKiller == "3":
        finalKillerguess = ("Archie Waldron")
    if finalKiller == "4":
        finalKillerguess = ("Matthew Fearnley")
    if finalKiller == "5":
        finalKillerguess = ("Amber Languille")
    if finalKiller == "6":
        finalKillerguess = ("Nathan Hopper")
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
    print("I think it was " + finalKillerguess)
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
        finalLocationguess = ("Lobby")
    if finalLocation == "2":
        finalLocationguess = ("Dining Room")
    if finalLocation == "3":
        finalLocationguess = ("Living Room")
    if finalLocation == "4":
        finalLocationguess = ("Master Bedroom")
    if finalLocation == "5":
        finalLocationguess = ("Kitchen")
    if finalLocation == "6":
        finalLocationguess = ("Library")
    if finalLocation == "7":
        finalLocationguess = ("Attic")
    if finalLocation == "8":
        finalLocationguess = ("Basement")
    if finalLocation == "9":
        finalLocationguess = ("Home Theatre")
    if finalLocation == "10":
        finalLocationguess = ("Bathroom")
    os.system("cls")
    print("")
    print("=============================")
    print("Final Accusation")
    print("=============================")
    print("")
    print("I think it was " + finalKillerguess)
    print("In the " + finalLocationguess)
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
        finalWeaponguess = ("Revolver")
    if finalWeapon == "2":
        finalWeaponguess = ("Knife")
    if finalWeapon == "3":
        finalWeaponguess = ("Rope")
    if finalWeapon == "4":
        finalWeaponguess = ("Poison")
    if finalWeapon == "5":
        finalWeaponguess = ("Baseball Bat")
    if finalWeapon == "6":
        finalWeaponguess = ("Statue")
    if finalWeapon == "7":
        finalWeaponguess = ("Hammer")
    if finalWeapon == "8":
        finalWeaponguess = ("Cheese Grater")
    os.system("cls")
    print("")
    print("=============================")
    print("Final Accusation")
    print("=============================")
    print("")
    print("I think it was " + finalKillerguess)
    print("In the " + finalLocationguess)
    print("With the " + finalWeaponguess)
    print("")
    time.sleep(3)
    rightKiller == True
    rightLocation == True
    rightWeapon == True
    if finalKillerguess == killer:
        print("")
        print(finalKillerguess + " is the Killer")
    else:
        print("")
        print(finalKillerguess + " is not the Killer")
        rightKiller == False
    if finalLocationguess == murderLocation:
        print("")
        print("The " + finalLocationguess + " is the Murder Location")
    else:
        print("")
        print("The " + finalLocationguess + " is not the Murder Location")
        rightLocation == False
    if finalWeaponguess == murderWeapon:
        print("")
        print("The " + finalWeaponguess + " is the Murder Weapon")
    else:
        print("")
        print("The " + finalWeaponguess + " is not the Murder Weapon")
        rightWeapon == False
    if rightKiller and rightLocation and rightWeapon == True:
        os.system("cls")
        print("")
        print("=============================")
        print("Final Accusation")
        print("=============================")
        print("")
        print("Congratulations!")
        print("You have figured out the correct solution and won the game!")
        time.sleep(1)
        goBack = input("Press enter to return to the main menu: ")
        time.sleep(1)
        gameLoop = 1
        return
    else:
        print("")
        print("=============================")
        print("Final Accusation")
        print("=============================")
        print("")
        print("You have given an incorrect solution and lost the game")
        time.sleep(1)
        goBack = input("Press enter to return to the main menu: ")
        gameLoop = 1
        return

def playerCardselection(killer, murderLocation, murderWeapon):
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
    print("")
    print("Your dealt cards are: \n")
    for playerCard in playerCards:
        print(playerCard)
    numberOfcards = 7
    time.sleep(3)
    return

def playerGuess():
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
        clearedKiller = killerGuess
    if locationGuess == murderLocation:
        print("")
        print("The " + locationGuess + " is the Murder Location")
    else:
        print("")
        print("The " + locationGuess + " is not the Murder Location")
        clearedLocation = locationGuess 
    if weaponGuess == murderWeapon:
        print("")
        print("The " + weaponGuess + " is the Murder Weapon")
    else:
        print("")
        print("The " + weaponGuess + " is not the Murder Weapon")
        clearedWeapon = weaponGuess
    # This needs to properly update the suspect list
    goBack = input("Press enter to return to the turn menu: ")

def roomTraversal():
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
    return

def rules():
    print("")
    print("If you were really good at computing, you could bend the rules to your will")
    print("")
    goBack = input("Press enter to return to the turn menu: ")
    return

def solutionCardselection():
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

def viewPlayercards(playerCards, numberOfcards):
    print("")
    print("Your dealt cards are: \n")
    for i in range(0,len(playerCards)):
        print(playerCards[i])
    print("")
    goBack = input("Press enter to return to the turn menu: ")
    return

def viewSuspectlist(killerSuspectlist, locationSuspectlist, weaponSuspectlist):
    #not quite sure what's wrong here, but just fix it
    print("")
    print("Possible Killers:")
    for killerSuspectlist in killerSuspectlist:
        print(killerSuspectlist)
    print("")
    print("Possible Locations:")
    for locationSuspectlist in locationSuspectlist:
        print(locationSuspectlist)
    print("")
    print("Possible Weapons:")
    for weaponSuspectlist in weaponSuspectlist:
        print(weaponSuspectlist)
    print("")
    goBack = input("Press enter to return to the turn menu: ")
    return
    
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
            k, ml, mw = solutionCardselection()
            os.system("cls")
            characterSelection()
            os.system("cls")
            pc = playerCardselection(k, ml, mw)
            pc = str(pc)
            os.system("cls")
            currentLocation = ("Outside The House")
            turnLoop = 1
            while turnLoop == 1:
                os.system("cls")
                print("")
                print("=============================")
                if pc == str("Cameron Morris"):
                    print(pc + "' Turn")
                else:
                    print(pc + "'s Turn")
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
                    roomTraversal()
                    turnLoop = 1
                    continue
                if playerAction == "2":
                    if currentLocation == ("Outside The House"):
                        print("")
                        print("You must enter the house before you can take a guess")
                        time.sleep(2)
                        os.system("cls")
                        continue
                    os.system("cls")
                    turnLoop = 0
                    playerGuess()
                    turnLoop = 1
                    continue
                if playerAction == "3":
                    os.system("cls")
                    turnLoop = 0
                    makeFinalaccusation()
                    turnLoop = 1
                    continue  
                if playerAction == "C":
                    os.system("cls")
                    turnLoop = 0
                    viewPlayercards(playerCards, numberOfcards)
                    turnLoop = 1
                    continue
                if playerAction == "S":
                    os.system("cls")
                    turnLoop = 0
                    viewSuspectlist(killerSuspectlist, locationSuspectlist, weaponSuspectlist)
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
