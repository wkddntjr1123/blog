import heapq
from sys import stdin


input = stdin.readline
n = int(input())
m_heap = []
for _ in range(n):
    op = int(input())
    if op == 0:  # pop
        print(heapq.heappop(m_heap)[1]) if m_heap else print(0)
    else:  # push
        heapq.heappush(m_heap, (abs(op), op))