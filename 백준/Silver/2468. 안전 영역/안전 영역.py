from collections import deque
from sys import stdin

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_height = max(map(max, board))


def bfs(x, y, visited, k):
    visited[x][y] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > k and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


res = 1
for k in range(1, max_height):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > k and not visited[i][j]:
                bfs(i, j, visited, k)
                cnt += 1
    res = max(res, cnt)

print(res)
