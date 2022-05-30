from collections import deque
from sys import  stdin


input = stdin.readline


n, k = map(int, input().split())
q = deque([k])  # k부터 시작
path = {k: -1}
while q:
    for _ in range(len(q)):
        x = q.popleft()
        if x == n:
            break
        if x % 2 == 0 and 0 <= x // 2 <= 100000 and x // 2 not in path:
            q.append(x // 2)
            path[x // 2] = x
        if 0 <= x + 1 <= 100000 and x + 1 not in path:
            q.append(x + 1)
            path[x + 1] = x
        if 0 <= x - 1 <= 100000 and x - 1 not in path:
            q.append(x - 1)
            path[x - 1] = x
route = [n]
while n in path and path[n] != -1:
    route.append(path[n])
    n = path[n]
print(len(route) - 1)
print(*route)
