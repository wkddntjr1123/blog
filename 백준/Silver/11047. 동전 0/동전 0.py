from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

answer = 0
for i in range(n - 1, -1, -1):
    if k < coins[i]:
        continue

    count = k // coins[i]
    k -= coins[i] * count
    answer += count
    if k == 0:
        break
print(answer)
