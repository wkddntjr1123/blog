from collections import defaultdict, deque
from sys import maxsize, stdin

input = stdin.readline

n = int(input())
q = deque([n])
dist = [-1 for _ in range(n + 1)]
dist[n] = 0
while q:
    cur = q.popleft()
    if cur == 1:
        print(dist[cur])
        exit()
    if cur % 2 == 0 and dist[cur // 2] == -1:
        q.append(cur // 2)
        dist[cur // 2] = dist[cur] + 1
    if cur % 3 == 0 and dist[cur // 3] == -1:
        q.append(cur // 3)
        dist[cur // 3] = dist[cur] + 1
    if dist[cur - 1] == -1:
        q.append(cur - 1)
        dist[cur - 1] = dist[cur] + 1
