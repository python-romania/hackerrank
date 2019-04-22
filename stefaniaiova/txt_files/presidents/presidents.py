# This program writes three lines of data in a file
def main():
    # Open a file named presidents.txt
    outfile = open("presidents.txt", "w")
    # Write the names of the Romanian presidents in the file
    outfile.write("Ion Iliescu\n")
    outfile.write("Emil Constantinescu\n")
    outfile.write("Traian Basescu\n")
    outfile.write("Klaus Iohannis\n")
    # Close the file
    outfile.close()
# Call the main function
main()