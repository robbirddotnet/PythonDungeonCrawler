from MyUtilities import dieRoller
import math
import random


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
# Background details.
# TODO: Write several new entries and remove class based details.
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


class Character:

    def __init__(self, level=1):
        self.level = level
        self.str = Character.genStat()
        self.dex = Character.genStat()
        self.con = Character.genStat()
        self.int = Character.genStat()
        self.wis = Character.genStat()
        self.cha = Character.genStat()
        self.characterClass = ""
        self.health = Character.RollHealth(self)
        self.defense = 10 + Character.statMod(self.con)
        self.attack = 10 + Character.statMod(self.str)  # TODO: separate by class

        # history stuff
        self.name = Character.random_name()
        self.birthplace = Character.random_birthplace()
        self.background = Character.random_background()
        self.silly_detail = Character.random_silly()

    def random_name():
        # create a random name by combining elements from the dictionary of name listsS at the top of the file
        return str(random.choice(names["first"])) + ' ' + str(random.choice(names["last"]))

    def random_birthplace():
        # assign the character a birthplace from the list at the top of the file
        return "You were born {birthplace}.".format(birthplace=str(random.choice(birthplace)))

    def random_background():
        # give the character a background from the list at the top of the file
        return str(random.choice(background))

    def random_silly():
        # give the character a silly detail from the list at the top of the file
        return str(random.choice(silly))

    def RollHealth(character):
        maxRoll = 0
        if character.characterClass == 'Barbarian':
            maxRoll = 12
        elif character.characterClass == 'Wizard':
            maxRoll = 6
        elif character.characterClass == 'Paladin' or character.characterClass == 'Fighter':
            maxRoll = 10
        elif character.characterClass == 'Rogue' or character.characterClass == 'Bard' or character.characterClass == 'Cleric':
            maxRoll = 8

        if character.level == 1:
            healthRoll = maxRoll
        else:
            healthRoll = sum(dieRoller(1, maxRoll))

        return healthRoll + Character.statMod(character.con)

    def genStat():
        # roll 4d6, then drop the lowest number.
        # add the sum and return them.
        rolls = dieRoller(4, 6)
        rolls.sort()
        # print(rolls)
        del rolls[0]
        return sum(rolls)

    def statMod(value):
        mod = math.floor(value / 2 - 5)
        if mod <= 0:
            return 0
        else:
            return mod

