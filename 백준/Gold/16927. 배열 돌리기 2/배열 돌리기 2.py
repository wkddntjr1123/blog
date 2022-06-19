from collections import deque
from functools import reduce
from math import ceil, gcd
from sys import stdin


input = stdin.readline
n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
span = ceil(min(n, m) / 2)


def valid(x, y):
    return 0 <= x < n and 0 <= y < m


def rotate(r):
    for i in range(span):
        q = deque()
        x, y = i, i
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        dir = [-1, 0, 0, 0]
        while valid(x, y) and not visited[x][y]:
            q.append(board[x][y])
            visited[x][y] = True
            dir[0] += 1
            x += 1
        x -= 1
        y += 1
        while valid(x, y) and not visited[x][y]:
            q.append(board[x][y])
            visited[x][y] = True
            dir[1] += 1
            y += 1
        y -= 1
        x -= 1
        while valid(x, y) and not visited[x][y]:
            q.append(board[x][y])
            visited[x][y] = True
            dir[2] += 1
            x -= 1
        x += 1
        y -= 1
        while valid(x, y) and not visited[x][y]:
            q.append(board[x][y])
            visited[x][y] = True
            dir[3] += 1
            y -= 1
        q.rotate((r % len(q)))
        board[x][y] = q.popleft()
        for i, cnt in enumerate(dir):
            for _ in range(cnt):
                x, y = x + dx[i], y + dy[i]
                board[x][y] = q.popleft()


rotate(r)
for line in board:
    print(*line)
