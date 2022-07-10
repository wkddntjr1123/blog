from bisect import bisect_left
from sys import maxsize, stdin

input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))

min_val = maxsize
min_a, min_b = -maxsize, maxsize
for i in range(n - 1):
    r_idx = bisect_left(arr, -arr[i], lo=i + 1)
    if r_idx >= n:
        r_idx -= 1
    if r_idx == i:
        continue
    if abs(arr[i] + arr[r_idx]) < min_val:
        min_val = abs(arr[i] + arr[r_idx])
        min_a, min_b = arr[i], arr[r_idx]
    if r_idx > 0:
        r_idx -= 1
    if r_idx == i:
        continue
    if abs(arr[i] + arr[r_idx]) < min_val:
        min_val = abs(arr[i] + arr[r_idx])
        min_a, min_b = arr[i], arr[r_idx]
print(min_a, min_b)