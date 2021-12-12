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


def printDamage(value, who):
    if value <= 0:
        print(str(who) + " missed!")
    else:
        print(str(who) + " dealt " + str(value) + " damage!")


def powerAttack(player, enemy):
    atk = attackRoll(calcBonus(player, "Attack") * 2)
    dmg = math.floor(calcDamage(atk, calcBonus(enemy, "Defense")))
    enemy["Health"] -= dmg
    printDamage(dmg, player["name"])


def quickAttack(player, enemy):
    atk = attackRoll(calcBonus(player, "Attack") * 2)
    dmg = math.floor(calcDamage(atk, math.floor(
        calcBonus(enemy, "Defense") * 1.5)))
    enemy["Health"] -= dmg
    printDamage(dmg, player["name"])


def normalAttack(player, enemy):
    atk = attackRoll(calcBonus(player, "Attack"))
    dmg = math.floor(calcDamage(atk, math.floor(calcBonus(enemy, "Defense"))))
    enemy["Health"] -= dmg
    printDamage(dmg, player["name"])


def counterAttack(player, enemy):
    atk = attackRoll(0)
    dmg = math.floor(calcDamage(atk, math.floor(calcBonus(enemy, "Defense"))))
    enemy["Health"] -= dmg
    printDamage(dmg, player["name"])


def enemyAttack(player, enemy, atkMod=1, defMod=1):
    atk = attackRoll(calcBonus(enemy, "Attack") * atkMod)
    dmg = math.floor(calcDamage(atk, calcBonus(player, "Defense") * defMod))
    player["Health"] -= dmg
    printDamage(dmg, enemy["name"])

def checkHealth(entity):
    if entity["Health"] <= 0:
        return True
    else:
        return False

def showCombatInstructions():
    string = """\n1. Normal Attack
2. Quick attack
3. Power attack
4. Counter attack"""
    print(string)
