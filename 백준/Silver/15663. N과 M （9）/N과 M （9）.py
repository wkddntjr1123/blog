from itertools import permutations
from sys import stdin


input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = set()
for item in permutations(arr, m):
    res.add(item)

for item in sorted(res):
    print(*item, sep=" ")
