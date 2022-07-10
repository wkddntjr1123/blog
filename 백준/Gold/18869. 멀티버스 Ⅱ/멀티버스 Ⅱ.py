from collections import defaultdict
from sys import stdin

input = stdin.readline

m, n = map(int, input().split())
table = defaultdict(int)
for _ in range(m):
    planets = list(map(int, input().split()))
    reverse_mapping = {value: idx for idx, value in enumerate(sorted(set(planets)))}
    table[tuple(reverse_mapping[num] for num in planets)] += 1
answer = 0
for v in table.values():
    if v >= 2:
        answer += v * (v - 1) // 2
print(answer)