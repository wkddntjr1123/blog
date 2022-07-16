from sys import stdin

input = lambda: stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n  # dp[i] : i번째 수 포함 시, 오름차순 최장 부분 수열 길이
r_dp = [1] * n  # r_dp[i] : i번째 수 포함 시, 내림차순 최장 부분 수열 길이 => arr 뒤집어서 계산

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

arr.reverse()
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and r_dp[i] < r_dp[j] + 1:
            r_dp[i] = r_dp[j] + 1

answer = 0
for i in range(n):
    answer = max(answer, dp[i] + r_dp[n - i - 1] - 1)

print(answer)