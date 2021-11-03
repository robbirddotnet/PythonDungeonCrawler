import random
from MyUtilities import dieRoller

names = {
    "first": [
        'Johnny',
        'Jack',
        'Joe',
        'Jill',
        'James',
        'Jerry',
        'Johnson',
        'Jelly',
        'Jenny',
        'Jessica',
        'Jotaro',
        'Jimmy',
        'Jello',
        'Janet',
        'Joseph'
    ],
    "last": [
        'Skydancer',
        'Hexem',
        'Puddles',
        'Bloodrose',
        'Aurelia',
        'Knickers',
        'Darkheart',
        'Venus',
        'Huntsman',
        'Mysterious',
        'Banana',
        'Dallas',
        'Cloud',
        'Amethyst',
        'Orlando',
        'Caboose',
        'Morningstar',
        'Littlepaws',
        'Dakota',
        'Tater',
        'Ravenhurst',
        'Blackwood',
        'Mercury',
        'Vermillion'
    ]
}

# "You were born _____"
birthplace = [
    'in an alley',
    'behind a dumpster',
    'on top of a mountain',
    'in the middle of the ocean',
    'in a bar',
    'in a forrest',
    'on the moon',
    'at home',
    'on a sinking ship',
    'under a shooting star',
    'in a labratory',
    'in a field',
    'in a cave',
    'in a prison'
]

background = [
    'You are a barbarian. When angry you lose control of your body and kill everything in sight.',
    'You became a bard after picking up and instrument and realizing you could play it.',
    'You became a cleric after an unmistakable sign convinced you to devote yourself to the divine.',
    'You have always had an affinity for animals, and so became a druid.',
    'You became a fighter after joining the army.',
    'After studying at a secluded monastery for years you became a monk.',
    'You became a paladin after a holy being called upon you to undertake a quest.',
    'After losing your way in the forest you learned to become a ranger.',
    'You\'re a quick-witted and nimble theif. Most would refer to you as a rogue.',
    'As a child you managed to set fire to things with your mind. Later you became a scorcerer.',
    'You became a warlock after making a pact with a horrifying being.',
    'After years of study you mastered the art of magic to become a wizard.'
]

silly = [
    'You smell funny.',
    'Under a full moon you turn into a potato.',
    'You are unable to jump.',
    'No one can spell your name correctly.',
    'People forget you within minutes.',
    'Rumors say you are weak to pickles.',
    'You were once caught by pirates after sleeping in a barrel.',
    'Everyone forgets your birthday.'
]


def generateCharacter(level):
    # Assemble a character backstory by randomly choosing from the above lists
    player = {}

    player["name"] = str(random.choice(
        names["first"])) + ' ' + str(random.choice(names["last"]))
    characterBirthplace = "You were born {birthplace}.".format(
        birthplace=str(random.choice(birthplace)))
    characterBackground = str(random.choice(background))
    characterSilly = str(random.choice(silly))

    attackValue = int(sum(dieRoller(3, 6)) + sum(dieRoller(level, 4)))
    defenseValue = int(sum(dieRoller(3, 6)) + sum(dieRoller(level, 4)))
    healthValue = int(sum(dieRoller(5, 6)) + sum(dieRoller(level, 4)))

    player.update({
        "history":  {
            "birthplace": characterBirthplace,
            "background": characterBackground,
            "silly": characterSilly
        },
        "level": level,
        "row": 0,
        "col": 0,
        "Attack": attackValue,
        "Defense": defenseValue,
        "Health": healthValue
    })

    displayHistory(player)

    return player


def displayHistory(player):
    print('Name: {name}'.format(name=player["name"]))
    print("You were born {birthplace}.".format(
        birthplace=player["history"]['birthplace']))
    print(str(player["history"]['background']))
    print(str(player["history"]['silly']))


def displayStats(player):
    print("Level: " + str(player["level"]))
    print("Attack: " + str(player["Attack"]))
    print("Defense: " + str(player["Defense"]))
    print("Health: " + str(player["Health"]))
