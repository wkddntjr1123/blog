from sys import stdin


input = stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n + 1)]

res = 0


def dfs(v):
    global res
    res += 1
    visited[v] = True
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)


dfs(1)
print(res - 1)
