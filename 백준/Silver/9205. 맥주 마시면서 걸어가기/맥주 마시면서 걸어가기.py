from collections import deque
from sys import stdin

input = stdin.readline

t = int(input())


def get_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    for i in range(len(stores)):
        stores[i].append(get_dist(stores[i][0], stores[i][1], fx, fy))
    visited = [False for _ in range(n)]
    happy = False
    q = deque([(x, y, get_dist(x, y, fx, fy))])
    while q:
        x, y, rest = q.popleft()
        if rest <= 1000:
            happy = True
            break
        for i in range(len(stores)):
            if visited[i]:
                continue
            nx, ny, to_dest = stores[i]
            if get_dist(x, y, nx, ny) <= 1000:  # 현 위치에서 도달 가능
                q.append((nx, ny, to_dest))
                visited[i] = True
    print("happy" if happy else "sad")