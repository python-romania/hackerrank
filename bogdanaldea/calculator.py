'''

Create a calculator that is able to do the math operations: addition, subtraction, multiplication, division, square, square root.

The calculator also has to be able to solve Linear equations 1!

The program needs to be user interactive, so you have to create a menu with multiple choices for the user and give the user opportunity to continue and exit at his choice!

Every user's choice, input and result will be written in a text file from disk!

'''


# DISPLAY MENU OPTIONS FOR USER TO CHOOSE
print('''
######      MENU        ####### TOGGLE  ###
#---------------------------#-------------#
#       ADDITION            #      1      #
#       SUBTRACTION         #      2      #
#       DIVISION            #      3      #
#       MULTIPLICATION      #      4      #
#       SQUARE              #      5      # 
#       SQUARE ROOT         #      6      #
#       LINEAR EC-1         #      7      #
#                           #             #  
###########################################
''')


def log_file():

    file_lo_log = open('log.txt', 'w')
    file_lo_log.write('FILE CREATED')
    file_lo_log.close()


log_file()


# DEFINE FUNCTION WHICH TAKES USER'S INPUTS
def user_input():

    while True:
        try:
            number_1 = float(input('FIRST VALUE: '))
            number_2 = float(input('Second VALUE: '))

            with open('log.txt', 'a') as log:
                log.write('\n \nFIRST VALUE: ' + str(number_1))
                log.write('\nSECOND VALUE: ' + str(number_2))

            return number_1, number_2
        except ValueError:
            print('INVALID. TRY AGAIN.')


# DEFINE ADDITION FUNCTION
def add(x, y):
    return x + y


# DEFINE SUBTRACTION FUNCTION
def sub(x, y):
    return x - y


# DEFINE MULTIPLICATION FUNCTION
def multi(x, y):
    return x * y


# DEFINE DIVISION FUNCTION
def div(x, y):
    return x / y


# DEFINE SQUARE ROOT FUNCTION
def square(x, y):
    return x ** y


# DEFINE SQUARE ROOT FUNCTION
def square_root():
    x = float(input('ROOT: '))
    return x ** 0.5


# DEFINE LINEAR EQUATION FUNCTION
def linear_eq():

    print('''
FORMULA: ax + b = c''')

    a = int(input('FIRST VALUE(a): '))
    b = int(input('SECOND VALUE(b): '))
    c = int(input('THIRD VALUE(c): '))

    print(f'{int(a)}x + {int(b)} = {int(c)}')

    equation = (int(c) - int(b)) / int(a)
    return equation


# DEFINE FUNCTION WHICH ASKS USER IF WANT TO CONTINUE OR EXIT
def ask_user_again_or_exit():

    while True:
        try:
            decision = str(input('''
NEXT CALCULATION ( N )
EXIT PROGRAM ( E )
    '''))
            if decision.upper() == 'N':
                calculator()
            elif decision.upper() == 'E':
                print('FINISHED')
                break
        except ValueError:
            print('PRESS REQUIRED BUTTON')


# MAIN FUNCTION
def calculator():

    result = 0
    operation = input('CHOOSE OPERATION: ')
    operation_list = ['ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION', 'SQUARE', 'SQUARE ROOT', 'LINEAR EQUATION 1']

    if operation == '1':
        print(f'YOU SELECTED {operation_list[0]}')
        a, b = user_input()
        result = add(a, b)

        with open('log.txt', 'a') as log:
            log.write('\nOPERATION: ' + str(operation_list[0]))
            log.write('\nRESULT:' + str(result))

    elif operation == '2':
        print(f'YOU SELECTED {operation_list[1]}')
        a, b = user_input()
        result = sub(a, b)

        with open('log.txt', 'a') as log:
            log.write('\nOPERATION: ' + str(operation_list[1]))
            log.write('\nRESULT:' + str(result))

    elif operation == '3':
        print(f'YOU SELECTED {operation_list[2]}')
        a, b = user_input()
        result = multi(a, b)

        with open('log.txt', 'a') as log:
            log.write('\nOPERATION: ' + str(operation_list[2]))
            log.write('\nRESULT:' + str(result))

    elif operation == '4':
        print(f'YOU SELECTED {operation_list[3]}')
        a, b = user_input()
        result = div(a, b)

        with open('log.txt', 'a') as log:
            log.write('\nOPERATION: ' + str(operation_list[3]))
            log.write('\nRESULT:' + str(result))

    elif operation == '5':
        print(f'YOU SELECTED {operation_list[4]}')
        a, b = user_input()
        result = square(a, b)

        with open('log.txt', 'a') as log:
            log.write('\nOPERATION: ' + str(operation_list[4]))
            log.write('\nRESULT:' + str(result))

    elif operation == '6':
        print(f'YOU SELECTED {operation_list[5]}')
        result = square_root()

        with open('log.txt', 'a') as log:
            log.write('\nOPERATION: ' + str(operation_list[5]))
            log.write('\nRESULT:' + str(result))

    elif operation == '7':
        print(f'YOU SELECTED {operation_list[6]}')
        result = linear_eq()

        with open('log.txt', 'a') as log:
            log.write('\nOPERATION: ' + str(operation_list[6]))
            log.write('\nRESULT:' + str(result))

    else:
        print('OPERATION UNAVAILABLE. TRY AGAIN')
        calculator()

    print(f'RESULT: {result}')

    ask_user_again_or_exit()


calculator()

