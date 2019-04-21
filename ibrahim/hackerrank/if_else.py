#!/bin/python3

number_input = int(input())


def check_constraints(number):
    if number in range(1, 101):
        return True
    else:
        return False


def is_it_weird(number):
    if number % 2 is 1:
        print("Weird")
    elif number % 2 is 0 and number in range(2, 6):
        print("Not Weird")
    elif number % 2 is 0 and number in range(6, 21):
        print("Weird")
    elif number % 2 is 0 and check_constraints(number) is True:
        print("Not Weird")


if __name__ == '__main__':
    if check_constraints(number_input) is True:
        is_it_weird(number_input)
    else:
        print("Your number needs to be between 0 and 100. Try again")
        number_input = int(input())
