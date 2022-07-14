from sys import stdin


input = lambda: stdin.readline().rstrip()

arr = set([input() for _ in range(int(input()))])
arr = sorted(arr, key=lambda s: (len(s), s))
print(*arr, sep="\n")