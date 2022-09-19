from bisect import bisect_left, bisect_right
from sys import stdin

input = stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))

for target in arr2:
    left_idx = bisect_left(arr1, target)
    right_idx = bisect_right(arr1, target)
    print(right_idx - left_idx, end=" ")