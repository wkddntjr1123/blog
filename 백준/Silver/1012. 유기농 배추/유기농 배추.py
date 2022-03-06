from copy import deepcopy
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

input = stdin.readline

for _ in range(int(input())):
    answer = 0
    n, m, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    visited = deepcopy(board)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1

    def dfs(x, y, visited):
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny, visited)

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == 1:
                dfs(i, j, visited)
                answer += 1
    print(answer)