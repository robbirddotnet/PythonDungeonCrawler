from Character import Character
from MyUtilities import *


def main():
    with term.location(0, term.height - 1):
        print(getattr(term, 'white_on_blue'))
    while True:
        clearScreen()
        you = Character()
        print(str(you))
        response = input('\nDo you like this character? (y/n): ')

        if response.lower() == 'n':
            continue
        elif response.lower() == 'y':
            clearScreen()
            print("Character accepted. Program ending.")
            break


main()
