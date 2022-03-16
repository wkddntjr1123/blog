from sys import stdin


input = stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [0 for _ in range(n + 1)]


def dfs(v):
    for nv in graph[v]:
        if dist[nv] == 0:
            dist[nv] = dist[v] + 1
            dfs(nv)


dfs(start)
print(dist[end] if dist[end] != 0 else -1)