from collections import deque
from itertools import combinations
from sys import maxsize, stdin


input = stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
results = []
min_dist = maxsize
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for case in combinations(range(1, n + 1), 2):
    visited = set()
    visited.add(case[0])
    visited.add(case[1])
    q = deque(case)
    level = 0  # 이동한 거리
    dist = 0  # case의 거리 최소합
    while len(visited) != n:  # 모든 건물 방문할 때 까지 bfs
        level += 1
        for _ in range(len(q)):
            v = q.popleft()
            for nv in graph[v]:
                if nv not in visited:  # 방문 안했으면
                    q.append(nv)
                    visited.add(nv)
                    dist += level * 2
    if dist <= min_dist:
        results.append((dist,case[0],case[1]))
        min_dist = dist
results.sort()
print(results[0][1],results[0][2],results[0][0])
