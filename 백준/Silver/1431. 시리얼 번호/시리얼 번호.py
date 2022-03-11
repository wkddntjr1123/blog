from sys import stdin
import re

input = stdin.readline

n = int(input())
str_list = []
for _ in range(n):
    str_list.append(input().rstrip())

str_list.sort(key=lambda x: (len(x), sum(map(int, re.findall("\d", x))), x))


print(*str_list, sep="\n", end="")