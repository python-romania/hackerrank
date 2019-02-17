def print_formatted(n_):
    start = int(1)
    wbn = len(bin(n_).replace("0b", ""))
    for r in range(start, n_ + 1):
        new_ = str(r).rjust(wbn, " ") + " " + str(oct(r)[2::].rjust(wbn, " ") + " " + str(hex(r)).replace("0x", "").upper().rjust(wbn, " ") + " " + str(bin(r)).replace("0b", "").rjust(wbn, " "))
        print(new_)


n = int(input())

print_formatted(n)
