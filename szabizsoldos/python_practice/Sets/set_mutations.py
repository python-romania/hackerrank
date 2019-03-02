elms = int(input())
A = set(list(map(int, input().split())))
os = int(input())

for i in range(os):
    raw_cmd = input().split()[0]
    inner_set = set(map(int, input().split()))

    if raw_cmd == 'intersection_update':
        A.intersection_update(inner_set)
    if raw_cmd == 'update':
        A.update(inner_set)
    if raw_cmd == 'symmetric_difference_update':
        A.symmetric_difference_update(inner_set)
    if raw_cmd == 'difference_update':
        A.difference_update(inner_set)

print(sum(A))
