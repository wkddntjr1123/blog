import heapq
from sys import stdin

input = stdin.readline

heap = []
for _ in range(int(input())):
    op = int(input())
    if op == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -op)