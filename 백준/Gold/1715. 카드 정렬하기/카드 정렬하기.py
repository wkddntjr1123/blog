import heapq
from sys import stdin

input = stdin.readline

n = int(input())
min_heap = []
for _ in range(n):
    heapq.heappush(min_heap, int(input()))
result = 0
while len(min_heap) != 1:
    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)
    result += a + b
    heapq.heappush(min_heap, (a + b))

print(result)