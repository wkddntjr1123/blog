from sys import stdin

HEIGHT = 0
CNT = 1

input = stdin.readline

arr = [int(input()) for _ in range(int(input()))]
stack = []
answer = 0
for h in arr:
    while stack and stack[-1][HEIGHT] < h:
        answer += stack.pop()[CNT]
    if not stack:
        stack.append((h, 1))
        continue
    if stack[-1][HEIGHT] == h:
        item = stack.pop()
        answer += item[CNT]
        if stack:
            answer += 1
        stack.append((item[HEIGHT], item[CNT] + 1))
    elif stack[-1][HEIGHT] > h:
        answer += 1
        stack.append((h, 1))

print(answer)