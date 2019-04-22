# This program takes three user names and write them into a tab

def main():
    print("Insert the name of three men.")
    name1 = input("man #1 ")
    name2 = input("man #2 ")
    name3 = input("man #3 ")
    # Open a file named men.txt
    file = open("men.txt", "w")
    # Write the name in file
    file.write(name1 + "\n")
    file.write(name2 + "\n")
    file.write(name3 + "\n")
    my_file = open("men.txt", "a")
    my_file.write("Jhon\n")
    my_file.write("David\n")
    my_file.write("Robert\n")
    # Close the file
    file.close()
# Call the main function
main()