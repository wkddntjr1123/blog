from collections import deque
from sys import maxsize, stdin


input = stdin.readline
n, m, k = map(int, input().split())

board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[[maxsize] * (k + 1) for _ in range(m)] for _ in range(n)]

q = deque([(0, 0, 0)])
visited[0][0][0] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m


while q:
    x, y, count = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not is_valid(nx, ny):
            continue

        if board[nx][ny] == 0 and visited[nx][ny][count] > visited[x][y][count] + 1:
            visited[nx][ny][count] = visited[x][y][count] + 1
            q.append((nx, ny, count))
        elif (
            board[nx][ny] == 1
            and count < k
            and visited[nx][ny][count + 1] > visited[x][y][count] + 1
        ):
            visited[nx][ny][count + 1] = visited[x][y][count] + 1
            q.append((nx, ny, count + 1))


result = min(visited[n - 1][m - 1])
print(-1 if result == maxsize else result)
