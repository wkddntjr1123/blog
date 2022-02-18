from sys import stdin


input = stdin.readline
n = int(input())
board = [list(map(int, input().rstrip("\n"))) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def valid_index(x, y):
    return (0 <= x < n) and (0 <= y < n)


def dfs(x, y, count=1):
    visited[x][y] = True
    for i in range(4):
        adj_x, adj_y = x + dx[i], y + dy[i]
        if valid_index(adj_x, adj_y) and board[adj_x][adj_y] == 1 and not visited[adj_x][adj_y]:
            count = dfs(adj_x, adj_y, count + 1)
    return count


result = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            result.append(dfs(i, j, 1))

result.sort()
print(len(result))
print(*result, sep="\n")