from collections import deque
from sys import stdin, maxsize

END = 2000

input = stdin.readline

target = int(input())

q = deque([(1, 0, 0)])

visited = set()
visited.add((1, 2))
while q:
    cur, clip, time = q.popleft()
    if cur == target:
        print(time)
        break
    # 1. copy to clipboard
    if (cur, cur) not in visited:
        q.append((cur, cur, time + 1))
        visited.add((cur, cur))
    # 2. paste clipboard
    if cur + clip < 2000 and (cur + clip, clip) not in visited:
        q.append((cur + clip, clip, time + 1))
        visited.add((cur + clip, clip))
    # 3. -1
    if cur - 1 > 0 and (cur - 1, clip) not in visited:
        q.append((cur - 1, clip, time + 1))
        visited.add((cur - 1, clip))
