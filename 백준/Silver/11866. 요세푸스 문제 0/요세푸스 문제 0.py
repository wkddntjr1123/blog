from collections import deque
from sys import stdin


input = lambda: stdin.readline().rstrip()

n, k = map(int, input().split())
q = deque([str(i) for i in range(1, n + 1)])
result = []
while q:
    q.rotate(-(k - 1))
    result.append(q.popleft())

print("<" + ", ".join(result) + ">")