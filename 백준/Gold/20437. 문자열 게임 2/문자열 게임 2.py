from collections import defaultdict
from sys import maxsize, stdin

input = stdin.readline
n = int(input())
for _ in range(n):
    s = input().rstrip()
    k = int(input())

    table = defaultdict(list)
    min_len = maxsize
    max_len = 0
    for idx, char in enumerate(s):
        table[char].append(idx)
        if len(table[char]) >= k:
            length = table[char][-1] - table[char][-k] + 1
            min_len = min(min_len, length)
            max_len = max(max_len, length)
    if min_len == maxsize:
        print(-1)
    else:
        print(min_len, max_len)
