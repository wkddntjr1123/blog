from sys import stdin
from functools import cmp_to_key

input = stdin.readline

arr = [input().rstrip() for _ in range(int(input()))]


def compare(a, b):
    if len(a) != len(b):
        return len(a) - len(b)
    numberConverter = lambda c: int(c) if c.isdigit() else 0
    sumA = sum(map(numberConverter, a))
    sumB = sum(map(numberConverter, b))
    if sumA != sumB:
        return sumA - sumB
    return -1 if a < b else 0


arr.sort(key=cmp_to_key(compare))

print("\n".join(arr))
