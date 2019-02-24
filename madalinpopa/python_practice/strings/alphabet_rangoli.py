def print_rangoli(size):

    # STEP 1: get the letters
    letters = []
    for i in range(size):
        letters.append(chr(ord('a') + i))

    # STEP 2: display alphabet
    pattern = []
    for i in range(size):
        s = "-".join(letters[i:size]) # -a-b-c-d-e
        pattern.append((s[::-1] + s[1:]).center(4*size-3, "-")) # e-d-c-b-a-b-c-d-e

    print("\n".join(i for i in pattern[::-1])) # first half
    print("\n".join(i for i in pattern[1:]))   # second half

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)