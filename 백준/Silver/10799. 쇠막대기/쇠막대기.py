from sys import stdin

input = stdin.readline

stack = []

s = input().rstrip()
res = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append("(")
    else:
        if s[i - 1] == "(":  # lazer
            stack.pop()
            res += len(stack)
        else:  # not lazer
            stack.pop()
            res += 1
print(res)