from collections import deque
from sys import maxsize, stdin

input = stdin.readline

n, m = map(int, input().split())
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

board = [list(map(int, input().split())) for _ in range(n)]


def bfs(board, sx, sy):
    q = deque([(sx, sy, 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[sx][sy] = True
    while q:
        x, y, dist = q.popleft()
        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    return dist + 1
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = True


answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            answer = max(answer, bfs(board, i, j))
print(answer)
