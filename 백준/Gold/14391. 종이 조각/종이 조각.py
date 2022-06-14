from itertools import product
from sys import maxsize, stdin

input = stdin.readline
n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

answer = 0
# c_board의 0은 세로, 1은 가로
def calc(c_board):
    visited = [[False for _ in range(m)] for _ in range(n)]
    avail = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            val = ""
            nx, ny = i, j
            if c_board[i][j] == 0 and not visited[i][j]:  # 세로
                while 0 <= nx < n and c_board[nx][ny] == 0 and not visited[nx][ny]:
                    val += board[nx][ny]
                    visited[nx][ny] = True
                    nx += 1
            elif c_board[i][j] == 1 and not visited[i][j]:
                while 0 <= ny < m and c_board[nx][ny] == 1 and not visited[nx][ny]:
                    val += board[nx][ny]
                    visited[nx][ny] = True
                    ny += 1
            if val:
                avail += int(val)
    return avail


def process(k, c_board):
    if k == n:
        global answer
        res = calc(c_board)
        answer = max(answer, res)
        return
    for row_case in product(range(0, 2), repeat=m):
        process(k + 1, c_board + [list(row_case)])


process(0, [])
print(answer)
