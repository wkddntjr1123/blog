from sys import stdin

input = stdin.readline

n = int(input().rstrip())
colors = [list(map(int, input().split())) for _ in range(n)]
dp = [[False for _ in range(3)] for _ in range(n)]

if n == 1:
    print(min(colors[0]))
else:
    dp[0] = colors[0]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + colors[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + colors[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + colors[i][2]
    print(min(dp[n - 1]))