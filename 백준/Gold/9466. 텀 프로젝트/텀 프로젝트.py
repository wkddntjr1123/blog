from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)

input = stdin.readline


def dfs(v, log, route):
    if visited[v]:
        return log
    if v in log:
        global answer
        answer -= len(log) - route.index(v)
        return log
    log.add(v)
    route.append(v)
    return dfs(students[v], log, route)


for _ in range(int(input())):
    n = int(input())
    students = [-1] + list(map(int, input().split()))
    visited = [False for _ in range(n + 1)]
    answer = n
    for v in range(1, len(students)):
        if not visited[v]:
            result = dfs(v, set(), [])
            for nv in result:
                visited[nv] = True
    print(answer)