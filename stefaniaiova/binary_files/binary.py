def main():
    str = "Hello"
    file = open("binary_file.bin", "wb")
    file.write(str.encode("utf - 8"))
    file.close()
    file = open("binary_file.bin", "rb")
    file_content = file.read()
    file.close()
    print("The content of the file is: ")
    print(file_content.decode("utf - 8"))
main()