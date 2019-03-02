from collections import Counter


group_size =  int(input())
room_numbers = list(input().split())
rooms = Counter(room_numbers)
captains_room = None

print(rooms.most_common()[::-1][0][0])


k = int(input())
arr = list(map(int, input().split()))

myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))
