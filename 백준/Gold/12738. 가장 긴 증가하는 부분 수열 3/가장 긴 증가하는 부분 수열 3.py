from bisect import bisect_left
from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

table = [arr[0]]
for i in range(1, n):
    if table[-1] < arr[i]:
        table.append(arr[i])
        continue
    insertIdx = bisect_left(table, arr[i])
    table[insertIdx] = arr[i]

print(len(table))
