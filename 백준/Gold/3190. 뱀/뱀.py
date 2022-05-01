from collections import deque
from sys import stdin

input = stdin.readline

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2  # 사과 : 2
board[0][0] = 1  # 뱀 : 1
dir = {}
for _ in range(int(input())):
    t, d = input().split()
    dir[int(t)] = d

snake = deque([(0, 0)])
time = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cur_dir = 0  # 0123 : 동남서북
while True:
    time += 1
    nx, ny = snake[0][0] + dx[cur_dir], snake[0][1] + dy[cur_dir]
    if not (0 <= nx < n) or not (0 <= ny < n) or board[nx][ny] == 1:  # 게임 오버
        print(time)
        exit()
    if board[nx][ny] != 2:  # 사과 못 먹으면
        tail = snake.pop()
        board[tail[0]][tail[1]] = 0  # 꼬리 제거
    board[nx][ny] = 1  # 머리 이동
    snake.appendleft([nx, ny])
    if time in dir:  # 방향 전환 시간
        if dir[time] == "L":  # 좌측
            cur_dir = (cur_dir - 1) % 4
        else:  # 우측
            cur_dir = (cur_dir + 1) % 4