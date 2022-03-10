from collections import deque
from sys import stdin

input = stdin.readline

x = int(input().rstrip())
route = [False for _ in range(x + 1)]


def bfs(num):
    q = deque()
    q.append((num, 0))
    while q:
        num, level = q.popleft()
        if num == 1:
            return level
        if num % 3 == 0 and route[num // 3] == False:
            q.append((num // 3, level + 1))
            route[num // 3] = num
        if num % 2 == 0 and route[num // 2] == False:
            q.append((num // 2, level + 1))
            route[num // 2] = num
        if num - 1 >= 1 and route[num - 1] == False:
            q.append((num - 1, level + 1))
            route[num - 1] = num


min_level = bfs(x)
print(min_level)
start = 1
result = []
while start:
    result.append(start)
    start = route[start]
print(" ".join(map(str, result[::-1])))