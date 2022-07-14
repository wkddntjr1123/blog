from collections import deque
from sys import stdin


input = lambda: stdin.readline().rstrip()
q = deque()
for i in range(int(input())):
    command = input()
    if " " in command:
        a, b = command.split()
        if a == "push_front":
            q.appendleft(b)
        elif a == "push_back":
            q.append(b)
    elif "pop_front" == command:
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif "pop_back" == command:
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif "size" == command:
        print(len(q))
    elif "empty" == command:
        if not q:
            print(1)
        else:
            print(0)
    elif "front" == command:
        if not q:
            print(-1)
        else:
            print(q[0])
    elif "back" == command:
        if not q:
            print(-1)
        else:
            print(q[-1])
