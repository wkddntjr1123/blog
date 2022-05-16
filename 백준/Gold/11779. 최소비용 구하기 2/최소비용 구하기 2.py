from collections import deque
import heapq
from sys import stdin, maxsize

input = stdin.readline

num_v = int(input())
num_e = int(input())
# 인접리스트
adj = [[] for _ in range(num_v + 1)]
for _ in range(num_e):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
# 거리
dist = [maxsize for _ in range(num_v + 1)]
# 경로 : 정점의 이전 경로를 저장
path = [False for _ in range(num_v + 1)]
heap = []


def dijkstra(start_v):
    heapq.heappush(heap, (0, start_v))
    dist[start_v] = 0
    path[start_v] = 0
    while heap:
        to_center_cost, center = heapq.heappop(heap)
        if dist[center] != to_center_cost:
            continue
        for item in adj[center]:
            to, cost = item
            if dist[to] > cost + to_center_cost:
                dist[to] = cost + to_center_cost
                path[to] = center
                heapq.heappush(heap, (dist[to], to))


start, end = map(int, input().split())
dijkstra(start)
print(dist[end])
path_list = deque()
while end != 0:
    path_list.appendleft(end)
    end = path[end]
print(len(path_list))
print(*path_list, sep=" ")