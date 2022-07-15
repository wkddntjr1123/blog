from sys import stdin

input = lambda: stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]
print(max(dp))