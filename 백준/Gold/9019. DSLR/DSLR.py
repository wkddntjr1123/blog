from collections import deque
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    visited = [False for _ in range(10000)]
    path = [False for _ in range(10000)]
    q = deque([a])
    visited[a] = True
    level = 0
    found = False
    while q:
        level += 1
        for _ in range(len(q)):
            x = q.popleft()
            if x == b:
                found = True
                break
            d = (x * 2) % 10000
            if not visited[d]:
                visited[d] = True
                path[d] = ("D", x)
                q.append(d)
            s = x - 1 if x != 0 else 9999
            if not visited[s]:
                visited[s] = True
                path[s] = ("S", x)
                q.append(s)
            x = str(x).rjust(4, "0")
            l = int(x[1:] + x[0])
            if not visited[l]:
                visited[l] = True
                path[l] = ("L", int(x))
                q.append(l)
            r = int(x[-1] + x[:-1])
            if not visited[r]:
                visited[r] = True
                path[r] = ("R", int(x))
                q.append(r)
        if found:
            break
    res = ""
    while path[b]:
        res += path[b][0]
        b = path[b][1]
    print(res[::-1])
