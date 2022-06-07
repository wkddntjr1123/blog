from collections import deque
from sys import stdin


input = stdin.readline


n, m, k = map(int, input().split())
board = [[5 for _ in range(n)] for _ in range(n)]  # 땅
food = [list(map(int, input().split())) for _ in range(n)]  # 추가 양분값
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)
for i in range(n):
    for j in range(n):
        trees[i][j] = deque(sorted(trees[i][j]))


def spring_summer(board, trees):
    for x in range(n):
        for y in range(n):
            for idx, age in enumerate(trees[x][y]):
                if age <= board[x][y]:
                    board[x][y] -= age
                    trees[x][y][idx] += 1
                else:
                    for j in range(idx, len(trees[x][y])):
                        board[x][y] += trees[x][y][j] // 2
                    while len(trees[x][y]) - idx:
                        trees[x][y].pop()
                    break


def fall(trees):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for x in range(n):
        for y in range(n):
            for k in range(len(trees[x][y])):
                if trees[x][y][k] % 5 == 0:
                    for i in range(8):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].appendleft(1)


def winter(board, food):
    for x in range(n):
        for y in range(n):
            board[x][y] += food[x][y]


for _ in range(k):
    spring_summer(board, trees)
    fall(trees)
    winter(board, food)

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)