from bisect import bisect_left
from sys import stdin

input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for start in range(n - 2):
    left, right = start + 1, n - 1
    while left < right:
        value = arr[start] + arr[left] + arr[right]
        if value > 0:
            right -= 1
        elif value < 0:
            left += 1
        else:
            idx = bisect_left(arr, arr[right], lo=left + 1, hi=right)
            answer += right - idx + 1
            left += 1

print(answer)