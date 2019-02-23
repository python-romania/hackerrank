if __name__ == '__main__':
    s = 'qA2'
    if 0 < len(s) < 1000:
        alphanumeric = any([c.isalnum() for c in s])
        alphabetic = any([c.isalpha() for c in s])
        hasdigits = any([c.isdigit() for c in s])
        lowercase = any([c.islower() for c in s])
        uppercase = any([c.isupper() for c in s])

        print(alphanumeric)
        print(alphabetic)
        print(hasdigits)
        print(lowercase)
        print(uppercase)

