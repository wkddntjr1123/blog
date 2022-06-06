from collections import Counter, defaultdict, deque
from sys import stdin


input = stdin.readline
n = int(input())
board = [[-1 for _ in range(n)] for _ in range(n)]
like_table = defaultdict(set)
students = deque()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for _ in range(n**2):
    s, *t = map(int, input().split())
    students.append(s)
    like_table[s].update(t)


def valid_index(x, y):
    return 0 <= x < n and 0 <= y < n


def choose_like(board, student):
    c = Counter()
    for x in range(n):
        for y in range(n):
            if board[x][y] != -1:
                continue
            for k in range(4):
                adj_x, adj_y = x + dx[k], y + dy[k]
                if valid_index(adj_x, adj_y) and board[adj_x][adj_y] in like_table[student]:
                    c[(x, y)] += 1
    res = []
    before_val = None
    for pos, val in c.most_common():
        if not before_val:
            before_val = val
            res.append(pos)
        else:
            if val == before_val:
                res.append(pos)
            else:
                break
    if not res:
        for i in range(n):
            for j in range(n):
                if board[i][j] == -1:
                    res.append((i, j))
    return res


def count_empty(board, likes):
    c = Counter()
    for like in likes:  # likes는 기본적으로 빈자리들
        x, y = like
        for i in range(4):
            adj_x, adj_y = x + dx[i], y + dy[i]
            if valid_index(adj_x, adj_y) and board[adj_x][adj_y] == -1:
                c[(x, y)] += 1
    res = []
    before_val = None
    for pos, val in c.most_common():
        if not before_val:
            before_val = val
            res.append(pos)
        else:
            if val == before_val:
                res.append(pos)
            else:
                break
    if not res:
        return likes
    return res


while students:
    student = students.popleft()
    # 1. 빈 칸들 중 상하좌우 좋아하는 사람이 많은 곳에 앉는다.
    likes = choose_like(board, student)
    if len(likes) == 1:
        x, y = likes[0]
        board[x][y] = student
        continue
    # 2. 주변에 빈 칸이 가장 많은 곳에 앉는다.
    empties = count_empty(board, likes)
    if len(empties) == 1:
        x, y = empties[0]
        board[x][y] = student
        continue
    # 3. 최소행,최소열
    empties.sort(key=lambda x: (x[0], x[1]))
    x, y = empties[0]
    board[x][y] = student

answer = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for k in range(4):
            adj_x, adj_y = x + dx[k], y + dy[k]
            if valid_index(adj_x, adj_y):
                if board[adj_x][adj_y] in like_table[board[x][y]]:
                    cnt += 1
        if cnt > 0:
            answer += 10 ** (cnt - 1)
print(answer)