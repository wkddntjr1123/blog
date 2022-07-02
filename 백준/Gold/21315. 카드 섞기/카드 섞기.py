from itertools import product
from math import log
from sys import stdin

input = stdin.readline


def shuffle(cards, k):
    if k == 0:
        return cards[::-1]
    return shuffle(cards[-(2**k) :], k - 1) + cards[: len(cards) - 2**k]


n = int(input())
end_cards = list(map(int, input().split()))
origin_cards = [i for i in range(1, n + 1)]

case = product(range(1, int(log(n, 2)) + 1), repeat=2)
for i, j in case:
    if end_cards == shuffle(shuffle(origin_cards, i), j):
        print(i, j)
        break
