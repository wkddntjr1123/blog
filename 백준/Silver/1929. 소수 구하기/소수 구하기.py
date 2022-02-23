from sys import stdin

input = stdin.readline

m, n = map(int, input().split())

check = [True for _ in range(n + 1)]
check[1] = False
for i in range(2, int(n ** (1 / 2)) + 1):
    if check[i]:
        for j in range(i**2, n + 1, i):
            check[j] = False

for i in range(m, n + 1):
    if check[i]:
        print(i)