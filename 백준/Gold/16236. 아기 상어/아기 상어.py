from collections import deque
from sys import stdin


input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

SIZE, EAT_NUM = 2, 0


q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            q.append((i, j, 0))  # start pos
            board[i][j] = 0
            break

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

answer = 0


def valid_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs():
    global SIZE, EAT_NUM, q, board
    visited = [[False] * n for _ in range(n)]
    x, y, dist = q[0]
    visited[x][y] = True
    cache = []
    while q:
        for _ in range(len(q)):
            x, y, dist = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not valid_range(nx, ny) or board[nx][ny] > SIZE or visited[nx][ny]:
                    continue
                if 0 < board[nx][ny] < SIZE:
                    cache.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
                else:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
        if cache:
            EAT_NUM += 1
            if EAT_NUM == SIZE:
                SIZE += 1
                EAT_NUM = 0
            q.clear()
            cache.sort(key=lambda item: (item[0], item[1]))
            tx, ty, dist = cache[0]
            q.append((tx, ty, 0))  # next start pos
            board[tx][ty] = 0
            return dist
    return False


while True:
    result = bfs()
    if not result:
        break
    answer += result
print(answer)