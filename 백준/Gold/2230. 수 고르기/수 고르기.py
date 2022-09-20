from sys import maxsize, stdin

input = stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
answer = maxsize

l, r = 0, 0
while r < len(arr):
    if l == r:
        r += 1
        continue
    dist = arr[r] - arr[l]
    if m <= dist:
        answer = min(answer, dist)
        l += 1
    else:
        r += 1

print(0 if answer == maxsize and m == 0 else answer)
