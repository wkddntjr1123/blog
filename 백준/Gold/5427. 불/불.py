from collections import deque
from sys import stdin


input = stdin.readline


def bfs(board):
    person, fires = deque(), deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == "@":
                person.append((i, j))
            if board[i][j] == "*":
                fires.append((i, j))
    level = 0
    while person:
        level += 1
        for _ in range(len(person)):
            x, y = person.popleft()
            if board[x][y] == "*":
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == ".":
                        board[nx][ny] = "@"
                        person.append((nx, ny))
                else:
                    return level
        for _ in range(len(fires)):
            x, y = fires.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] in (".", "@"):
                    board[nx][ny] = "*"
                    fires.append((nx, ny))
    return False


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(int(input())):
    m, n = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    res = bfs(board)
    print(res if res else "IMPOSSIBLE")