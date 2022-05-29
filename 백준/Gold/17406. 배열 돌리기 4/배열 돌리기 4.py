from copy import deepcopy
from itertools import permutations
from sys import maxsize, stdin


def min_row_sum(board):
    res = maxsize
    for line in board:
        res = min(res, sum(line))
    return res


def rotate(min_x, min_y, max_x, max_y):
    # 재귀 종료 조건
    if max_x - min_x <= 1 or max_y - min_y <= 1:
        return
    # 1. 가장자리 돌리기
    temp = board[min_x][min_y]
    for i in range(min_x, max_x):
        board[i][min_y] = board[i + 1][min_y]
    for j in range(min_y, max_y):
        board[max_x][j] = board[max_x][j + 1]
    for i in range(max_x, min_x, -1):
        board[i][max_y] = board[i - 1][max_y]
    for j in range(max_y, min_y, -1):
        board[min_x][j] = board[min_x][j - 1]
    board[min_x][min_y + 1] = temp
    # 2. 1칸 내부 들어가서 돌리기
    rotate(min_x + 1, min_y + 1, max_x - 1, max_y - 1)


input = stdin.readline

n, m, num_r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

operation = []
for _ in range(num_r):
    r, c, s = map(int, input().split())
    r, c = r - 1, c - 1
    operation.append((r - s, c - s, r + s, c + s))  # min_x, min_y, max_x, max_y

res = maxsize
original_board = deepcopy(board)
for case in permutations(operation, len(operation)):
    board = deepcopy(original_board)
    for min_x, min_y, max_x, max_y in case:
        rotate(min_x, min_y, max_x, max_y)
    res = min(res, min_row_sum(board))

print(res)
