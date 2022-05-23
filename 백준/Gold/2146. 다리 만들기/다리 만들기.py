from collections import deque
from itertools import combinations
from sys import maxsize, stdin


input = stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x: int, y: int) -> list:
    q = deque([(x, y)])
    visited[x][y] = True
    borders = set()
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    borders.add((x, y))
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return list(borders)


def get_dist(pos1, pos2):

    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


border_table = {}
island = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            border_table[island] = bfs(i, j)
            island += 1

answer = maxsize

for a, b in combinations((border_table.keys()), 2):
    for pos1 in border_table[a]:
        for pos2 in border_table[b]:
            answer = min(answer, get_dist(pos1, pos2))

print(answer - 1)