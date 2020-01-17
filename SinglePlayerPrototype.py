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
        print("5. Andrew Fiendley")
        print("6. Nathan Hopper")
        print("7. James Swann")
        print("")
        characterSelection = input("Select your character: ")
        if not characterSelection in ["1","2","3","4","5","6","7"]:
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
            playerAvatar = ("Andrew Fiendley")
        if characterSelection == "6":
            characterLoop = 0
            playerAvatar = ("Nathan Hopper")
        if characterSelection == "7":
            characterLoop = 0
            playerAvatar = ("James Swann")
        continue
    playerAvatar = str(playerAvatar)
    print("")
    print("You are " + playerAvatar)
    time.sleep(1.5)
    return playerAvatar

#def clientSetup():
    
#def gameCountdown(hostUsername):
    print("")
    print("=============================")
    print(str(hostUsername) + "'s Lobby")
    print("=============================")
    print("")
    print("Game starting in 5 seconds")
    time.sleep(1)
    print("")
    print("Game starting in 4 seconds")
    time.sleep(1)
    print("")
    print("Game starting in 3 seconds")
    time.sleep(1)
    print("")
    print("Game starting in 2 seconds")
    time.sleep(1)
    print("")
    print("Game starting in 1 second")
    time.sleep(1)

#def hostSetup():

def mainMenu():
    print("")
    print("\t\t\t******************************************")
    print("\t\t\t*\t\tClued Up\t\t *")
    print("\t\t\t******************************************")
    print("\t\t\t* 1.Single Player Game\t\t\t *")
    print("\t\t\t* 2.Multiplayer Game\t\t\t *")
    print("\t\t\t* 3.Game Rules\t\t\t         *")
    print("\t\t\t* 4.Exit the Program\t\t\t *")
    print("\t\t\t******************************************")
    print("")

def makeFinalAccusation(killer, murderLocation, murderWeapon):
    finalKillerGuessLoop = 1
    while finalKillerGuessLoop == 1:
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
        print("5. Andrew Fiendley")
        print("6. Nathan Hopper")
        print("7. James Swann")
        print("")
        finalKiller = input("Enter your option here: ")
        if not finalKiller in ["1","2","3","4","5","6","7"]:
            print("")
            print("This is not a valid option")
            time.sleep(1)
            os.system("cls")
        if finalKiller == "1":
            finalKillerGuess = ("Cameron Morris")
            finalKillerGuessLoop = 0
        if finalKiller == "2":
            finalKillerGuess = ("Sam Forrester")
            finalKillerGuessLoop = 0
        if finalKiller == "3":
            finalKillerGuess = ("Archie Waldron")
            finalKillerGuessLoop = 0
        if finalKiller == "4":
            finalKillerGuess = ("Matthew Fearnley")
            finalKillerGuessLoop = 0
        if finalKiller == "5":
            finalKillerGuess = ("Andrew Fiendley")
            finalKillerGuessLoop = 0
        if finalKiller == "6":
            finalKillerGuess = ("Nathan Hopper")
            finalKillerGuessLoop = 0
        if finalKiller == "7":
            finalKillerGuess = ("James Swann")
            finalKillerGuessLoop = 0
    os.system("cls")
    finalLocationGuessLoop = 1
    while finalLocationGuessLoop == 1:
        print("")
        print("=============================")
        print("Final Accusation")
        print("=============================")
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
        print("11. Conservatory")
        print("")
        finalLocation = input("Enter your option here: ")
        if not finalLocation in ["1","2","3","4","5","6","7","8","9","10","11"]:
            print("")
            print("This is not a valid option")
            time.sleep(1)
            os.system("cls")
        if finalLocation == "1":
            finalLocationGuess = ("Lobby")
            finalLocationGuessLoop = 0
        if finalLocation == "2":
            finalLocationGuess = ("Dining Room")
            finalLocationGuessLoop = 0
        if finalLocation == "3":
            finalLocationGuess = ("Living Room")
            finalLocationGuessLoop = 0
        if finalLocation == "4":
            finalLocationGuess = ("Master Bedroom")
            finalLocationGuessLoop = 0
        if finalLocation == "5":
            finalLocationGuess = ("Kitchen")
            finalLocationGuessLoop = 0
        if finalLocation == "6":
            finalLocationGuess = ("Library")
            finalLocationGuessLoop = 0
        if finalLocation == "7":
            finalLocationGuess = ("Attic")
            finalLocationGuessLoop = 0
        if finalLocation == "8":
            finalLocationGuess = ("Basement")
            finalLocationGuessLoop = 0
        if finalLocation == "9":
            finalLocationGuess = ("Home Theatre")
            finalLocationGuessLoop = 0
        if finalLocation == "10":
            finalLocationGuess = ("Bathroom")
            finalLocationGuessLoop = 0
        if finalLocation == "11":
            finalLocationGuess = ("Conservatory")
            finalLocationGuessLoop = 0
    os.system("cls")
    finalWeaponGuessLoop = 1
    while finalWeaponGuessLoop == 1:
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
        print("9. Chainsaw")
        print("")
        finalWeapon = input("Enter your option here: ")
        if not finalWeapon in ["1","2","3","4","5","6","7","8"]:
            print("")
            print("This is not a valid option")
            time.sleep(1)
            os.system("cls")
        if finalWeapon == "1":
            finalWeaponGuess = ("Revolver")
            finalWeaponGuessLoop = 0
        if finalWeapon == "2":
            finalWeaponGuess = ("Knife")
            finalWeaponGuessLoop = 0
        if finalWeapon == "3":
            finalWeaponGuess = ("Rope")
            finalWeaponGuessLoop = 0
        if finalWeapon == "4":
            finalWeaponGuess = ("Poison")
            finalWeaponGuessLoop = 0
        if finalWeapon == "5":
            finalWeaponGuess = ("Baseball Bat")
            finalWeaponGuessLoop = 0
        if finalWeapon == "6":
            finalWeaponGuess = ("Statue")
            finalWeaponGuessLoop = 0
        if finalWeapon == "7":
            finalWeaponGuess = ("Hammer")
            finalWeaponGuessLoop = 0
        if finalWeapon == "8":
            finalWeaponGuess = ("Cheese Grater")
            finalWeaponGuessLoop = 0
        if finalWeapon == "9":
            finalWeaponGuess = ("Chainsaw")
            finalWeaponGuessLoop = 0
    os.system("cls")
    print("")
    print("=============================")
    print("Final Accusation")
    print("=============================")
    print("")
    print("I think it was " + finalKillerGuess)
    print("In the " + finalLocationGuess)
    print("With the " + finalWeaponGuess)
    rightKiller = False
    rightLocation = False
    rightWeapon = False
    time.sleep(3)
    if finalKillerGuess == killer:
        print("")
        print(finalKillerGuess + " is the Killer")
        rightKiller = True
    else:
        print("")
        print(finalKillerGuess + " is not the Killer")
    if finalLocationGuess == murderLocation:
        print("")
        print("The " + finalLocationGuess + " is the Murder Location")
        rightLocation = True
    else:
        print("")
        print("The " + finalLocationGuess + " is not the Murder Location")
    if finalWeaponGuess == murderWeapon:
        print("")
        print("The " + finalWeaponGuess + " is the Murder Weapon")
        rightWeapon = True
    else:
        print("")
        print("The " + finalWeaponGuess + " is not the Murder Weapon")
    if rightKiller and rightLocation and rightWeapon == True:
        print("")
        print("Congratulations! You solved the murder and won the game!")
        print("")
        goBack = input("Press Enter to return to the Main Menu: ")
        time.sleep(1)
        os.system("cls")
    else:
        print("")
        print("You have given an incorrect solution, and lost the game")
        print("")
        goBack = input("Press Enter to return to the Main Menu: ")
        time.sleep(1)
        os.system("cls")
            
def playerCardSelection(playerAvatar, killer, murderLocation, murderWeapon):
    allCards = ["Cameron Morris", "Sam Forrester", "Archie Waldron", "Matthew Fearnley", "Andrew Fiendley",
                "Nathan Hopper", "James Swann" "Lobby", "Dining Room", "Living Room", "Master Bedroom", "Kitchen", "Library",
                "Attic", "Basement", "Home Theatre", "Bathroom", "Conservatory", "Revolver", "Knife", "Rope", "Poison",
                "Baseball Bat", "Statue", "Hammer", "Cheese Grater", "Chainsaw"]
    allCards.remove(killer)
    allCards.remove(murderLocation)
    allCards.remove(murderWeapon)
    playerCards = []
    for i in range(7):
        cardChoice = (random.choice(allCards))
        playerCards.append(cardChoice)
        allCards.remove(cardChoice)
    print("")
    print("=============================")
    if playerAvatar == str("Cameron Morris"):
        print(playerAvatar + "' Cards")
    else:
        print(playerAvatar + "'s Cards")
    print("=============================")
    print("")
    print("Your dealt cards are:")
    print("")
    print(*playerCards, sep = "\n")
    time.sleep(3)
    return playerCards

def playerGuess(currentLocation, killer, murderLocation, murderWeapon, suspectKillers, suspectLocations, suspectWeapons):
    if currentLocation == ("Outside The House"):
            print("")
            print("You must enter the house before you can take a guess")
            time.sleep(2)
            os.system("cls")
    else:
        locationGuess = (currentLocation)
        killerGuessLoop = 1
        while killerGuessLoop == 1:
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
            print("5. Andrew Fiendley")
            print("6. Nathan Hopper")
            print("7. James Swann")
            print("")
            killerChoice = input("Enter your option here: ")
            if not killerChoice in ["1","2","3","4","5","6","7"]:
                print("")
                print("This is not a valid option")
                time.sleep(1)
                os.system("cls")
            if killerChoice == "1":
                killerGuess = ("Cameron Morris")
                killerGuessLoop = 0
            if killerChoice == "2":
                killerGuess = ("Sam Forrester")
                killerGuessLoop = 0
            if killerChoice == "3":
                killerGuess = ("Archie Waldron")
                killerGuessLoop = 0
            if killerChoice == "4":
                killerGuess = ("Matthew Fearnley")
                killerGuessLoop = 0
            if killerChoice == "5":
                killerGuess = ("Andrew Fiendley")
                killerGuessLoop = 0
            if killerChoice == "6":
                killerGuess = ("Nathan Hopper")
                killerGuessLoop = 0
            if killerChoice == "7":
                killerGuess = ("James Swann")
                killerGuessLoop = 0
        os.system("cls")
        weaponGuessLoop = 1
        while weaponGuessLoop == 1:
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
            print("9. Chainsaw")
            print("")
            weaponChoice = input("Enter your option here: ")
            if not weaponChoice in ["1","2","3","4","5","6","7","8","9"]:
                print("")
                print("This is not a valid option")
                time.sleep(1)
                os.system("cls")
            if weaponChoice == "1":
                weaponGuess = ("Revolver")
                weaponGuessLoop = 0
            if weaponChoice == "2":
                weaponGuess = ("Knife")
                weaponGuessLoop = 0
            if weaponChoice == "3":
                weaponGuess = ("Rope")
                weaponGuessLoop = 0
            if weaponChoice == "4":
                weaponGuess = ("Poison")
                weaponGuessLoop = 0
            if weaponChoice == "5":
                weaponGuess = ("Baseball Bat")
                weaponGuessLoop = 0
            if weaponChoice == "6":
                weaponGuess = ("Statue")
                weaponGuessLoop = 0
            if weaponChoice == "7":
                weaponGuess = ("Hammer")
                weaponGuessLoop = 0
            if weaponChoice == "8":
                weaponGuess = ("Cheese Grater")
                weaponGuessLoop = 0
            if weaponChoice == "9":
                weaponGuess = ("Chainsaw")
                weaponGuessLoop = 0
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
        else:
            print("")
            print(killerGuess + " is not the Killer")
            if killerGuess in suspectKillers:
                suspectKillers.append
                suspectKillers.remove(killerGuess)
        if locationGuess == murderLocation:
            print("")
        else:
            print("")
            print("The " + locationGuess + " is not the Murder Location")
            if locationGuess in suspectLocations:
                suspectLocations.append               
                suspectLocations.remove(locationGuess)
        if weaponGuess == murderWeapon:
            print("")
        else:
            print("")
            print("The " + weaponGuess + " is not the Murder Weapon")
            if weaponGuess in suspectWeapons:
                suspectWeapons.append
                suspectWeapons.remove(weaponGuess)
        print("")
        time.sleep(1)
        print("Suspect List has been updated")
        print("")
        time.sleep(1)
        goBack = input("Press Enter to return to the Turn Menu: ")

def playerTypeSelection():
    playerType = 0
    print("")
    print("=============================")
    print("Player Type Selection")
    print("=============================")
    print("")
    print("Please choose whether you would like to be a Host or a Client")
    print("")
    print("1. Host")
    print("2. Client")
    print("")
    playerTypeChoice = input("Enter your option here: ")
    if not playerTypeChoice in {"1","2"}:
        print("")
        print("This is not a valid option")
        time.sleep(1)
        os.system("cls")
    if playerTypeChoice == "1":
        playerType = 1
        print("")
        print("You have selected to play as a Host")
        time.sleep(1)
    if playerTypeChoice == "2":
        playerType = 2
        print("")
        print("You have selected to play as a Client")
        time.sleep(1)
    return playerType
        
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
        print("11. Conservatory")
        print("")
        newRoom = input("Enter your option here: ")
        if not newRoom in ["1","2","3","4","5","6","7","8","9","10","11"]:
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
        if newRoom == "11":
            roomLoop = 0
            currentLocation = ("Conservatory")
    print("")
    print("You are now in the " + currentLocation)
    print("")
    time.sleep(1.5)
    goBack = input("Press Enter to return to the Turn Menu: ")
    return currentLocation

def rules():
    print("")
    print("=============================")
    print("Story")
    print("=============================")
    print("")
    print("It was a dark, dreary stormy night, when the party was being held in the grand Méfiant Manor, when unexpectedly, a most frightening incident occured.")
    print("The wealthy entrepreneur, Mr. Charles Orpse, has been found dead whilst the other guests were partying elsewhere in the manor.")
    print("The task of searching for the killer has now fallen on to you")
    print("Can you solve the crime?")
    time.sleep(3)
    print("")
    goOn = input("Press Enter to continue: ")
    os.system("cls")
    print("")
    print("=============================")
    print("General Rules")
    print("=============================")
    print("")
    print(" - To solve the murder, you must move between the different rooms of the manor in order to make guesses.")
    print(" - On your turn, you will be allowed to guess the identity of the killer, the location where the murder took place, and the murder weapon.")
    print(" - In order to include a specific room in to your guess, you must be in that room")
    print(" - You will be provided with a suspect list in order to aid in your investigation, which will automatically update once guesses are made")
    print(" - Once you think you have solved the case, you must make a Final Accusation to confirm your suspicions")
    print(" - To win the game, you must correctly guess all three aspects of the crime") 
    time.sleep(3)
    print("")
    goOn = input("Press Enter to continue: ")
    os.system("cls")
    print("")
    print("=============================")
    print("Helpful Tips")
    print("=============================")
    print("")
    print(" - To make a choice in a menu, type in the corresponding number or letter, followed by Enter")
    print(" - Once you have begun a Final Accusation, you cannot return to the main game. Be certain you have the correct information beforehand")
    print("")
    goBack = input("Press Enter to return to the Main Menu: ")

def solutionCardSelection():
    possibleKillers = ["Cameron Morris", "Sam Forrester", "Archie Waldron",
                       "Matthew Fearnley", "Andrew Fiendley", "Nathan Hopper", "James Swann"]
    killer = random.choice(possibleKillers)
    possibleLocations = ["Lobby", "Dining Room", "Living Room", "Master Bedroom",
                         "Kitchen", "Library", "Attic", "Basement", "Home Theatre",
                         "Bathroom", "Conservatory"]
    murderLocation = random.choice(possibleLocations)
    possibleWeapons = ["Revolver", "Knife", "Rope", "Poison", "Baseball Bat",
                       "Statue", "Hammer", "Cheese Grater", "Chainsaw"]
    murderWeapon = random.choice(possibleWeapons)
    print("")
    print("=============================")
    print("Single Player Game")
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

def suspectCardsPrep(killer, murderLocation, murderWeapon):
    suspectKillers = ["Cameron Morris", "Sam Forrester", "Archie Waldron",
                       "Matthew Fearnley", "Andrew Fiendley", "Nathan Hopper", "James Swann"]
    suspectLocations = ["Lobby", "Dining Room", "Living Room", "Master Bedroom",
                         "Kitchen", "Library", "Attic", "Basement", "Home Theatre",
                         "Bathroom", "Conservatory"]
    suspectWeapons = ["Revolver", "Knife", "Rope", "Poison", "Baseball Bat",
                       "Statue", "Hammer", "Cheese Grater", "Chainsaw"]
    return suspectKillers, suspectLocations, suspectWeapons
    
def turnMenu(playerAvatar, currentLocation):
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

def viewPlayerCards(playerCards, playerAvatar):
    print("")
    print("=============================")
    if playerAvatar == ("Cameron Morris"):
        print(str(playerAvatar) + "' Cards")
    else:
        print(str(playerAvatar) + "'s Cards")
    print("=============================")
    print("")
    print("Your dealt cards are:")
    print("")
    print(*playerCards, sep = "\n")
    print("")
    goBack = input("Press Enter to return to the Turn Menu: ")
    
def viewSuspectList(suspectKillers, suspectLocations, suspectWeapons):
    print("")
    print("=============================")
    print("Suspect List")
    print("=============================")
    print("")
    print("Suspected Killers:")
    print(*suspectKillers, sep = "\n")
    print("")
    print("Suspected Locations:")
    print(*suspectLocations, sep = "\n")
    print("")
    print("Suspected Weapons:")
    print(*suspectWeapons, sep = "\n")
    print("")
    goBack = input("Press Enter to return to the Turn Menu: ")
      
def actualGame():
    gameLoop = 1
    while gameLoop == 1:
        mainMenu()
        mainMenuChoice = input("Enter your option here: ")
        if not mainMenuChoice in ["1","2","3","4"]:
            print("")
            print("This is not a valid option")
            time.sleep(1)
            os.system("cls")
        if mainMenuChoice == "1":
            os.system("cls")
            gameLoop = 0
            killer, murderLocation, murderWeapon = solutionCardSelection()
            os.system("cls")
            playerAvatar = characterSelection()
            os.system("cls")
            playerCards = playerCardSelection(playerAvatar, killer, murderLocation, murderWeapon)
            os.system("cls")
            suspectKillers, suspectLocations, suspectWeapons = suspectCardsPrep(killer, murderLocation, murderWeapon)
            currentLocation = ("Outside The House")
            turnLoop = 1
            while turnLoop == 1:
                turnMenu(playerAvatar, currentLocation)
                turnMenuChoice = input("Enter your option here: ").upper()
                if not turnMenuChoice in ["1","2","3","C","S"]:
                    print("")
                    print("This is not a valid option")
                    time.sleep(1)
                    os.system("cls")
                    continue
                if turnMenuChoice == "1":
                    os.system("cls")
                    turnLoop = 0
                    currentLocation = roomTraversal(currentLocation)
                    turnLoop = 1
                    continue
                if turnMenuChoice == "2":
                    os.system("cls")
                    turnLoop = 0
                    playerGuess(currentLocation, killer, murderLocation, murderWeapon, suspectKillers, suspectLocations, suspectWeapons)
                    turnLoop = 1
                    continue
                if turnMenuChoice == "3":
                    os.system("cls")
                    turnLoop = 0
                    makeFinalAccusation(killer, murderLocation, murderWeapon)
                    gameLoop = 1
                    continue  
                if turnMenuChoice == "C":
                    os.system("cls")
                    turnLoop = 0
                    viewPlayerCards(playerCards, playerAvatar)
                    turnLoop = 1
                    continue
                if turnMenuChoice == "S":
                    os.system("cls")
                    turnLoop = 0
                    viewSuspectList(suspectKillers, suspectLocations, suspectWeapons)
                    turnLoop = 1
                    continue

        if mainMenuChoice == "2":
            os.system("cls")
            gameLoop = 0
            playerType = playerTypeSelection()
            if playerType == 1:
                os.system("cls")
                hostSetup()
            if playerType == 2:
                os.system("cls")
                clientSetup()
            os.system("cls")
            gameCountdown(hostUsername)
            print("")
            print("The Multiplayer aspect of Clued Up is currently under development")
            print("Updates will be coming soon")
            time.sleep(2)
            print("")
            goBack = input("Press Enter to return to the Main Menu: ")
            gameLoop = 1
            os.system("cls")

# 1. Fix the Game Lobby so that all the clients start at the same time
# 2. Add a function that allows cards to be dealt between all players
# 3. Produce a write-up that will actually be graded and not this
# 4. *Stretch-Bonus* Add multiple language choice features
# 5. Go to the Winchester, have a nice cold pint, and wait for all this to blow over
            
        if mainMenuChoice == "3":
            gameLoop = 0
            os.system("cls")
            rules()
            gameLoop = 1
            os.system("cls")
            
        if mainMenuChoice == "4":
            gameLoop = 0
            os.system("cls")
            print("")
            killCode = input("Press Enter to exit the program: ")

actualGame()
