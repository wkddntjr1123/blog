from sys import stdin


input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

max_len = 2
for i in range(n):  # 0 1 2
    for j in range(n - 1, i + 1, -1):  # 2
        if arr[i] + arr[i + 1] > arr[j]:
            max_len = max(max_len, j - i + 1)
if len(arr) in (1, 2):
    print(len(arr))
else:
    print(max_len)
