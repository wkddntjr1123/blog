from bisect import bisect_left
from sys import maxsize, stdin

input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))

answer = maxsize
for start in range(len(arr) - 1):
    lower_bound = bisect_left(arr, -arr[start], lo=start + 1)
    for right in (lower_bound - 1, lower_bound):
        if start < right < n and (abs(arr[right] + arr[start]) < abs(answer)):
            answer = arr[right] + arr[start]
print(answer)