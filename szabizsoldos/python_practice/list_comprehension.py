a, b, c, n = (int(input()) for _ in range(4))

# modul clasic
comp_list = []
for x in range(a + 1):
    for y in range(b + 1):
        for z in range(c + 1):
            if x + y + z != n:
                # comp_list.append([x, y, z])
                print([x, y, z])

# modul Python, one liner, acelasi lucru

comp_list = [[x, y, z] for x in range(a + 1) for y in range(b + 1) for z in range(c + 1) if x + y + z != n]
