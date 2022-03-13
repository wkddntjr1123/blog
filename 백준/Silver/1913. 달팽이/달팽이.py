from sys import stdin


input = stdin.readline
n = int(input())
target = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
x = y = n // 2
movement = [1, 1, 2, 2, 2]  # +0, +2, +2, +2, +2

board[x][y] = 1
for _ in range(n // 2):  # 1 cycle
    for dir, cnt in enumerate(movement):
        if dir == 0:  # 상
            for _ in range(cnt):
                board[x - 1][y] = board[x][y] + 1
                x -= 1
        elif dir == 1:  # 우
            for _ in range(cnt):
                board[x][y + 1] = board[x][y] + 1
                y += 1
        elif dir == 2:  # 하
            for _ in range(cnt):
                board[x + 1][y] = board[x][y] + 1
                x += 1
        elif dir == 3:  # 좌
            for _ in range(cnt):
                board[x][y - 1] = board[x][y] + 1
                y -= 1
        elif dir == 4:  # 상
            for _ in range(cnt):
                board[x - 1][y] = board[x][y] + 1
                x -= 1
    for i in range(1, 5):
        movement[i] += 2

for line in board:
    print(*line)
for i, line in enumerate(board, start=1):
    for j, val in enumerate(line, start=1):
        if val == target:
            print(i, j)
            exit()