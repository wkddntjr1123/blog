n = int(input())
nums = list(map(int, input().split()))

stack = []
res = [-1 for _ in range(n)]

for i, v in enumerate(nums):
    while stack and stack[-1][1] < v:
        res[stack.pop()[0]] = v
    stack.append((i, v))

print(*res, sep=" ")