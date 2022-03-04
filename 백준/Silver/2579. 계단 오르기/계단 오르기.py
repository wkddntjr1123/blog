from sys import stdin


input = stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.reverse()

table = [[0, 0] for _ in range(n)]
table[0][0] = arr[0]
if n >= 2:
    table[1][1] = arr[0] + arr[1]
if n >= 3:
    table[2][0] = arr[0] + arr[2]
for i in range(3, n):
    table[i][0] = max(table[i - 2][0], table[i - 2][1]) + arr[i]
    table[i][1] = table[i - 1][0] + arr[i]

print(max(map(max, table)))