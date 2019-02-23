from collections import Counter


nums, n = list(map(int, input().split())), list(map(int, input().split()))
ncnt = Counter(n)
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0

for i in a:
    if i in ncnt:
        nr = ncnt.get(i)
        happiness += nr
for i in b:
    if i in ncnt:
        nr = ncnt.get(i)
        happiness -= nr

print(happiness)
#
# same as above

n, m = input().split()
sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))
