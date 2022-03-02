from collections import deque
from copy import deepcopy
from sys import stdin


input = stdin.readline

n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
visited = deepcopy(board)
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] += 1


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
    return cnt


total = 0
answer = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            answer.append(bfs(i, j))
            total += 1
answer.sort()
print(total)
print(*answer)