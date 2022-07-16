from sys import stdin


input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sum_table = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            sum_table[i][j] = board[i][j]
        elif i == 0:
            sum_table[i][j] = sum_table[i][j - 1] + board[i][j]
        elif j == 0:
            sum_table[i][j] = sum_table[i - 1][j] + board[i][j]
        else:
            sum_table[i][j] = (
                sum_table[i - 1][j] + sum_table[i][j - 1] + board[i][j] - sum_table[i - 1][j - 1]
            )

for _ in range(m):
    x1, y1, x2, y2 = map(lambda c: int(c) - 1, input().split())
    answer = sum_table[x2][y2]
    if x1 != 0:
        answer -= sum_table[x1 - 1][y2]
    if y1 != 0:
        answer -= sum_table[x2][y1 - 1]
    if x1 != 0 and y1 != 0:
        answer += sum_table[x1 - 1][y1 - 1]
    print(answer)