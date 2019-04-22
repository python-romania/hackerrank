# This program demonstrates how to copy a file
def main():
    # Open the file named men.txt
    file = open("men.txt", "r")
    
    lines = file.read()
    file.close()
    copy = open("copymen.txt", "w")
    copy.write(lines)
    copy.close()
    print("The copy of the file was made.")
    copy = open("copymen.txt", "r")
    lines = copy.read()
    print(lines)
    copy.close()
main()