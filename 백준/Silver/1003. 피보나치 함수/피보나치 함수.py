from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    table = [False for _ in range(n + 3)]
    table[0] = (1, 0)
    table[1] = (0, 1)
    table[2] = (1, 1)
    for i in range(3, n + 1):
        table[i] = (
            table[i - 1][0] + table[i - 2][0],
            table[i - 1][1] + table[i - 2][1],
        )
    print(*table[n])