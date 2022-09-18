from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
table = [1 for _ in range(n)]

for i in range(1, n):
    maxVal = 0
    for j in range(0, i):
        if arr[i] < arr[j]:
            maxVal = max(maxVal, table[j])
    table[i] = maxVal + 1
print(max(table))
