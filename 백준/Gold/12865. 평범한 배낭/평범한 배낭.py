from sys import stdin


input = stdin.readline
n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]  # (무게, 가치)

# table[i][j] : i번째 물건까지 넣는 경우에, 배낭의 무게가 j무게일 경우 최대 가치합
table = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):  # i-1번째 물건 까지 포함
    for cur_w in range(1, k + 1):  # 배낭 무게
        w, v = items[i - 1]
        if cur_w >= w:
            table[i][cur_w] = max(v + table[i - 1][cur_w - w], table[i - 1][cur_w])
        else:
            table[i][cur_w] = table[i - 1][cur_w]
print(max(map(max, table)))