"""
Assignment 4: Counter

Run using "counter_script.py"
"""
def main():

    print('\nHello! Let\'s all learn how to count together.')
    while True:
        num1 = input("Enter a start value (default 0): ")
        if num1.isnumeric():
            num1 = int(num1)
            break
        if not num1:
            num1 = 0
            break
        print('Sorry invalid input. Try again.')

    while True:
        num2 = input("Enter an end value: ")
        if num2.isnumeric():
            num2 = int(num2)
            break
        print('Sorry invalid input. Try again.')

    if num1 > num2:
        print("We only wanna count upwards - backwards is beyond me." \
        " Please make sure your end value is greater than your start value.")
        exit()

    while True:
        step = input("Enter a step value greater than 0 (default 1): ")
        if step.isnumeric():
            if int(step) == 0:
                step = 1
                break
            step = int(step)
            break
        if not num1:
            step = 1
            break
        print('Sorry invalid input. Try again.')

    counter = num1
    print(f'\nThe numbers are: {counter}', end=' ')
    while True:
        counter += step
        if counter <= num2:
            print(f'{counter}', end=' ')
        else:
            print(' ')
            break

if __name__ == '__main__':
    main()
