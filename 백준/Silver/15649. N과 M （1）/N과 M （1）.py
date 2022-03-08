from itertools import permutations
from sys import stdin


input = stdin.readline

to, count = map(int, input().split())

for item in permutations(range(1, to + 1), count):
    print(*item, sep=" ")
