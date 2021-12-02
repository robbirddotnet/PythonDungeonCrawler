from MyUtilities import dieRoller, clearScreen
from PlayerGenerator import generateCharacter


def createEnemy(player):
    enemy = generateCharacter(player["level"])
    return enemy
