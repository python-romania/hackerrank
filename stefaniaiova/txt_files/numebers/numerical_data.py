# The program demonstrates that numbers must be converted into strings before they are written in text txt_files

def main():
    # Open a file for writing
    outfile = open("numbers.txt", "w")
    # Ia trei numere de la user
    num1 = int(input("insert a number: "))
    num2 = int(input("insert the second number: "))
    num3 = int(input("insert the third number: "))
    # Write the three numbers in file
    outfile.write(str(num1) + "\n")
    outfile.write(str(num2) + "\n")
    outfile.write(str(num3) + "\n")
    # Close the file
    outfile.close()
    print("Data written in numbers.txt")
# Call the main function
main()