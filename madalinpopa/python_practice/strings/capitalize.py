import re

def solve(s):
    # STEP 1: Capitalize first letter in every word
    names = [i.title() for i in s.split() if i.isalpha()]

    # STEP 2: Compare initial string and replace with names
    for name in names:
        index = s.lower().find(name.lower())
        if index >= 0:
            s = s.replace(s[index:index + len(name)], name)
    return s


s = "1 w 2 r 3g"
print(solve(s))