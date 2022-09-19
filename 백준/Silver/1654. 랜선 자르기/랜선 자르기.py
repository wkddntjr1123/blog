from sys import stdin

input = stdin.readline

k, target = map(int, input().split())
lines = [int(input()) for _ in range(k)]


def getCount(lines, length):
    return sum(map(lambda line: line // length, lines))


def biLeft(lines, target):
    lo, hi = 1, max(lines)
    while lo <= hi:
        cutLength = (lo + hi) // 2
        if target > getCount(lines, cutLength):
            hi = cutLength - 1
        else:
            lo = cutLength + 1
    return hi


print(biLeft(lines, target))
