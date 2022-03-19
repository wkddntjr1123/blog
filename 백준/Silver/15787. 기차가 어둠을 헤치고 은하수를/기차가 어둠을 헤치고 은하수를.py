from collections import defaultdict
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

train = defaultdict(int)

for _ in range(m):
    order = tuple(map(int, input().split()))
    if order[0] == 1:
        train[order[1] - 1] |= 1 << (order[2] - 1)
    elif order[0] == 2:
        train[order[1] - 1] &= ~(1 << (order[2] - 1))
    elif order[0] == 3:
        train[order[1] - 1] <<= 1
        train[order[1] - 1] &= ~(1 << 20)
    elif order[0] == 4:
        train[order[1] - 1] >>= 1

res = set()
for i in range(n):
    res.add(train[i])
print(len(res))