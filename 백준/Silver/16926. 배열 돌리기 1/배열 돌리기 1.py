from collections import deque
from sys import stdin


input = stdin.readline

n, m, r = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
board = [list(map(int, input().split())) for _ in range(n)]


def valid(i, j):
    return 0 <= i < n and 0 <= j < m


def rotate(i, j, board, r):
    visited[i][j] = True
    q = deque([board[i][j]])
    i += 1
    trail = [0, 0, 0, 0]  # 하 우 상 좌 : 몇칸씩 가는지
    while valid(i, j) and not visited[i][j]:
        visited[i][j] = True
        q.append(board[i][j])
        trail[0] += 1
        i += 1
    i -= 1
    j += 1
    while valid(i, j) and not visited[i][j]:
        visited[i][j] = True
        q.append(board[i][j])
        trail[1] += 1
        j += 1
    j -= 1
    i -= 1
    while valid(i, j) and not visited[i][j]:
        visited[i][j] = True
        q.append(board[i][j])
        trail[2] += 1
        i -= 1
    i += 1
    j -= 1
    while valid(i, j) and not visited[i][j]:
        visited[i][j] = True
        q.append(board[i][j])
        trail[3] += 1
        j -= 1
    q.rotate(r)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    board[i][j] = q.popleft()
    for k, cnt in enumerate(trail):
        for _ in range(cnt):
            i += dx[k]
            j += dy[k]
            board[i][j] = q.popleft()


i = 0
while True:
    if not valid(i, i) or visited[i][i]:
        break
    rotate(i, i, board, r)
    i += 1
for line in board:
    print(*line)