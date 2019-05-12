""" Create a calculator that is able to do the mathematic operations: addition, subtraction, multiplication, division,
square, square root.
    The calculator also has to be able to solve Linear equations 1!
    The program needs to be user interactive, so you have to create a menu with multiple choices for the user and give
the user oportunity to continue and exit at his choice!
    Every user's choice, input and result will be written in a text file from disk!"""


# Define a function that calculate the sum of two numbers
def add_two_numbers(a, b):
    # Return the result
    return a + b


# Define a function that calculate the subtract of two numbers
def subtract_two_numbers(a, b):
    # Return the result
    return a - b


# Define a function that calculate the multiplication of two numbers
def multiplication(a, b):
    # Return the result
    return a * b


# Define a function that calculate the division of two numbers
def division(a, b):
    # Return the result
    return a / b


# Define a function that calculate the square of a number
def square(a, b):
    # Return the result
    return a ** b


# Define a function that calculate the square_root of a number
def square_root(a):
    # Return the result
    return a ** 0.5


# Define a function that calculate the linear equation
def eq_1(values):
    # Get the first element of the linear equation
    a = values[0]
    # Get the second element of the linear equation
    b = values[1]
    # Define the third element of the linear equation
    c = values[2]
    # Use the format function to print the general form of the linear equation
    step1 = "{}x + {} = {}".format(int(a), int(b), int(c))
    # Use the format function to solve the second step of resolving the eqation
    step2 = "{}x = {} - {}".format(int(a), int(c), int(b))
    # Use the format function to solve the third step of resolving the equation
    step3 = "x = ({} - {}) / {}".format(int(c), int(b), int(a))
    # Use the format function to find the value of x
    step4 = "x = {}".format((c - b) / a)
    # Return the formatted result and the formatted steps
    return "{}\n{}\n{}\n{}\n".format(step1, step2, step3, step4)


# Menu:
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
print("5. Square")
print("6. Square_root")
print("7. Linear equation 1")
print("8. Bye!")


# Define a function who creat a text file
def main():
    # Open a text file named "calculator" in append mode
    outfile = open("calculator.txt", "a")
    # Write in the text file the name of menu
    outfile.write("Menu of operations:\n")
    # Write in the text file the options that user has
    outfile.write("1. Addition\n")
    outfile.write("2. Subtract\n")
    outfile.write("3. Multiply\n")
    outfile.write("4. Division\n")
    outfile.write("5. Square\n")
    outfile.write("6. Square_root\n")
    outfile.write("7. Linear equation 1\n")
    outfile.write("8. Bye!\n")
    # Close the program
    outfile.close()


# Call the main function
main()

# Start an infinite loop while
while True:
    # Define a variable where the user can make his chioce: what operation he wants
    user_input_helper_text = "Insert your choice: "
    # Get a variable with the user input
    user_input = input(user_input_helper_text)
    # Use the if declaration for the first choice of the user
    if user_input == "1":
        # Define a variable which indicates user's choice
        user_choice = "You choose addition operation."
        # Print the variable user_choice
        print(user_choice)
        # Define a variable that has a string as a value
        number1_helper_text = "Insert the first number: "
        # Get input from user and convert to integer
        number1 = int(input(number1_helper_text))
        # Define a variable that has a string as a value
        number2_helper_text = "Insert the second number: "
        # Get input from user and convert to integer
        number2 = int(input(number2_helper_text))
        # Define a variable who calculate the sum of two numbers
        numbers_sum = number1 + number2
        # Print the result
        print(numbers_sum)

        # Open text file
        with open("calculator.txt", "a") as txt_file:
            # Write in the file the content of user choice in the text file
            txt_file.write(user_input_helper_text + user_input + "\n")
            # Write in the file what operation was choosen by user
            txt_file.write(user_choice + "\n")
            # Write in the file the first number insert by user
            txt_file.write(number1_helper_text + str(number1) + "\n")
            # Write in the file the second number insert by user
            txt_file.write(number2_helper_text + str(number2) + "\n")
            # Write in the file the sum of those numbers
            txt_file.write(str(numbers_sum) + "\n")

    # Use the elif declaration for the second choice of user
    elif user_input == "2":
        # Define  avariable wich indicates user's choice
        user_choice = "You choose subtract operation."
        # Print the variable user_choice
        print(user_choice)
        # Define a variable that has a string as a value
        number1_helper_text = "Insert the first number: "
        # Get input from user and convert to integer
        number1 = int(input(number1_helper_text))
        # Define a variable that has a string as a value
        number2_helper_text = "Insert the second number: "
        # Get input from user and convert into integer
        number2 = int(input(number2_helper_text))
        # Define a variable who calculate the subtract of two numbers
        numbers_subtract = number1 - number2
        # Print the result
        print(numbers_subtract)

        # Open text file
        with open("calculator.txt", "a") as txt_file:
            # Write in the file the content of user choice
            txt_file.write(user_input_helper_text + user_input + "\n")
            # Write in the file what operation was choosen by user
            txt_file.write(user_choice + "\n")
            # Write in the file the first number insert by user
            txt_file.write(number1_helper_text + str(number1) + "\n")
            # Write in the file the second number insert by user
            txt_file.write(number2_helper_text + str(number2) + "\n")
            # Write in the file the result of the subtract of those numbers
            txt_file.write(str(numbers_subtract) + "\n")

    # Use the elif declaration for the third choice of user
    elif user_input == "3":
        # Define a variable which indicates the user's choice
        user_choice = "You choose multiply operation."
        # Print the variable user_choice
        print(user_choice)
        # Define  a variable that has a string as a value
        number1_helper_text = "Insert the first number: "
        # Get input from user and convert into integer
        number1 = int(input(number1_helper_text))
        # Define a variable that has a string as a value
        number2_helper_text = "Insert the second number: "
        # Get input from user and convert into integer
        number2 = int(input(number2_helper_text))
        # Define a variable that calculate the multiplication of two numbers
        numbers_multiply = number1 * number2
        # Print the result
        print(numbers_multiply)

        # Open text file
        with open("calculator.txt", "a") as txt_file:
            # Write in the file the content of user choice
            txt_file.write(user_input_helper_text + user_input + "\n")
            # Write in the file what operation has choosen by user
            txt_file.write((user_choice + "\n"))
            # Write in the file the first number insert by user
            txt_file.write(number1_helper_text + str(number1) + "\n")
            # Write in file the second number insert by user
            txt_file.write(number2_helper_text + str(number2) + "\n")
            # Write in file the result of multiplication of those numbers
            txt_file.write(str(numbers_multiply) + "\n")

    # Use the elif declaration for the fourth choice of user
    elif user_input == "4":
        # Define a variable which indicates the user's choice
        user_choice = "You choose division operation."
        # Print the variable user_choice
        print(user_choice)
        # Define a variable that has a string as a value
        number1_helper_text = "Insert first number: "
        # Get input from user and convert into integer
        number1 = int(input(number1_helper_text))
        # Define a variable that has a string as a value
        number2_helper_text = "Insert the second number: "
        # Get input from user and convert into integer
        number2 = int(input(number2_helper_text))
        # Define a variable who calculate the divion of two numbers
        numbers_division = number1 / number2
        # Print the result
        print(numbers_division)

        # Open text file
        with open("calculator.txt", "a") as txt_file:
            # Write in the file the content of user choice
            txt_file.write(user_input_helper_text + user_input + "\n")
            # Write in the file what operation was choosen by user
            txt_file.write(user_choice + "\n")
            # Write in the file the first number insert by user
            txt_file.write(number1_helper_text + str(number1) + "\n")
            # Write in the file the second number insert by user
            txt_file.write(number2_helper_text + str(number2) + "\n")
            # Write in the file the result of divion of those numbers
            txt_file.write(str(numbers_division) + "\n")

    # Use the elif declaration for the fifth choice of user
    elif user_input == "5":
        # Define a variable wich indicates the user's choice
        user_choice = "You choose square operation."
        # Print the variable user_choice
        print(user_choice)
        # Define a variable that has a string as a value
        number1_helper_text = "Insert the first number: "
        # Get input from user and convert into integer
        number1 = int(input(number1_helper_text))
        # Define a variable that has a  string as a value
        number2_helper_text = "Insert the second number: "
        # Get input from user and convert into integer
        number2 = int(input(number2_helper_text))
        # Define a variable who calculate the square of a number
        numbers_square = number1 ** number2
        # Print the result
        print(numbers_square)

        # Open text file
        with open("calculator.txt", "a") as txt_file:
            # Write in the file the content of user choice
            txt_file.write(user_input_helper_text + user_input + "\n")
            # Write in the file what operation was choosen by user
            txt_file.write(user_choice + "\n")
            # Write in the file the first number insert by user
            txt_file.write(number1_helper_text + str(number1) + "\n")
            # Write in the file the second number insert by user
            txt_file.write(number2_helper_text + str(number2) + "\n")
            # Write in the file the result of the square of those numbers
            txt_file.write(str(numbers_square) + "\n")

    # Use the elif declaration for the sixth choice of user
    elif user_input == "6":
        # Define a variable which indicates the user's choice
        user_choice = "You choose square_root operation."
        # Print the variable user_choice
        print(user_choice)
        # Define a variable that has a string as a value
        number_helper_text = "Insert a number: "
        # Get input from user and convert into integer
        number = int(input(number_helper_text))
        # Define a variable that calculate the square_root of a number
        number_square_root = number ** 0.5
        # Print the result
        print(number_square_root)

        # Open text file
        with open("calculator.txt", "a") as txt_file:
            # Write in the file the content of the user choice
            txt_file.write(user_input_helper_text + user_input + "\n")
            # Write in the file what operation was choosen by user
            txt_file.write(user_choice + "\n")
            # Write in the file the number insert by user
            txt_file.write(number_helper_text + str(number) + "\n")
            # Write in the file the result of the square_root of that number
            txt_file.write(str(number_square_root) + "\n")

    # Use the elif declaration for the seventh choice of user
    elif user_input == "7":
        user_choice = "You choose the linear equation 1."
        print(user_choice)
        values1_helper_text = "Insert the first value: "
        values1 = int(input(values1_helper_text))
        values2_helper_text = "Insert the second value: "
        values2 = int(input(values2_helper_text))
        values3_helper_text = "Insert the third value: "
        values3 = int(input(values3_helper_text))
        linear_equation_result = eq_1([values1, values2, values3])
        print(linear_equation_result)
        with open("Calculator.txt", "a") as txt_file:
            txt_file.write(user_input_helper_text + user_input + "\n")
            txt_file.write(user_choice + "\n")
            txt_file.write(values1_helper_text + str(values1) + "\n")
            txt_file.write(values2_helper_text + str(values2) + "\n")
            txt_file.write(values3_helper_text + str(values3) + "\n")
            txt_file.write(str(linear_equation_result) + "\n")
    elif user_input == "8":
        with open("calculator.txt", "a") as txt_file:
            bye = "Bye!\n================================================\n"
            print(bye)
            txt_file.write(bye)
        break
    else:
        print("Your choice does not exist into the menu. Please insert an available choice!")

