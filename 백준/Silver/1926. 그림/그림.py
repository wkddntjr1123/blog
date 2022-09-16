from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def process():
    global n, m, board, visited
    pic_num = 0
    max_len = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                max_len = max(max_len, bfs(i, j))
                pic_num += 1
    return pic_num, max_len


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    global n, m, board, visited, dx, dy
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            adj_x, adj_y = x + dx[i], y + dy[i]
            if (
                0 <= adj_x < n
                and 0 <= adj_y < m
                and board[adj_x][adj_y] == 1
                and not visited[adj_x][adj_y]
            ):
                q.append((adj_x, adj_y))
                visited[adj_x][adj_y] = True
    return cnt


num, length = process()
print(num, length, sep="\n")