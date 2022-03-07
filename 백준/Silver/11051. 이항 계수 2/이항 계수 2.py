from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

# (n-1)C(k-1) + (n-1)Ck = nCk
# dp[i][j]는 iCj
dp = [[False for _ in range(1001)] for _ in range(1001)]

for i in range(1, n + 1):
    dp[i][0], dp[i][i] = 1, 1
    for j in range(1, i):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10007

print(dp[n][k])