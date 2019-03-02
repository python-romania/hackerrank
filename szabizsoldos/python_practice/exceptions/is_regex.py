import re

T = int(input())

for i in range(T):
    is_valid = None
    try:
        re.compile(input())
        is_valid = True
    except re.error:
        is_valid = False

    print(is_valid)
