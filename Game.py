from MyUtilities import dieRoller, targetRoller


def main():
    while True:

        quantity = int(input('How many times to roll (0 to quit): '))

        if quantity == 0:
            quit()

        sides = int(input('Sides per die: '))

        if sides <= 1:
            print('Cannot have a one-sided die.')
            continue

        target = int(input('Target to beat: '))

        rolls = dieRoller(quantity, sides)

        print("Your rolls: ")

        for x in rolls:
            print(x, end=' ')

        print()
        if target > 0:
            # rolls = dieRoller(quantity, sides)
            successes = targetRoller(rolls, target)
            print('Number of successes: ' + str(successes))


main()
