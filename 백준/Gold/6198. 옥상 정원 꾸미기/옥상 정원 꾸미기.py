from collections import defaultdict
from sys import maxsize, stdin


input = stdin.readline

arr = [int(input()) for _ in range(int(input()))] + [maxsize]
stack = []
answer = 0
for i in range(len(arr)):
    if not stack or arr[stack[-1]] > arr[i]:
        stack.append(i)
    else:
        while stack and arr[stack[-1]] <= arr[i]:
            answer += i - stack.pop() - 1
        stack.append(i)
print(answer)