from sys import stdin
from itertools import product

input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for item in product(arr,repeat=m):
    print(*item,sep=" ")
