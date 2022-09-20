from sys import maxsize, stdin

input = stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]


def solution(n, arr):
    if len(arr) <= 2:
        return sum(arr)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = arr[0]
    dp[1][0] = arr[1]
    dp[1][1] = arr[0] + arr[1]
    for i in range(2, n):
        dp[i][0] = max(max(dp[i - 2]) + arr[i], max(dp[i - 3]) + arr[i] if i - 3 >= 0 else 0)
        dp[i][1] = dp[i - 1][0] + arr[i]
    return max(map(max, dp))


print(solution(n, arr))
