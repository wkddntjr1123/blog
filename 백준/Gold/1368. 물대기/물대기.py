from sys import stdin


input = stdin.readline

n = int(input())

edges = []
for i in range(1, n + 1):
    edges.append((i, n + 1, int(input())))  # 우물 비용

graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        edges.append((i + 1, j + 1, graph[i][j]))  # u,v,cost

edges.sort(key=lambda x: x[2])  # cost 정렬
n += 1

# 크루스칼
parent = [-1 for _ in range(n + 1)]


def find(v):
    buffer = []
    while parent[v] >= 0:  # v가 루트노드가 아니면
        buffer.append(v)
        v = parent[v]
    for i in buffer:
        parent[i] = v
    return v


def is_same_group(u, v):
    u, v = find(u), find(v)
    if u == v:
        return True
    if parent[u] > parent[v]:  # 항상 u의 높이가 더 높도록 스왑
        u, v = v, u
    if parent[u] == parent[v]:
        parent[u] -= 1  # 높이 1 증가
    parent[v] = u  # union
    return False


cnt = result = 0
for edge in edges:  # 작은 정점부터 쭉 순회
    u, v, cost = edge
    if not is_same_group(u, v):  # 같은 그룹이 아니면
        result += cost
        cnt += 1
    if cnt == n - 1:
        break

print(result)
