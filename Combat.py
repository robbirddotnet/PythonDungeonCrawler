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
    # Create an enemy to fight, based on player level.
    enemy = generateCharacter(player["level"])
    enemy["name"] = random.choice(enemyNameList)
    return enemy


def pressEnter():
    input("Press Enter to continue.")


def combatIntro(enemy):
    print(str(enemy["name"]) + " approaches! Prepare for combat.\n")

    input("Press Enter to continue.")


def attackRoll(bonus):
    return dieRoller(1, 20)[0] + bonus


def calcDamage(attack, defense):
    # Determine the damage by adding attack bonus and subtracting target's defense.
    # If the damage goes below zero, set it to zero.
    # print("Calcuating damage.")
    # print("attack: " + str(attack), end='\t')
    # print("defense: " + str(defense), end='\t')
    damage = attack - defense - 10
    # print("damage: " + str(damage))
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


def calcBonus(entity, type):
    return math.floor(entity[type] / 5)


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


def displayCombatStats(player, enemy):
    # print("Your level: " + str(player["level"]))
    print("Your health: " + str(player["Health"]))
    print(str(enemy["name"]) + " health: " + str(enemy["Health"]))


def showCombatInstructions():
    string = """\n1. Normal Attack
2. Quick attack
3. Power attack
4. Counter attack"""
    print(string)


def combatLoop(player, enemy):
    # Ask for player's attack type, then execute it.
    # Continue until the player or enemy are dead.
    playerMaxHP = player["Health"]
    clearScreen()
    combatIntro(enemy)

    while player["Health"] > 0 and enemy["Health"] > 0:
        clearScreen()

        displayCombatStats(player, enemy)
        showCombatInstructions()
        atkType = int(input("Your choice: "))
        enemyAtkMod = 1
        playerDefMod = 1
        clearScreen()
        if atkType == 1:
            normalAttack(player, enemy)
        elif atkType == 2:
            quickAttack(player, enemy)
        elif atkType == 3:
            powerAttack(player, enemy)
            enemyAtkMod = 1.5
        elif atkType == 4:
            counterAttack(player, enemy)
            playerDefMod = 2
        elif atkType.lower() == 'h' or atkType.lower() == 'help':
            print(help)
        pressEnter()
        clearScreen()
        if checkHealth(enemy):
            playerWon = True
            player["enemiesKilled"].append(enemy["name"])
            break

        enemyAttack(player, enemy, enemyAtkMod, playerDefMod)
        if checkHealth(player):
            playerWon = False
            break
        pressEnter()

    clearScreen()
    if playerWon:
        exp = 1
        print(str(enemy["name"]) + " defeated!\n")
        print(str(exp) + " exp gained.")
        print("Health restored.")
        player["Health"] = playerMaxHP

        player["exp"] += 1

        if player["exp"] >= 3:
            player["exp"] = 0
            player["level"] += 1
            print("\nYou are now level " + str(player["level"]))

    elif not playerWon:
        print("You have died!\n")
        print("Game over!")

    input("\nPress Enter to continue.")
    return playerWon
