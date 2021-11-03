from PlayerGenerator import generateCharacter
from MyUtilities import clearScreen


def main():
    while True:
        clearScreen()
        you = generateCharacter(1)
        response = input('\nDo you like this character? (y/n): ')

        if response.lower() == 'n':
            continue
        elif response.lower() == 'y':
            break


main()
