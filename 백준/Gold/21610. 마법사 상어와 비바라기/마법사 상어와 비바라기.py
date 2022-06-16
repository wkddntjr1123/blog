from sys import stdin

input = stdin.readline


def create_cloud(board, cloud, visited):
    cloud.clear()
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and board[x][y] >= 2:
                cloud.append([x, y])
                board[x][y] -= 2


def move_cloud(dir, cnt, cloud):
    dx = [999, 0, -1, -1, -1, 0, 1, 1, 1]
    dy = [999, -1, -1, 0, 1, 1, 1, 0, -1]
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + dx[dir] * cnt) % n
        cloud[i][1] = (cloud[i][1] + dy[dir] * cnt) % n


def rain_fall(board, cloud, visited):
    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]
    for x, y in cloud:
        board[x][y] += 1
        visited[x][y] = True
    for x, y in cloud:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny]:
                board[x][y] += 1


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]


for _ in range(m):
    dir, cnt = map(int, input().split())
    visited = [[False for _ in range(n)] for _ in range(n)]
    move_cloud(dir, cnt, cloud)
    rain_fall(board, cloud, visited)
    create_cloud(board, cloud, visited)

answer = 0
for line in board:
    answer += sum(line)
print(answer)
