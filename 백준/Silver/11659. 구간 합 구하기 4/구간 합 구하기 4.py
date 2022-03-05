from sys import stdin


input = stdin.readline
n, t = map(int, input().split())
nums = list(map(int, input().split()))
s = [0 for _ in range(len(nums))]
s[0] = nums[0]
for i in range(1, len(nums)):
    s[i] = s[i - 1] + nums[i]
for _ in range(t):
    u, v = map(lambda x: int(x) - 1, input().split())
    print(s[v] - s[u - 1] if u != 0 else s[v])