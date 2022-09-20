from sys import maxsize, stdin


input = stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left = right = 0
min_res = maxsize
while True:
    if right == n:
        break
    if left == right:
        right += 1
        continue
    if arr[right] - arr[left] >= m:
        min_res = min(min_res, arr[right] - arr[left])
        left += 1
    else:
        right += 1
print(min_res) if m != 0 else print(0)