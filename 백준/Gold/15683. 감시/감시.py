from sys import maxsize, stdin

input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

num0 = 0
cctv_list = []  # (cctv번호, x, y)
cctv_match = {
    1: [[0], [1], [2], [3]],
    2: [[1, 3], [0, 2]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
}
# 상우하좌 : 0123
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def change_board(temp_board, direction_list, x, y):
    global n, m
    changed_list = []
    for direction in direction_list:
        adj_x, adj_y = x, y
        while 0 <= adj_x < n and 0 <= adj_y < m:
            if temp_board[adj_x][adj_y] == 6:
                break
            if temp_board[adj_x][adj_y] == 0:
                temp_board[adj_x][adj_y] = -1
                changed_list.append((adj_x, adj_y))
            adj_x, adj_y = adj_x + dx[direction], adj_y + dy[direction]
    return changed_list


def rollback_board(temp_board, changed_list):
    for pos in changed_list:
        temp_board[pos[0]][pos[1]] = 0


for i in range(n):
    for j in range(m):
        if board[i][j] == 5:  # 5번 cctv는 먼저 처리
            for k in range(4):
                changed_list = change_board(board, [0, 1, 2, 3], i, j)
        elif board[i][j] in (1, 2, 3, 4):
            cctv_list.append((board[i][j], i, j))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            num0 += 1
result = maxsize

# k는 cctv 개수
def tracking(k, temp_board):
    global n, m, num0, result
    if k == len(cctv_list):
        result = min(result, num0)
        return
    cctv, x, y = cctv_list[k]
    for direction_list in cctv_match[cctv]:
        changed_list = change_board(temp_board, direction_list, x, y)
        num0 -= len(changed_list)
        tracking(k + 1, temp_board)
        rollback_board(temp_board, changed_list)
        num0 += len(changed_list)


tracking(0, board)
print(result)