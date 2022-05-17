from collections import deque
from sys import maxsize, stdin


input = stdin.readline

m, n, h = map(int, input().split())
graph = [[False for _ in range(n)] for _ in range(h)]
outer = inner = 0
for _ in range(n * h):
    graph[outer][inner] = list(map(int, input().split()))
    inner += 1
    if inner >= n:
        inner = 0
        outer += 1

q = deque()
# 익은 모든 토마토가 bfs 시작점
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append((k, i, j))

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 0, -1, 0, 1]
dy = [0, 0, 1, 0, -1, 0]


def valid(z, x, y):
    return 0 <= z < h and 0 <= x < n and 0 <= y < m


while q:
    for _ in range(len(q)):
        z, x, y = q.popleft()
        for i in range(6):  # 같은 상자 인접 토마토
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if valid(nz, nx, ny) and graph[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1
res = -maxsize
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                print(-1)
                exit()
            if (graph[z][x][y] - 1) > res:
                res = graph[z][x][y] - 1
print(res)