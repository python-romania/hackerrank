def validate(s_):
    print(any(c.isalnum() for c in s_))
    print(any(c.isalpha() for c in s_))
    print(any(c.isdigit() for c in s_))
    print(any(c.islower() for c in s_))
    print(any(c.isupper() for c in s_))

s = input()
validate(s)
