def solve(s_):
    pattern = []
    for ms in s_.split(" "):
        if ms[0:1].isalpha():
            pattern.append(ms[0:1].upper() + ms[1:len(ms)])
        else:
            pattern.append(ms)
    return " ".join(pattern)

s = str(input())
print(solve(s))
