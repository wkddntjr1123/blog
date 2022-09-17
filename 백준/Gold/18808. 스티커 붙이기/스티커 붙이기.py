from sys import stdin

input = stdin.readline

n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    stickers.append([list(map(int, input().split())) for _ in range(r)])
answer = 0


def rotate(sticker):
    w, h = len(sticker), len(sticker[0])
    rotatedSticker = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(w):
        for j in range(h):
            rotatedSticker[j][w - i - 1] = sticker[i][j]
    return rotatedSticker


def attach(board, sticker, boardX, boardY):
    w, h = len(sticker), len(sticker[0])
    changedPos = []
    for i in range(w):
        for j in range(h):
            if sticker[i][j] == 1:
                if board[boardX + i][boardY + j] == 1:
                    return False
                changedPos.append((boardX + i, boardY + j))
    for x, y in changedPos:
        board[x][y] = 1
    return True


for sticker in stickers:
    for _ in range(4):
        isAttached = False
        w, h = len(sticker), len(sticker[0])
        for x in range(n - w + 1):
            for y in range(m - h + 1):
                if attach(board, sticker, x, y):
                    isAttached = True
                    break
            if isAttached:
                break
        if isAttached:
            break
        sticker = rotate(sticker)

print(sum(map(sum, board)))
