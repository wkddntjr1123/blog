from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)


def dfs(v):
    global answer
    if not graph[v]:  # 리프노드 경우
        return 0
    child = []
    for nv, ncost in graph[v]:
        child.append(dfs(nv) + ncost)
    child.sort(reverse=True)
    if len(child) > 1:
        answer = max(answer, child[0] + child[1])
    answer = max(answer, child[0])
    return child[0]


input = lambda: stdin.readline().rstrip()

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
answer = 0
dfs(1)
print(answer)