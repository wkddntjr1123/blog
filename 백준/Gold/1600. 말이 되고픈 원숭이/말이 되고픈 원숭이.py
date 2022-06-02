from collections import deque
from sys import maxsize, stdin


input = stdin.readline

k = int(input())
m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1, -2, -1, -2, -1, 2, 1, 2, 1]
dy = [1, 0, -1, 0, 1, 2, -1, -2, 1, 2, -1, -2]


def valid(x, y):
    return 0 <= x < n and 0 <= y < m


# dist[x][y][k] = 이동 거리,  k는 남은 말 이동 가능 수
dist = [[[maxsize for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

q = deque([(0, 0, k)])
dist[0][0][k] = 0
while q:
    x, y, rest_k = q.popleft()
    cur_dist = dist[x][y][rest_k]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if valid(nx, ny) and board[nx][ny] == 0 and dist[nx][ny][rest_k] > cur_dist + 1:
            dist[nx][ny][rest_k] = cur_dist + 1
            q.append((nx, ny, rest_k))
    if rest_k > 0:
        for i in range(4, 12):
            nx, ny = x + dx[i], y + dy[i]
            if valid(nx, ny) and board[nx][ny] == 0 and dist[nx][ny][rest_k - 1] > cur_dist + 1:
                dist[nx][ny][rest_k - 1] = cur_dist + 1
                q.append((nx, ny, rest_k - 1))
answer = min(dist[-1][-1])
print(answer if answer != maxsize else -1)