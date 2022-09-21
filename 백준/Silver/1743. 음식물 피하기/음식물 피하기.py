from collections import deque
from sys import stdin

input = stdin.readline

n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    r, c = map(lambda x: int(x) - 1, input().split())
    board[r][c] = 1
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(board, visited, sx, sy):
    result = 1
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                result += 1
    return result


answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            answer = max(answer, bfs(board, visited, i, j))

print(answer)
