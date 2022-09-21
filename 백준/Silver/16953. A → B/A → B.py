from collections import deque
from sys import maxsize, stdin

input = stdin.readline

n, target = map(int, input().split())
q = deque([n])
visited = set()


def add_one(num):
    return int(str(num) + "1")


dist = 1
while q:
    for _ in range(len(q)):
        cur = q.popleft()
        if cur == target:
            print(dist)
            exit()
        if cur * 2 <= target and cur * 2 not in visited:
            q.append(cur * 2)
            visited.add(cur * 2)
        added_num = add_one(cur)
        if added_num <= target and added_num not in visited:
            q.append(added_num)
            visited.add(added_num)
    dist += 1

print(-1)
