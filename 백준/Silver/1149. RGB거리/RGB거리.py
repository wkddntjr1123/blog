from sys import maxsize, stdin

input = stdin.readline

n = int(input())
dp = [[maxsize] * 3 for _ in range(n)]
rgbCost = []
for _ in range(n):
    rgbCost.append(tuple(map(int, input().split())))
dp[0] = rgbCost[0]

for i in range(1, n):
    dp[i][0] = rgbCost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = rgbCost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = rgbCost[i][2] + min(dp[i - 1][0], dp[i - 1][1])
print(min(dp[-1]))
