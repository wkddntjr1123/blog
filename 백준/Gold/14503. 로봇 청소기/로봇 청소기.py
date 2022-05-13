from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
r, c, dir = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0


def dfs(x, y, d):
    global cnt
    # 현재 위치 청소
    if board[x][y] == 0:
        cnt += 1
        board[x][y] = 2
    for i in range(1, 5):
        nd = (d - i) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            dfs(nx, ny, nd)
            return
    # 360회전 이후
    nd = (d + 2) % 4
    nx, ny = x + dx[nd], y + dy[nd]
    # 뒤가 벽이 아니면 후진
    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1:
        dfs(nx, ny, d)


dfs(r, c, dir)
print(cnt)
