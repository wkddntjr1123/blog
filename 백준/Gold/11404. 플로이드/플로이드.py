from sys import maxsize, stdin

input = stdin.readline

n = int(input())
m = int(input())
adj = [[maxsize for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    s, t, cost = map(int, input().split())
    if not adj[s][t] or adj[s][t] > cost:
        adj[s][t] = cost


def floyd(adj):
    for v in range(1, n + 1):
        for i in range(1, n + 1):
            if i == v:
                continue
            for j in range(1, n + 1):
                if i == j or j == v:
                    continue
                if adj[i][j] > (adj[i][v] + adj[v][j]):
                    adj[i][j] = adj[i][v] + adj[v][j]


test = [
    [maxsize, maxsize, maxsize, maxsize, maxsize, maxsize],
    [maxsize, maxsize, 4, 1, 1, maxsize],
    [maxsize, 4, maxsize, maxsize, maxsize, 8],
    [maxsize, 1, maxsize, maxsize, 3, 15],
    [maxsize, 1, maxsize, 3, maxsize, 6],
    [maxsize, maxsize, 8, 15, 6, maxsize],
]
floyd(adj)
for line in adj[1:]:
    for val in line[1:]:
        if val == maxsize:
            print(0, end=" ")
        else:
            print(val, end=" ")
    print()