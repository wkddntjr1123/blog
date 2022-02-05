from sys import maxsize, stdin


input = stdin.readline

x = int(input())
table = [-1 for _ in range(x + 1)]
table[1] = 0
for i in range(2, x + 1):
    table[i] = (
        min(
            table[i - 1],
            table[i // 2] if i % 2 == 0 else maxsize,
            table[i // 3] if i % 3 == 0 else maxsize,
        )
        + 1
    )
print(table[x])