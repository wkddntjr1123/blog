from collections import deque
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def bfs(x, y):
    global n, m, board, visited
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    level = 0
    while q:
        level += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == n - 1 and y == m - 1:
                return level
            for i in range(4):
                adj_x, adj_y = x + dx[i], y + dy[i]
                if (
                    0 <= adj_x < n
                    and 0 <= adj_y < m
                    and not visited[adj_x][adj_y]
                    and board[adj_x][adj_y] == 1
                ):
                    q.append((adj_x, adj_y))
                    visited[adj_x][adj_y] = True

print(bfs(0, 0))
