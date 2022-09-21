from collections import deque
from sys import stdin

input = stdin.readline

m, n = map(int, input().split())
board = [input().rstrip() for _ in range(n)]


def bfs(board, target):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    power = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == target and not visited[i][j]:
                count = 0
                q.append((i, j))
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    count += 1
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if (
                            0 <= nx < n
                            and 0 <= ny < m
                            and not visited[nx][ny]
                            and board[nx][ny] == target
                        ):
                            q.append((nx, ny))
                            visited[nx][ny] = True
                power += count**2
    return power


print(bfs(board, "W"), bfs(board, "B"))
