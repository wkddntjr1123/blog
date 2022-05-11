import math
from sys import stdin


input = stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
answer = -1


def check(i, j, di, dj):
    global answer
    res = ""
    while 0 <= i < n and 0 <= j < m:
        res += board[i][j]
        if is_sqrt(int(res)):
            answer = max(answer, int(res))
        i += di
        j += dj


def is_sqrt(num):
    val = math.sqrt(num)
    return (val - int(val)) == 0


for i in range(n):
    for j in range(m):
        for di in range(-n, n):
            for dj in range(-m, m):
                if di or dj:
                    check(i, j, di, dj)

if n == m == 1:
    print(board[0][0]) if is_sqrt(int(board[0][0])) else print(-1)
else:
    print(answer)
