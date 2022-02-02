def right_rotate(board):
    n = len(board)

    next = [board[i][n - 1 - i] for i in range(n)]
    for i in range(n):
        board[i][n - 1 - i] = board[i][n // 2]

    prev = next[:]
    next = [board[n // 2][n - 1 - i] for i in range(n)]
    for i in range(n):
        board[n // 2][n - 1 - i] = prev[i]

    prev = next[:]
    next = [board[n - 1 - i][n - 1 - i] for i in range(n)]
    for i in range(n):
        board[n - 1 - i][n - 1 - i] = prev[i]

    prev = next[:]
    for i in range(n):
        board[n - 1 - i][n // 2] = prev[i]


t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    if d < 0:
        d = 360 - abs(d)
    d //= 45
    board = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(d):
        right_rotate(board)
    for line in board:
        print(*line)