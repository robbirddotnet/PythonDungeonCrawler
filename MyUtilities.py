import random
import os


def dieRoller(quantityOfDice, numberOfSides):
    allRolls = []

    for x in range(0, quantityOfDice):
        roll = int(random.randint(1, numberOfSides))
        allRolls.append(roll)

    return allRolls


def targetRoller(allRolls, targetNumber):
    numPassed = 0

    for x in allRolls:
        if x >= targetNumber:
            numPassed += 1

    return numPassed


def clearScreen():
    # Clear the user's terminal.
    os.system('clear')
