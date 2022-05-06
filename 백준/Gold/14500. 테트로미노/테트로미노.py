from sys import stdin


input = stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

blocks = [
    [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
    ],
    [
        [(0, 0), (0, 1), (1, 0), (1, 1)],
    ],
    [
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 2), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 1), (1, 1), (2, 0), (2, 1)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
    ],
    [
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(0, 1), (0, 2), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
        [(0, 1), (1, 1), (1, 0), (2, 0)],
    ],
    [
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(0, 1), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (1, 1)],
        [(0, 1), (1, 1), (2, 1), (1, 0)],
    ],
]

for shape in blocks:
    for block in shape:
        for i in range(n):
            for j in range(m):
                val, fail = 0, False
                for di, dj in block:
                    nx, ny = i + di, j + dj
                    if 0 <= nx < n and 0 <= ny < m:
                        val += board[nx][ny]
                    else:
                        fail = True
                        break
                if not fail:
                    answer = max(answer, val)
print(answer)
