from itertools import combinations
from sys import maxsize, stdin

input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

homes = []
shops = []
result = maxsize
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i, j))
        if board[i][j] == 2:
            shops.append((i, j))
visited = [False for _ in range(len(shops))]


def get_min_dist(selected_shops):
    global homes, result
    temp_result = 0
    for home in homes:
        min_dist = maxsize
        for shop in selected_shops:
            min_dist = min(min_dist, abs(home[0] - shop[0]) + abs(home[1] - shop[1]))
        temp_result += min_dist
    result = min(result, temp_result)


for selected in combinations(shops, m):
    get_min_dist(selected)

print(result)