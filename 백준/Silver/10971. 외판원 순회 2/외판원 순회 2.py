from sys import maxsize, stdin

input = stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [False for _ in range(n)]
answer = maxsize


def dfs(k, cost, prev):
    if k == n - 1:
        if board[prev][0] != 0:
            cost += board[prev][0]
            global answer
            answer = min(answer, cost)
        return
    for next in range(1, n):
        if visited[next] or board[prev][next] == 0:
            continue
        visited[next] = True
        dfs(k + 1, cost + board[prev][next], next)
        visited[next] = False


dfs(0, 0, 0)
print(answer)
