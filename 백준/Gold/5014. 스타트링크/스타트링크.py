from collections import deque
from sys import stdin

input = stdin.readline

F, S, G, U, D = map(int, input().split())

q = deque([S])
dist = [-1 for _ in range(F + 1)]
dist[S] = 0

found = False
while q:
    cur = q.popleft()
    if cur == G:
        found = True
        break
    if cur + U <= F and dist[cur + U] == -1:
        q.append(cur + U)
        dist[cur + U] = dist[cur] + 1
    if cur - D >= 1 and dist[cur - D] == -1:
        q.append(cur - D)
        dist[cur - D] = dist[cur] + 1
print(dist[G] if found else "use the stairs")
