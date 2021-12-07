from MyUtilities import dieRoller, clearScreen
import math
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


def calcDamage(attack, defense):
    print("Calcuating damage.")
    print("attack: " + str(attack), end='\t')
    print("defense: " + str(defense), end='\t')

    damage = attack - defense - 10
    print("damage: " + str(damage))

    if damage < 0:
        damage = 0

    return damage


def checkHealth(entity):
    if entity["Health"] <= 0:
        return True
    else:
        return False
