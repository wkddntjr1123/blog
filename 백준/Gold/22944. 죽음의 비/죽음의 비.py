from collections import deque
from sys import stdin

input = stdin.readline


n, h, d = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]


def bfs(start_x, start_y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([(start_x, start_y, h, 0, 0)])  # x,y,hp,um,dist
    visited[start_x][start_y] = h
    while q:
        x, y, hp, um, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == "E":
                    return dist + 1
                new_hp, new_um = hp, um
                if board[nx][ny] == "U":
                    new_um = d - 1
                else:
                    if new_um > 0:
                        new_um = new_um - 1
                    else:
                        new_hp = new_hp - 1
                if new_hp == 0:
                    continue
                if visited[nx][ny] < new_hp:
                    q.append((nx, ny, new_hp, new_um, dist + 1))
                    visited[nx][ny] = new_hp
    return -1


for i in range(n):
    for j in range(n):
        if board[i][j] == "S":
            print(bfs(i, j))
            break
