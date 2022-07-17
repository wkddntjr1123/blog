from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)


def find_leaf(v):
    q = deque([v])
    visited = set([v])
    while q:
        v = q.popleft()
        for nv, _ in graph[v]:
            if nv not in visited:
                q.append(nv)
                visited.add(nv)
    return v


def dfs(v, visited):
    visited.add(v)
    global answer
    child = []
    for nv, ncost in graph[v]:
        if nv not in visited:
            child.append(dfs(nv, visited) + ncost)
            visited.add(nv)
    if not child:
        return 0
    child.sort(reverse=True)
    if len(child) > 1:
        answer = max(answer, child[0] + child[1])
    answer = max(answer, child[0])
    return child[0]


input = lambda: stdin.readline().rstrip()

n = int(input())
graph = [set() for _ in range(n + 1)]
for _ in range(n - 1):
    info = list(map(int, input().split()))
    for i in range(1, len(info) - 1, 2):
        graph[info[0]].add((info[i], info[i + 1]))
        graph[info[i]].add((info[0], info[i + 1]))
answer = 0
dfs(find_leaf(1), set())  # 양방향이므로 리프 노드에서 시작하면서 방문처리
print(answer)