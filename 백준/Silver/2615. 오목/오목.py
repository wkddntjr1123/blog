from sys import stdin


input = stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]


def valid(i, j):
    return 0 <= i < 19 and 0 <= j < 19


def check_row(i, j):
    val = board[i][j]
    p = j - 1
    cnt = 1
    res = [(i, j)]
    while valid(i, p) and board[i][p] == val:
        res.append((i, p))
        cnt += 1
        p -= 1
    p = j + 1
    while valid(i, p) and board[i][p] == val:
        res.append((i, p))
        cnt += 1
        p += 1
    if cnt != 5:
        return None
    return res


def check_col(i, j):
    val = board[i][j]
    p = i - 1
    cnt = 1
    res = [(i, j)]
    while valid(p, j) and board[p][j] == val:
        res.append((p, j))
        cnt += 1
        p -= 1
    p = i + 1
    while valid(p, j) and board[p][j] == val:
        res.append((p, j))
        cnt += 1
        p += 1
    if cnt != 5:
        return None
    return res


def check_slash(i, j):
    val = board[i][j]
    l, r = i + 1, j + 1
    cnt = 1
    res = [(i, j)]
    while valid(l, r) and board[l][r] == val:
        res.append((l, r))
        cnt += 1
        l += 1
        r += 1
    l, r = i - 1, j - 1
    while valid(l, r) and board[l][r] == val:
        res.append((l, r))
        cnt += 1
        l -= 1
        r -= 1
    if cnt != 5:
        return None
    return res


def check_back(i, j):
    val = board[i][j]
    l, r = i + 1, j - 1
    cnt = 1
    res = [(i, j)]
    while valid(l, r) and board[l][r] == val:
        res.append((l, r))
        cnt += 1
        l += 1
        r -= 1
    l, r = i - 1, j + 1
    while valid(l, r) and board[l][r] == val:
        res.append((l, r))
        cnt += 1
        l -= 1
        r += 1
    if cnt != 5:
        return None
    return res


res = False
for i in range(19):
    for j in range(19):
        if board[i][j] == 0:
            continue
        res = check_row(i, j) or check_col(i, j) or check_slash(i, j) or check_back(i, j)
        if res:
            print(board[i][j])
            res = sorted(res, key=lambda x: (x[1], x[0]))[0]
            print(res[0] + 1, res[1] + 1)
            exit()

print(0)