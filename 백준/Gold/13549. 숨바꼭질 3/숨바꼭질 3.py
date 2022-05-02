from collections import deque
from sys import maxsize, stdin

input = stdin.readline

n, k = map(int, input().split())
dist = [maxsize for _ in range(200000 + 1)]
dist[k] = 0
q = deque([k])

while q:
    x = q.popleft()
    if x % 2 == 0 and dist[x // 2] > dist[x]:
        dist[x // 2] = dist[x]
        q.append(x // 2)
    if 0 <= x - 1 and dist[x - 1] > (dist[x] + 1):
        dist[x - 1] = dist[x] + 1
        q.append(x - 1)
    if x + 1 <= 150000 and dist[x + 1] > (dist[x] + 1):
        dist[x + 1] = dist[x] + 1
        q.append(x + 1)
print(dist[n])