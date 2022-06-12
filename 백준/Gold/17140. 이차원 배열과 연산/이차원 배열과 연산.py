from collections import Counter
from sys import stdin


input = stdin.readline

r, c, k = map(int, input().split())
r -= 1
c -= 1
board = [list(map(int, input().split())) for _ in range(3)]


def R(board):
    new_board = [[] for _ in range(len(board))]
    max_len = len(board[0])
    for i in range(len(board)):
        c = Counter()
        for j in range(len(board[i])):
            if board[i][j] != 0:  # 0은 카운트에서 제외
                c[board[i][j]] += 1
        c = c.most_common(50)
        c.sort(key=lambda x: (x[1], x[0]))
        for val, cnt in c:
            new_board[i].append(val)
            new_board[i].append(cnt)
        max_len = max(max_len, len(new_board[i]))
    for i in range(len(new_board)):
        while len(new_board[i]) != max_len:
            new_board[i].append(0)
    return new_board


def transpose(board):
    new_board = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            new_board[j][i] = board[i][j]
    return new_board


def C(board):
    board = transpose(board)
    board = R(board)
    board = transpose(board)
    return board


answer = -1
for time in range(0, 101):
    if r < len(board) and c < len(board[0]) and board[r][c] == k:
        answer = time
        break
    if len(board) >= len(board[0]):
        board = R(board)
    else:
        board = C(board)
print(answer)