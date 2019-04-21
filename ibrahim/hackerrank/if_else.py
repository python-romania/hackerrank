#!/bin/python3

N = int(input())

def check_constraints(N):
    if N >=1 and N <= 100:
        return True
    else:
        return False


def is_it_weird(N):
    if N % 2 is 1:
        print("Weird")
    elif N % 2 is 0 and N >= 2 and N <= 5:
        print("Not Weird")
    elif N % 2 is 0 and N >= 6 and N <= 20:
        print("Weird")
    elif N % 2 is 0 and N > 20:
        print("Not Weird")

if check_constraints(N) is True:
    is_it_weird(N)
else:
    print("Your number needs to be between 0 and 100. Try again")
    N = int(input())
