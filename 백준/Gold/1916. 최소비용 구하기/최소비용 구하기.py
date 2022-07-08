from sys import maxsize, stdin
from heapq import heappop, heappush

input = stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
dist = [maxsize for _ in range(n + 1)]
for _ in range(int(input())):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
start, end = map(int, input().split())
dist[start] = 0
heap = [(0, start)]
while heap:
    cur_cost, cur_v = heappop(heap)
    if cur_cost > dist[cur_v]:
        continue
    for n_cost, nv in graph[cur_v]:
        if cur_cost + n_cost < dist[nv]:
            dist[nv] = cur_cost + n_cost
            heappush(heap, (dist[nv], nv))
print(dist[end])