import math
import logging


class Calculator:

    # is_active if True, application is running
    is_active = True

    @staticmethod
    def add():
        numbers = list(map(float, input('Please enter two numbers to sum, separated by space: ').split()))
        result = (numbers[0] + numbers[1])

        print("Sum of numbers {} + {} = {}".format(numbers[0], numbers[1], result))

        logger.info(f"Please enter two numbers to sum, separated by space: {numbers[0]} and {numbers[1]}")
        logger.info(f"Sum of numbers {numbers[0]} + {numbers[1]} = {result}")

    @staticmethod
    def subtract():
        numbers = list(map(float, input('Please enter two numbers to subtract, separated by space: ').split()))
        result = (numbers[0] - numbers[1])

        print("Sum of numbers {} - {} = {}".format(numbers[0], numbers[1], result))

        logger.info(f"Please enter two numbers to subtract, separated by space: {numbers[0]} and {numbers[1]}")
        logger.info(f"Sum of numbers {numbers[0]} - {numbers[1]} = {result}")

    @staticmethod
    def multiply():
        # Returns: a list of float numbers
        numbers = list(map(float, input('Please enter two numbers to multiply, separated by space: ').split()))
        result = (numbers[0] * numbers[1])

        print("Sum of numbers {} * {} = {}".format(numbers[0], numbers[1], result))

        logger.info(f"Please enter two numbers to multiply, separated by space: {numbers[0]} and {numbers[1]}")
        logger.info(f"Sum of numbers {numbers[0]} * {numbers[1]} = {result}")

    @staticmethod
    def divide():
        # Returns: a list of float numbers
        numbers = list(map(float, input('Please enter two numbers to divide, separated by space: ').split()))
        result = (numbers[0] / numbers[1])

        print("Sum of numbers {} / {} = {}".format(numbers[0], numbers[1], result))

        logger.info(f"Please enter two numbers to divide, separated by space: {numbers[0]} and {numbers[1]}")
        logger.info(f"Sum of numbers {numbers[0]} / {numbers[1]} = {result}")

    def square(self):
        try:
            # Returns: a list of float numbers
            numbers = list(map(float, input('Please enter two numbers to square(power), separated by space: ').split()))
            result = (numbers[0] ** numbers[1])
        except IndexError:
            self.square()

        print("{} at the power of {}  = {}".format(numbers[0], numbers[1], result))

        logger.info(f"Please enter two numbers to square(power), separated by space: {numbers}")
        logger.info(f"{numbers[0]} at the power of {numbers[1]}  = {result}")

    def square_root(self):
        result = None
        number = None
        try:
            # Returns: a float number
            number = float(input('Please enter a number to find the square root: '))
            result = math.sqrt(number)
        except IndexError:
            self.square_root()

        print("Square root of {} = {}".format(number, result))

        logger.info(f"Please enter a number to find the square root: {number}")
        logger.info(f"Square root of {number} = {result}")

    def linear_eq(self):
        # passing variable x in safe dictionary
        expression = input("Enter linear equation with X: ")
        x = int(input("Value of X: "))
        logger.info(f"Enter linear equation with X: {expression}")
        logger.info(f"Value of X: {x}")
        safe_dict['x'] = x
        try:
            # Returns: eval() of first order linear equation
            y = eval(expression, {"__builtins__": None}, safe_dict)
            print("y={}".format(y))
            logger.info(f"y={y}")
        except:
            print('Expression not in safe list.')

    # User is prompted to continue or exit
    def confirm_continue(self):
        confirm = input('Continue? (Y) or Exit(X), please enter your choise: (Y or X)').upper()
        if confirm == 'Y':
            logger.info("User is continuing due to choice of Continue.")
            pass
        elif confirm == 'X':
            logger.info("User is exiting due to choice of Exit.")
            self.is_active = False

    def menu(self):
        logger.info("Displaying menu choices for user prompt")
        for (key, item) in menu_items.items():
            print(key, ' - ', item)
            logger.info(f"{key}. {item}")
        selection = int(input('Please select your option: '))
        logger.info(f"User choice: {selection}")

        if selection == 0:
            self.add()
        elif selection == 1:
            self.subtract()
        elif selection == 2:
            self.multiply()
        elif selection == 3:
            self.divide()
        elif selection == 4:
            self.square()
        elif selection == 5:
            self.square_root()
        elif selection == 6:
            self.linear_eq()

        self.confirm_continue()


# Application only runs if ran from calculator.py
if __name__ == "__main__":
    """
    Configuring logger for activity log.
    """
    logging.basicConfig(filename="calculator_log.txt", filemode="w", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", datefmt='%d-%b-%y %H:%M:%S')
    logger = logging.getLogger(__name__)

    # list of safe methods
    # otherwise malicious code could be entered
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                 'tan', 'tanh']

    # A dictionary of menu items for the user to chose from
    menu_items = {0: 'Add two numbers', 1: 'Subtract two numbers',
                  2: 'Multiply two numbers', 3: 'Divide two numbers',
                  4: 'Square', 5: 'Square root', 6: 'First order linear differential equation'}

    # creating a dictionary of safe methods
    safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])
    calculator = Calculator()

    # while is_active = True, the application is running
    # otherwise, application quits
    while calculator.is_active:
        calculator.menu()

