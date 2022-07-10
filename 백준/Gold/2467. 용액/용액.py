from bisect import bisect_left
from sys import maxsize, stdin

input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))

min_val = maxsize
min_a, min_b = -maxsize, maxsize
for i in range(n - 1):
    right = bisect_left(arr, -arr[i], lo=i + 1)
    for r_idx in (right - 1, right):
        if i < r_idx < n:
            if abs(arr[i] + arr[r_idx]) < min_val:
                min_val = abs(arr[i] + arr[r_idx])
                min_a, min_b = arr[i], arr[r_idx]
print(min_a, min_b)
