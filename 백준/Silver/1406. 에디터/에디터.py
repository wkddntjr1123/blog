from collections import deque
from sys import stdin

input = lambda: stdin.readline().rstrip()

left, right = deque(input()), deque()

for _ in range(int(input())):
    op = input()
    if op == "L":
        if left:
            right.appendleft(left.pop())
    elif op == "D":
        if right:
            left.append(right.popleft())
    elif op == "B":
        if left:
            left.pop()
    else:
        _, value = op.split()
        left.append(value)

print("".join(left) + "".join(right))