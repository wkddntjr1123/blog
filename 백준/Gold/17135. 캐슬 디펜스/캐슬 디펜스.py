from collections import deque
from copy import deepcopy
from itertools import combinations
from sys import stdin


input = stdin.readline


def move(board) -> None:
    for i in range(n - 1, 0, -1):
        board[i] = board[i - 1]
    board[0] = [0 for _ in range(m)]


def attack(board, attackers, d) -> int:
    targets = set()
    for x, y in attackers:  # 궁수 1명씩 bfs
        visited = [[False for _ in range(m)] for _ in range(n + 1)]
        q = deque([(x, y)])
        visited[x][y] = True
        dx = [0, -1, 0]
        dy = [-1, 0, 1]
        level = 0
        target = None
        out = False
        while q:
            if level > d:
                break
            level += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                if board[x][y] == 1:
                    target = (x, y)
                    out = True
                    break
                for i in range(3):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        q.append((nx, ny))
                        visited[nx][ny] = True
            if out:
                break
        if target:
            targets.add(target)
    res = 0
    for item in targets:
        board[item[0]][item[1]] = 0
        res += 1
    return res


n, m, d = map(int, input().split())
origin_board = [list(map(int, input().split())) for _ in range(n)]
origin_board.append([-1 for _ in range(m)])  # 성 표현
answer = 0
for case in combinations(range(m), 3):
    temp_answer = 0
    attackers = [(n, y) for y in case]
    board = deepcopy(origin_board)
    for _ in range(n):
        temp_answer += attack(board, attackers, d)
        move(board)
    answer = max(answer, temp_answer)
print(answer)