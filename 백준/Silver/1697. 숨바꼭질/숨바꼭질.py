from collections import deque
from sys import stdin

input = stdin.readline
start, target = map(int, input().split())
dist = [-1 for _ in range(100001)]


def bfs():
    global start, target
    if start == target:
        return 0
    q = deque()
    q.append(start)
    dist[start] = 0
    while q:
        for _ in range(len(q)):
            num = q.popleft()

            for val in (num + 1, num * 2, num - 1):
                if val > 100000 or val < 0:
                    continue
                if target in (num - 1, num + 1, num * 2):
                    return dist[num] + 1
                if dist[val] == -1:
                    q.append(val)
                    dist[val] = dist[num] + 1


print(bfs())
