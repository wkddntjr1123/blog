from sys import stdin


input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())
if m > n / 2:
    m = n - m
upper = 1
bottom = 1
for num in range(n, n - m, -1):
    upper *= num
for num in range(2, m + 1):
    bottom *= num
print(upper // bottom)