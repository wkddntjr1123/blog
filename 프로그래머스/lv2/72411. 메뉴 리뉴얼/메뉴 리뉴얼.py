from collections import Counter, defaultdict
from itertools import combinations


def solution(orders, course):
    res = defaultdict(Counter)
    orders.sort()
    for i in range(len(orders)):
        orders[i] = "".join(sorted(orders[i]))
    for order in orders:
        for length in course:
            for item in combinations(order, length):
                res[length]["".join(item)] += 1
    answer = []
    for length in course:
        c = res[length]
        if len(c) == 0:
            continue
        arr = c.most_common()
        max_size = arr[0][1]
        if max_size < 2:
            continue
        for item in arr:
            if item[1] != max_size:
                break
            answer.append(item[0])
    answer.sort()
    return answer