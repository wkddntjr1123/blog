from collections import deque
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    left = True
    ops = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    if n == 0:
        arr = []
    fail = False
    for op in ops:
        if op == "R":
            left = not left
        else:
            if not arr:
                fail = True
                break
            arr.popleft() if left else arr.pop()
    if not left:
        arr.reverse()
    print("error" if fail else f"[{','.join(arr)}]")
