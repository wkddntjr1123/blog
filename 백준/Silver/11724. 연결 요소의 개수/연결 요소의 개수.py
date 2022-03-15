from sys import stdin

input = stdin.readline

num_v, num_e = map(int, input().split())

adj_list = [[] for _ in range(num_v + 1)]
for _ in range(num_e):
    s, t = map(int, input().split())
    adj_list[s].append(t)
    adj_list[t].append(s)
visited = [False for _ in range(num_v + 1)]


def dfs(v):
    visited[v] = True
    for next_v in adj_list[v]:
        if not visited[next_v]:
            dfs(next_v)


result = 0
for v in range(1, num_v + 1):
    if not visited[v]:
        result += 1
        dfs(v)
print(result)