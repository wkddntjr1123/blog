from sys import stdin

input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def valid(board, n, x, y, answer):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != board[x][y]:
                return False
    if board[x][y] == 0:
        answer[0] += 1
    else:
        answer[1] += 1
    return True

def process(board, n, x, y, answer):
    if not valid(board, n, x, y, answer):
        process(board, n // 2, x, y, answer)
        process(board, n // 2, x + n // 2, y, answer)
        process(board, n // 2, x, y + n // 2, answer)
        process(board, n // 2, x + n // 2, y + n // 2, answer)

answer = [0, 0]
process(board, n, 0, 0, answer)
print(*answer, sep="\n")