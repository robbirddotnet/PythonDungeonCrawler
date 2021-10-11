import random


def dieRoller(quantityOfDice, numberOfSides):
    # print('In dieRoller: ')
    # if numberOfSides <= 1:
    #     print('Cannot have one-sided die.')
    #     return 0

    allRolls = []

    for x in range(0, quantityOfDice):
        roll = int(random.randint(1, numberOfSides))
        # print('Roll: ' + str(roll))
        allRolls.append(roll)

    # print('AllRolls: ' + str(allRolls))
    return allRolls


def targetRoller(allRolls, targetNumber):
    # print('in target roller:')

    numPassed = 0

    for x in allRolls:
        # print('x is: ' + str(x))
        if x >= targetNumber:
            numPassed += 1

    # print('num passed : ' + str(numPassed))
    return numPassed
