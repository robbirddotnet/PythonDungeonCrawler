from PlayerGenerator import generateCharacter, displayHistory, displayStats
from MyUtilities import clearScreen


def main():
    while True:
        clearScreen()
        you = generateCharacter(1)
        displayHistory(you)
        print('\n')
        displayStats(you)

        response = input('\nDo you like this character? (y/n): ')

        if response.lower() == 'n':
            continue
        elif response.lower() == 'y':
            break


main()
