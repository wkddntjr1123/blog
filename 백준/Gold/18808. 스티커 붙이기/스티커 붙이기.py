from sys import stdin

input = stdin.readline


def rotate(sticker):
    return list(map(list, zip(*sticker[::-1])))


def valid_pos(board, sticker, x, y):
    val_pos = []
    for i in range(x, x + len(sticker)):
        for j in range(y, y + len(sticker[0])):
            if sticker[i - x][j - y] == 1:
                if board[i][j] == 0:  # 붙이기 가능
                    val_pos.append((i, j))
                else:
                    return False
    for i, j in val_pos:
        board[i][j] = 1
    return True


n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
stickers = []
for _ in range(k):
    r, _ = map(int, input().split())
    stickers.append([list(map(int, input().split())) for _ in range(r)])

for sticker in stickers:
    find = False
    for _ in range(4):  # 회전
        for i in range(n - len(sticker) + 1):
            for j in range(m - len(sticker[0]) + 1):
                if valid_pos(board, sticker, i, j):
                    find = True
                    break
            if find:
                break
        if find:
            break
        else:
            sticker = rotate(sticker)

answer = 0
for line in board:
    answer += line.count(1)
print(answer)