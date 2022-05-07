from collections import deque
from sys import stdin

input = stdin.readline
m, n = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
board = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    global n, m, board
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append((i, j))
    day = -1
    while q:
        day += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                adj_x, adj_y = x + dx[i], y + dy[i]
                if 0 <= adj_x < n and 0 <= adj_y < m and board[adj_x][adj_y] == 0:
                    q.append((adj_x, adj_y))
                    board[adj_x][adj_y] = 1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return -1
    return day


print(bfs())
