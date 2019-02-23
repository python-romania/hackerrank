def print_formatted(number):
    binaryw = len(bin(number))
    for nr in range(1, number + 1):
        decimal = str(nr).rjust(binaryw, " ")
        octal = str(oct(nr)[2:].rjust(binaryw, " "))
        hexa = str(hex(nr).replace("0x", "").upper().rjust(binaryw, " "))
        binary = str(bin(number).replace("0b", "").rjust(binaryw, " "))
        output = f"{decimal} {octal} {hexa} {binary}"
        print(output)

if __name__ == '__main__':
    # n = int(input())
    print_formatted(2)
