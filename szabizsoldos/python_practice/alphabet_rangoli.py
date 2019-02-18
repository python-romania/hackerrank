# Alphabet Rangoli


def print_rangoli(n_):
    pattern = []
    for i in range(n_):
        s = "-".join(chr(ord('a')+n_-j-1) for j in range(i+1))
        pattern.append([(s+s[::-1][1:]).center((n_*4)-3, '-')])

    for i in range(n_ - 1):
        s = "-".join(chr(ord('a')+n_-j-1) for j in range(n_ - i - 1))
        pattern.append([((s+s[::-1][1:]).center((n_*4)-3, '-'))])

    return pattern


n = int(input())
print("\n".join(str(s[0]) for s in print_rangoli(n)))
