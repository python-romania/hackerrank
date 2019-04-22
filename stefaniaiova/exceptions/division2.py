# The program divide a number to another
def main():
    # Take two number
    number1 = int(input("Insert a number: "))
    number2 = int(input("Insert another number: "))
    # If the second number is diffrent from 0, divide one to another and print the result
    if number2 != 0:
        result = number1 / number2
        print(number1, "impartit la ", number2, "este", result)
    else:
        print("The division to 0 is impossible.")
# Call the main function
main()