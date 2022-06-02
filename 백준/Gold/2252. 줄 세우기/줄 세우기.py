from collections import deque
from sys import stdin

input = stdin.readline
num_v, m = map(int, input().split())
# 인접리스트
adj_list = [[] for _ in range(num_v + 1)]
# 각 정점의 indgree 개수를 저장
indgree = [0 for _ in range(num_v + 1)]
for _ in range(m):
    s, t = map(int, input().split())
    adj_list[s].append(t)
    indgree[t] += 1


# indgree가 0이면 q에 추가
q = deque()
for v in range(1, num_v + 1):
    if indgree[v] == 0:
        q.append(v)
result = []
while q:
    v = q.popleft()
    result.append(v)
    for to_v in adj_list[v]:
        indgree[to_v] -= 1
        if indgree[to_v] == 0:
            q.append(to_v)
print(" ".join(map(str, result)))