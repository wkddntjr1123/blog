from collections import Counter
from sys import stdin


input = stdin.readline

n = int(input())
table = Counter()
for _ in range(n):
    _, suffix = input().split(".")
    table[suffix.rstrip("\n")] += 1
for k in sorted(table.keys()):
    print(k, table[k], sep=" ")