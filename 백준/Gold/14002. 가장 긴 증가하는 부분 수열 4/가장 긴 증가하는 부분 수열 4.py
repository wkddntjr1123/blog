from sys import stdin

input = lambda: stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
parent = [-1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            parent[i] = j

answer = -1
start = -1
for i, v in enumerate(dp):
    if v > answer:
        answer = v
        start = i
print(answer)
route = [arr[start]]
while parent[start] != -1:
    route.append(arr[parent[start]])
    start = parent[start]
route.reverse()
print(*route)