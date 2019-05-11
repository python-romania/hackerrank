"""
Author: Ibrahim Zarifeh

Project Description:
Create a calculator that is able to do the math operations: addition, subtraction, multiplication, division, square,
square root.
The calculator also has to be able to solve Linear equations 1!
The program needs to be user interactive, so you have to create a menu with multiple choices for the user and give the
user opportunity to continue and exit at his choice!
Every user's choice, input and result will be written in a text file from disk!

Created on: 10/05/2019 05:57 AM
"""

import time


def introduction():
    """
    This function will display the list of options available
    :return: Selected option
    """
    option = input("""
Welcome to the Interactive Calculator

Select one of the following options:
1 for Addition
2 for Subtraction
3 for Multiplication
4 for Division
5 for Power
6 for Square root

Selected option is: """)

    return option


def is_option_valid(selected_option):
    """
    This function will check if the selected option is valid
    :param selected_option: The option that the user selected
    :return: True if valid, False if not valid
    """
    possible_options = ['1', '2', '3', '4', '5', '6']

    if selected_option in possible_options:
        return True
    else:
        return False


def get_input():
    """
    This function will ask the user for two numbers
    :return: Two input numbers
    """
    while True:
        try:
            input1 = float(input("First number: "))
            input2 = float(input("Second number: "))

            return input1, input2

        except ValueError:
            print("Your input is not a number. Please try again...")
            continue


def filter_option(selected_option, check_result):
    """
    This function will filter the selected option and it will send the inputs to the correspondent math operation
    :param selected_option: The option selected by the user
    :param check_result: If the option is valid or not
    :return: Selected option, Two input numbers and the result
    """
    result = 0.0

    if check_result is True:

        input1, input2 = get_input()

        if selected_option is '1':
            result = addition(input1, input2)
        elif selected_option is '2':
            result = subtraction(input1, input2)
        elif selected_option is '3':
            result = multiplication(input1, input2)
        elif selected_option is '4':
            result = division(input1, input2)
        elif selected_option is '5':
            result = power(input1, input2)
        elif selected_option is '6':
            input2 = None
            result = square_root(input1)

        return selected_option, input1, input2, result
    else:
        print("You have selected an invalid option. Please try again...")
        main()


def addition(a: float, b: float):
    """
    :param a: First input number
    :param b: Second input number
    :return: The addition between the two numbers
    """
    return a + b


def subtraction(a: float, b: float):
    """
    :param a: First input number
    :param b: Second input number
    :return: The subtraction between the two numbers
    """
    return a - b


def multiplication(a: float, b: float):
    """
    :param a: First input number
    :param b: Second input number
    :return: The multiplication between the two numbers
    """
    return a * b


def division(a: float, b: float):
    """
    :param a: First input number
    :param b: Second input number
    :return: The division between the two numbers
    """
    return a / b


def power(a: float, b: float):
    """
    :param a: First input number
    :param b: Second input number
    :return: The result of the first number power second number
    """
    return pow(a, b)


def square_root(a: float):
    """
    :param a: Input number
    :return: The square root of the input number
    """
    return a ** 0.5


def name_file():
    """
    This function will set the file name
    :return: filename
    """
    return time.strftime("%d-%m-%Y_%I-%M-%S_{}")


def file_content(option, input1, input2, result):
    """
    This function will create the content form which will be saved to file
    :param option: Selected option
    :param input1: First input number
    :param input2: Second input number
    :param result: The math operation result between the two number
    :return:
    """
	
    title = name_file()
	
    if option is '1':
        selected_option = "Addition"
    elif option is '2':
        selected_option = "Subtraction"
    elif option is '3':
        selected_option = "Multiplication"
    elif option is '4':
        selected_option = "Division"
    elif option is '5':
        selected_option = "Power"
    elif option is '6':
        selected_option = "Square root"

    content = """
    ## {4} ##
    # Math operation: {0} #
    # First number: {1}   #
    # Second Number: {2}  #
    # Result: {3}         #
    #######################
    """.format(selected_option, input1, input2, result, title)

    return content


def write_to_file(filename, content_structure):
    """
    This function will create and write to the file
    :param filename: The file name that the file will have
    :param content_structure: The content that will be saved to the file
    """
    f = open(filename, "a+")
    f.write(content_structure)
    f.close()


def want_user_to_continue():
    """
    This function will allow the user to re-run the script or exit
    """
    while True:
        decision = input("Do you wish to use the calculator again [y/n]:")
        decision = decision.lower()
        possible_decision = ['y', 'n']

        if decision in possible_decision:
            if 'y' in decision:
                main()
            elif 'n' in decision:
                print("Thanks for using the Interactive Calculator!")
                print("See you soon. Bye bye :D")
                exit()
        else:
            print("Please type 'y' to use the calculator again or 'n' to exit!")
            continue


def main():
    """
    This function contains all the functions which will be called by the main loop
    """
    option = introduction()
    check_option = is_option_valid(option)

    selected_option, input1, input2, result = filter_option(option, check_option)  # Why printing the option

    print("Result: " + str(result))

    filename = "Log.txt"

    content = file_content(selected_option, input1, input2, result)

    write_to_file(filename, content)

    want_user_to_continue()


if __name__ == '__main__':
    open("Log.txt", "w")
    main()
