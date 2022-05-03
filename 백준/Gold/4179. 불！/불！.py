from collections import deque
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
board = [list(input().rstrip()) for _ in range(n)]
visited_j = [[False for _ in range(m)] for _ in range(n)]
visited_f = [[False for _ in range(m)] for _ in range(n)]


def bfs():
    global n, m, board
    q_j = deque()
    q_f = deque()
    # 지훈, 불 초기화
    for i in range(n):
        for j in range(m):
            if board[i][j] == "J":
                q_j.appendleft((i, j))
                visited_j[i][j] = True
            elif board[i][j] == "F":
                q_f.appendleft((i, j))
                visited_f[i][j] = True
    result = 0
    while q_j or q_f:
        result += 1
        for _ in range(len(q_j)):  # 1사이클
            x, y = q_j.popleft()
            if board[x][y] == "F":  # 불번진곳에 지훈이 서있으면 X
                continue
            for i in range(4):
                adj_x, adj_y = x + dx[i], y + dy[i]
                if not (0 <= adj_x < n and 0 <= adj_y < m):
                    return result
                if board[adj_x][adj_y] == "#":  # 벽이면 X
                    continue
                if not visited_j[adj_x][adj_y] and board[adj_x][adj_y] == ".":
                    q_j.append((adj_x, adj_y))
                    visited_j[adj_x][adj_y] = True
        for _ in range(len(q_f)):  # 1사이클
            x, y = q_f.popleft()
            for i in range(4):
                adj_x, adj_y = x + dx[i], y + dy[i]
                if not (0 <= adj_x < n and 0 <= adj_y < m):
                    continue
                if board[adj_x][adj_y] == "#":  # 벽이면 X
                    continue
                if not visited_f[adj_x][adj_y]:
                    q_f.append((adj_x, adj_y))
                    board[adj_x][adj_y] = "F"
                    visited_f[adj_x][adj_y] = True
    return "IMPOSSIBLE"


print(bfs())