from collections import deque
from sys import stdin

input = stdin.readline

q = deque([i for i in range(1, int(input()) + 1)])
while q:
    x = q.popleft()
    if len(q) == 0:
        print(x)
        break
    q.append(q.popleft())