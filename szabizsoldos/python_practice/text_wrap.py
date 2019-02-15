import textwrap

def wrap(string, max_width):
    s_ = "\n".join(textwrap.wrap(string, max_width))
    return s_

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
