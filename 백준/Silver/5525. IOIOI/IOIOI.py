from sys import stdin

input = stdin.readline

n = int(input())
_ = input()

s = input().rstrip()
stack = [i for i, char in enumerate(s) if char == "I"]

res = cnt = 0
for i in range(1, len(stack)):
    if stack[i - 1] + 2 == stack[i]:
        cnt += 1
    else:
        cnt = 0
    if cnt >= n:
        res += 1
print(res)