from heapq import heappush, heappop
from collections import defaultdict
from sys import maxsize, stdin

input = stdin.readline
for _ in range(int(input())):
    operations = [input().rstrip() for _ in range(int(input()))]
    min_q, max_q = [], []
    table = defaultdict(int)
    for item in operations:
        op, val = item.split()
        val = int(val)
        if op == "I":
            heappush(min_q, val)
            heappush(max_q, -val)
            table[val] += 1
        else:
            while val == -1 and min_q:
                pop_val = heappop(min_q)
                if table[pop_val] > 0:
                    table[pop_val] -= 1
                    break
            while val == 1 and max_q:
                pop_val = -heappop(max_q)
                if table[pop_val] > 0:
                    table[pop_val] -= 1
                    break
    max_res, min_res = -maxsize, maxsize
    for k, v in table.items():
        if v > 0:
            max_res, min_res = max(max_res, k), min(min_res, k)
    if max_res == -maxsize:
        print("EMPTY")
    else:
        print(max_res, min_res)
