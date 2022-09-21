from collections import deque
from sys import stdin

MAX_RECUR = 100000

input = stdin.readline


n, target = map(int, input().split())
if n == target:
    print(0, 1, sep="\n")
    exit()
if target in (n - 1, n + 1, n * 2):
    print(1)
    print((n - 1, n + 1, n * 2).count(target))
    exit()
if target == 0:
    print(n, 1, sep="\n")
    exit()

visited = [0 for _ in range(MAX_RECUR + 1)]
count = [0 for _ in range(MAX_RECUR + 1)]
count[n] = 1
q = deque([n])
answer = 0
dist = 0
while q:
    if answer:
        print(dist)
        print(answer)
        break
    toVisited = set()
    for _ in range(len(q)):
        cur = q.popleft()
        if cur - 1 > 0 and not visited[cur - 1]:
            count[cur - 1] += count[cur]
        if cur + 1 <= MAX_RECUR and not visited[cur + 1]:
            count[cur + 1] += count[cur]
        if 0 < cur * 2 <= MAX_RECUR and not visited[cur * 2]:
            count[cur * 2] += count[cur]
        for val in (cur - 1, cur + 1, cur * 2):
            if 0 < val <= MAX_RECUR and not visited[val]:
                toVisited.add(val)
                if val == target:
                    answer += count[cur]
    for num in toVisited:
        q.append(num)
        visited[num] = True
    dist += 1
