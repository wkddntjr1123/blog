from collections import deque
from sys import stdin

input = stdin.readline

num_v, num_e, start_v = map(int, input().split())

adj_list = [[] for _ in range(num_v + 1)]
for _ in range(num_e):
    s, t = map(int, input().split())
    adj_list[s].append(t)
    adj_list[t].append(s)
for l in adj_list:
    l.sort()
visited_bfs = [False for _ in range(num_v + 1)]
visited_dfs = [False for _ in range(num_v + 1)]

def dfs(v):
    s = []
    s.append(v)
    while s:
        v = s.pop()
        if visited_dfs[v]:
            continue
        visited_dfs[v] = True
        print(v, end=" ")
        for next_v in adj_list[v][::-1]:
            if not visited_dfs[next_v]:
                s.append(next_v)

def bfs(v):
    q = deque()
    q.append(v)
    visited_bfs[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for next_v in adj_list[v]:
            if not visited_bfs[next_v]:
                q.append(next_v)
                visited_bfs[next_v] = True

dfs(start_v)
print()
bfs(start_v)