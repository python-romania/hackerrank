# /Create a calculator that is able to do the math operations: addition,
# subtraction, multiplication, division, square, square root.
#?? The calculator also has to be able to solve Linear equations 1!
# The program needs to be user interactive, so you have to create a menu
# with multiple choices for the user and give the user opportunity to continue and exit at his choice!
#?? Every user's choice, input and result will be written in a text file from disk!


# Define function
def calc():
    operations = input('''
    Meniu
    1. Addition
    2. Substraction
    3. Division
    4. Multimplication
    5. Square
    6. Square root
    7. Linear ecuations 1
        ''')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    # Addition
    if operations == '1':
        print('Addition')
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    # Subtraction
    elif operations == '2':
        print('Substraction')
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    # Multiplication
    elif operations == '3':
        print('Multiplication')
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    # Division
    elif operations == '4':
        print('Division')
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    # Square
    elif operations == '5':
        print('Square')
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 / number_2)


    # # Square_root
    # elif operations == '6':
    # print('Square_root')
    #     print('{} ** 0.5 = '.format(number_1)
    #
    #
    #
    # # Linear equations 1
    # elif operations == '7':


    else:
        print('Please type a valid operations! ')
    again()

def again():
    calc_again = input('''
    To calculate again please type Y, to exit type N''')
    if calc_again.upper() == 'Y' :
        calc()
    elif calc_again.upper() == 'N':
        print('See you ! ')
calc()