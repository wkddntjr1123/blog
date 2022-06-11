from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)

input = stdin.readline

n, l, r = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]


def one_day(board):
    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    def dfs(board, x, y, acc, count, arr):
        visited[x][y] = True
        acc += board[x][y]
        arr.append((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and l <= abs(board[x][y] - board[nx][ny]) <= r
            ):
                acc, count = dfs(board, nx, ny, acc, count + 1, arr)  # 여기가 문제네 dfs끝날 때 재귀 터져버림
        return acc, count

    find = False
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                arr = []
                acc, cnt = dfs(board, x, y, 0, 1, arr)
                if cnt != 1:
                    for i, j in arr:
                        board[i][j] = acc // cnt
                    find = True
    return find


# board 변경 일어나면 True를 리턴
answer = 0
while one_day(board):
    answer += 1
print(answer)
