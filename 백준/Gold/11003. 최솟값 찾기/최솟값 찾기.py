from heapq import heappush, heappop
from sys import stdin
from typing import Counter

input = stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))
heap = []  # 최소힙
table = Counter()
answer = []
for i in range(len(arr)):
    table[arr[i]] += 1
    if table[arr[i]] == 1:  # 새로 들어온 값이면 최소힙에 넣기
        heappush(heap, arr[i])
    if i - l >= 0:
        table[arr[i - l]] -= 1
    while table[heap[0]] == 0:  # 윈도우 범위(L)에서 벗어난 값 제거
        heappop(heap)
    answer.append(heap[0])
print(*answer)