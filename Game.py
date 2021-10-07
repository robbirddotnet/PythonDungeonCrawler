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


while True:

    quantity = int(input('How many times to roll (0 to quit): '))

    if quantity == 0:
        quit()

    sides = int(input('Sides per die: '))

    if sides <= 1:
        print('Cannot have a one-sided die.')
        continue

    target = int(input('Target to beat: '))

    rolls = dieRoller(quantity, sides)

    print("Your rolls: ")

    for x in rolls:
        print(x, end=' ')

    print()
    if target > 0:
        # rolls = dieRoller(quantity, sides)
        successes = targetRoller(rolls, target)
        print('Number of successes: ' + str(successes))
