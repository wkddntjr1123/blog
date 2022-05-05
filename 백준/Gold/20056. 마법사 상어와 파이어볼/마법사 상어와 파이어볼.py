from collections import deque
from sys import stdin

input = stdin.readline

n, f, k = map(int, input().split())
board = [[deque() for _ in range(n)] for _ in range(n)]
fire_pos = deque()
for _ in range(f):
    r, c, m, s, d = map(int, input().split())
    fire_pos.append((r, c, m, s, d))

def move_fires():
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    check_point = set()
    while fire_pos:
        r, c, m, s, d = fire_pos.pop()
        nr, nc = (r + dx[d] * s) % n, (c + dy[d] * s) % n
        board[nr][nc].append((m, s, d))
        check_point.add((nr, nc))
    check_fires(check_point)

def check_fires(check_point):
    for x, y in check_point:
        length = len(board[x][y])
        if length == 1:
            m, s, d = board[x][y].pop()
            fire_pos.append((x, y, m, s, d))
        elif length >= 2:
            sum_m, sum_s, cnt = 0, 0, 0
            for m, s, d in board[x][y]:
                sum_m += m
                sum_s += s
                if d % 2 == 0:
                    cnt += 1
            board[x][y] = deque()
            sum_m //= 5
            sum_s //= length
            if sum_m == 0:
                continue
            dirs = (0, 2, 4, 6) if cnt in (0, length) else (1, 3, 5, 7)
            for d in dirs:
                fire_pos.append((x, y, sum_m, sum_s, d))

for _ in range(k):
    move_fires()
answer = 0
for _, _, m, _, _ in fire_pos:
    answer += m
print(answer)