from sys import maxsize, stdin

input = lambda: stdin.readline().rstrip()

x = int(input())
dp = [maxsize] * (x + 3)
parent = [-1] * (x + 3)
dp[1] = 0
dp[2] = 1
parent[2] = 1
dp[3] = 1
parent[3] = 1

for i in range(4, x + 1):
    val = maxsize
    if i % 3 == 0:
        val = dp[i // 3]
        parent[i] = i // 3
    if i % 2 == 0 and dp[i // 2] < val:
        val = dp[i // 2]
        parent[i] = i // 2
    if dp[i - 1] < val:
        val = dp[i - 1]
        parent[i] = i - 1
    dp[i] = val + 1
print(dp[x])
route = [x]
while parent[x] != -1:
    route.append(parent[x])
    x = parent[x]
print(*route)