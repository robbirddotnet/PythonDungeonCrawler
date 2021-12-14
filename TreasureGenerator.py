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

def rollMinorOrCombat(player):
    # Roll to see if the player gets a treasure or combat.
    # On a six, get treasure. On a one, enter combat.
    value = dieRoller(1, 6)[0]
    print("Minor Treasure roll: " + str(value))

    return value


