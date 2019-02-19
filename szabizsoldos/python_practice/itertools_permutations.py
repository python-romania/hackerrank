from itertools import permutations

s = input()
args_ = list(s.split())

comp = ("\n".join("".join(p) for p in sorted(permutations(args_[0], int(args_[1])))))
print(comp)

#
# for p in sorted(permutations(args_[0], int(args_[1]))):
#     print("".join(p))
