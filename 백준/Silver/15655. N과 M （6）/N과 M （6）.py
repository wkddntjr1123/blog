from itertools import combinations
from sys import stdin


input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for item in combinations(arr, m):
    print(*item, sep=" ")
