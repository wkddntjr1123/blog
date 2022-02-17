from itertools import product
from sys import stdin


input = stdin.readline

to, count = map(int, input().split())

for item in product(range(1, to + 1), repeat=count):
    print(*item, sep=" ")
