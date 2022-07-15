from sys import stdin

input = lambda: stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))