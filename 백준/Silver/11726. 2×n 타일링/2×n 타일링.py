from sys import stdin

input = stdin.readline

n = int(input().rstrip())
dp = [False for _ in range(n + 1)]

if n == 1:
    print(1)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 10007
    print(dp[n])