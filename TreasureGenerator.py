from MyUtilities import dieRoller
import random

# lists of stuff
treasureAttribute = [
    'Power',
    'Greatness',
    'Badassery',
    'the Internet',
    'Silliness',
    'Strength',
    'Vitality',
    'Vile Darkness',
    'Things and Stuff',
    'Madness',
    'Positive Vibes',
    'Rainbows'
]

treasureObject = [
    'Amulet',
    'Staff',
    'Ring',
    'Necklace',
    'Token',
    'Badge',
    'Cape',
    'Sandals',
    'Loincloth',
    'Crown',
    'Goblet',
    'Book'
]
minorSetup = [
    'You find ',
    'You meet ',
    'You are discovered by '
    'You come upon '
]
minorNoun = [
    'a Dragon',
    'a Monk',
    'another lost soul',
    'a swarm of rats',
    'an Elven archer',
    'a wise old warrior',
    'an ancient spirit'
]


def genTreasure(board, treasureList, timesToRun):
    width = len(board[0])
    height = len(board)

    while timesToRun != 0:
        object = random.choice(treasureObject)
        attribute = random.choice(treasureAttribute)
        name = str(object) + ' of ' + str(attribute)

        row, col = placeTreasure(width, height, name, treasureList)
        # board[row][col] = "X" # Uncomment to cheat.
        timesToRun -= 1


def placeTreasure(width, height, treasureName, treasureList):
    # Generate coordinates somewhere within board limits.
    # Then add it to the list of treasures.
    repeat = True
    while repeat:
        repeat = False
        row = random.randrange(0, height)
        col = random.randrange(0, width)

        # Check against existing treasures (booty) for duplicate locations.
        for booty in treasureList:
            if booty['x'] == col and booty['y'] == row:
                repeat = True
            # else:
                # continue

    treasureList.append({
        'name': treasureName,
        'x': col,
        'y': row
    })
    return row, col

    for booty in treasureList:
        if booty['x'] == playX and booty['y'] == playY:
            addToTreasuresFound(booty['name'], player)
            treasureList.remove(booty)
            genTreasure(board, treasureList, 1)


def minorTreasure(player):
    # Determine minor treasure type and value with random rolls.
    # Then, display a message from the setup and noun lists.
    # Finally, add the values to the player dictionary.
    type = random.choice(["Health", "Attack", "Defense"])
    if type == 'health':
        treasureValue = sum(dieRoller(2, 4))
    else:
        treasureValue = dieRoller(1, 4)[0]

    print(str(random.choice(minorSetup)) + str(random.choice(minorNoun)) + '.')

    print("+" + str(treasureValue) + " " + str(type))
    applyTreasureStats(type, treasureValue, player)


def applyTreasureStats(key, value, player):
    # Add the rolled stats from a minor treasure to the player dictionary.
    player[key] += value


def majorTreasure():
    print()


def rollMinorOrCombat(player):
    # Roll to see if the player gets a treasure or combat.
    # On a six, get treasure. On a one, enter combat.
    value = dieRoller(1, 6)[0]
    print("Minor Treasure roll: " + str(value))

    return value


    print("You have found the " + str(treasure) + ".")
    player["treasuresFound"].append(treasure)
