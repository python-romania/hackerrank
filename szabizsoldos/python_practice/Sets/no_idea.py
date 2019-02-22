from collections import Counter


nums, n = list(map(int, str(input()).split())), list(map(int, str(input()).split()))
ncnt = Counter(n)
a = set(map(int, str(input()).split()))
b = set(map(int, str(input()).split()))
happiness = 0

for i in a:
    if i in ncnt:
        nr = ncnt.get(i)
        happiness += nr
for i in b:
    if i in n:
        nr = ncnt.get(i)
        happiness -= nr

print(happiness)

# same as above

n, m = input().split()
sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))
