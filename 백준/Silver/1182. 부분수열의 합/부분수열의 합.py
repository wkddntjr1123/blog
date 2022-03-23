from sys import stdin

input = stdin.readline
n, target = map(int, input().split())

nums = list(map(int, input().split()))
answer = 0


def dfs(k, s):
    if k == n:
        if s == target:
            global answer
            answer += 1
        return
    dfs(k + 1, s)
    dfs(k + 1, s + nums[k])


dfs(0, 0)
if target == 0:
    answer -= 1
print(answer)
