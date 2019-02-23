if __name__ == '__main__':
    N = int(input())
    data = []
    commands = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse',]
    for _ in range(N):
        com = input().split()
        if com[0] in commands and len(com) == 3:
            eval("data."+ com[0] + "(" + com[1] + "," + com[2] +")" )
        elif com[0] in commands and len(com) == 2:
            eval("data."+ com[0] + "(" + com[1] + ")")
        elif com[0] == "print":
            print(data)
        else:
            eval("data."+ com[0] + "(" + ")")
