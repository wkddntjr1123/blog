from collections import deque
from sys import maxsize, stdin

input = stdin.readline

n = int(input())
m = int(input())
adj = [[maxsize for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    s, t, cost = map(int, input().split())
    adj[s][t] = min(adj[s][t], cost)
nxt = [[0 for _ in range(n + 1)] for _ in range(n + 1)]


def init_nxt(adj, nxt):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if adj[i][j] != maxsize:
                nxt[i][j] = j


def floyd(adj, nxt):
    for i in range(1, n + 1):
        adj[i][i] = 0
    for v in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if adj[i][j] > (adj[i][v] + adj[v][j]):
                    adj[i][j] = adj[i][v] + adj[v][j]
                    nxt[i][j] = nxt[i][v]


init_nxt(adj, nxt)
floyd(adj, nxt)

for line in adj[1:]:
    for val in line[1:]:
        if val in (0, maxsize):
            print(0, end=" ")
        else:
            print(val, end=" ")
    print()

# [i][j]도시의 경로 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if adj[i][j] in (0, maxsize):
            print(0)
            continue
        path = []
        start = i
        while start != j:
            path.append(start)
            start = nxt[start][j]
        path.append(j)
        print(len(path), *path, sep=" ")