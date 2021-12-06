from MyUtilities import dieRoller, clearScreen
from PlayerGenerator import generateCharacter
import random

enemyNameList = [
    "Orc",
    "Goblin",
    "Barbarian",
    "Gnoll",
    "Elf",
    "Bear",
    "Imp",
    "Zombie",
    "Kobold",
    "Giant Spider",
    "Reptile of Enormous Proportions",
    "Giant Rat",
    "Giant Bat",
    "Internet Troll",
    "Devil",
    "Demon",
    "Evil Genie",
    "Slime",
    "Beholder"
]


def createEnemy(player):
    enemy = generateCharacter(player["level"])
    enemy["name"] = random.choice(enemyNameList)
    return enemy


def combatIntro(enemy):
    print(str(enemy["name"]) + " approaches! Prepare for combat.\n")

    input("Press Enter to continue.")


def attackRoll(bonus):
    return dieRoller(1, 20)[0] + bonus
