from sys import stdin

input = stdin.readline

a, b = map(int, input().split())
res = set([input().rstrip() for _ in range(a)]) & set([input().rstrip() for _ in range(b)])
print(len(res))
print(*sorted(res), sep="\n")