from collections import deque
from sys import stdin

input = stdin.readline

num_v = int(input())
graph = [[] for _ in range(num_v + 1)]
for _ in range(num_v - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
p = [-1 for _ in range(num_v + 1)]

def bfs(root):
    q = deque()
    q.append(root)
    p[root] = 0
    while q:
        cur = q.popleft()
        for adj in graph[cur]:
            if p[adj] != -1:
                continue
            q.append(adj)
            p[adj] = cur

bfs(1)
for i in range(2, num_v + 1):
    print(p[i])