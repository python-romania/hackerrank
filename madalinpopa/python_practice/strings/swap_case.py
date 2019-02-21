def swap_case(s):
    output = []
    if 0 < len(s) <= 1000:
        for c in s:
            if c.isalpha() and c.isupper():
                output.append(c.lower())
            elif c.isalpha and c.islower():
                output.append(c.upper())
            else:
                output.append(c)
    return ''.join(output)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
