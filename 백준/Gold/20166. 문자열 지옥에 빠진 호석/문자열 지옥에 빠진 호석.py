from collections import defaultdict, deque
from sys import stdin


input = lambda: stdin.readline().rstrip()


def range_parse(x, y):
    if x < 0:
        x = n - 1
    if x >= n:
        x = 0
    if y < 0:
        y = m - 1
    if y >= m:
        y = 0
    return x, y


def bfs(_x, _y):
    q = deque([(_x, _y, board[_x][_y])])
    for idx in range(1, 5):  # 최대 문자열 길이만큼 반복 == MAX 5
        for _ in range(len(q)):
            x, y, s = q.popleft()
            table[s] += 1
            for i in range(len(dx)):
                nx, ny = range_parse(x + dx[i], y + dy[i])
                if idx != 4:
                    q.append((nx, ny, s + board[nx][ny]))
                else:
                    table[s + board[nx][ny]] += 1


n, m, k = map(int, input().split())
board = [input() for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
table = defaultdict(int)  # 1번의 전체적인 bfs만 돌아서 먼저 board 상 모든 문자에 대한 값을 캐싱
for i in range(n):
    for j in range(m):
        bfs(i, j)
for _ in range(k):
    s = input()
    answer = 0
    print(table[s])
