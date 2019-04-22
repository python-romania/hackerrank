# This program read and write the content of the file named presidents.txt

def main():
    # Open the file named presidents.txt
    infile = open("presidents.txt", "r")
    # Read the content
    file_contents = infile.read()
    # Close the content
    infile.close()
    # Print the read data
    print(file_contents)
# Call the main function
main()
