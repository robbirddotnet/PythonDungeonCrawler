from PlayerGenerator import generateCharacter
from MyUtilities import clearScreen


def main():
    while True:
        generateCharacter()
        response = input('\nDo you like this character? (y/n): ')

        if response.lower() == 'n':
            clearScreen()
            continue
        elif response.lower() == 'y':
            break


main()
