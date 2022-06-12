from sys import stdin


input = stdin.readline

input()
arr = list(enumerate(map(int, input().split())))
stack = []
res = [0 for _ in range(len(arr))]
while arr:
    idx, val = arr.pop()
    if not stack:
        stack.append((idx, val))
        continue
    while stack and stack[-1][1] < val:
        prev_idx, _ = stack.pop()
        res[prev_idx] = idx + 1
    stack.append((idx, val))
print(*res)
