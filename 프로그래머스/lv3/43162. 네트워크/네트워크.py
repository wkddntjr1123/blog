def dfs(graph, v, visited):
    visited[v] = True
    for nv in graph[v]:
        if not visited[nv]:
            dfs(graph, nv, visited)


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    visited = [False for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            dfs(graph, v, visited)
            answer += 1
    return answer