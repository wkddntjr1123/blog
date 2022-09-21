from collections import deque
from sys import stdin, maxsize

END = 2000

input = stdin.readline

target = int(input())

q = deque([(1, 0, 0)])

visited = [[False for _ in range(2001)] for _ in range(2001)]
visited[1][0] = True

while q:
    cur, clip, time = q.popleft()
    if cur == target:
        print(time)
        break
    # 1. copy to clipboard
    if not visited[cur][cur]:
        q.append((cur, cur, time + 1))
        visited[cur][cur] = True
    # 2. paste clipboard
    if cur + clip < 2000 and not visited[cur + clip][clip]:
        q.append((cur + clip, clip, time + 1))
        visited[cur + clip][clip] = True
    # 3. -1
    if cur - 1 > 0 and not visited[cur - 1][clip]:
        q.append((cur - 1, clip, time + 1))
        visited[cur - 1][clip] = True
