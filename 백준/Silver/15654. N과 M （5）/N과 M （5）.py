from itertools import permutations
from sys import stdin


input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for item in permutations(arr, m):
    print(*item, sep=" ")
