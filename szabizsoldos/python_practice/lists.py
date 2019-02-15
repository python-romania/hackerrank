n = int(input())  # number of commands


def play():
    lst = []
    for i in range(1, n+1):
        inpt = list(input().split())
        cmd = inpt[0]

        if cmd == 'insert':
            lst.insert(int(inpt[1]), int(inpt[2]))
        elif cmd == 'print':
            print(lst)
        elif cmd == 'remove':
            lst.remove(int(inpt[1]))  # be aware to add int(), otherwise weird not found (x) error
        elif cmd == 'append':
            lst.append(int(inpt[1]))
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()
        else:
            lst.clear()


play()
