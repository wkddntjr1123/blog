from bisect import bisect_left
from collections import defaultdict


def solution(words, queries):
    answer = []
    table, reverse_table = defaultdict(list), defaultdict(list)
    for word in words:
        table[len(word)].append(word)
        reverse_table[len(word)].append(word[::-1])
    for k in table:
        table[k].sort()
        reverse_table[k].sort()
    for query in queries:
        if query[0] == "?":
            target = reverse_table[len(query)]
            answer.append(
                bisect_left(target, query[::-1].replace("?", "z"))
                - bisect_left(target, query[::-1].replace("?", "a"))
            )
        else:
            target = table[len(query)]
            answer.append(
                bisect_left(target, query.replace("?", "z"))
                - bisect_left(target, query.replace("?", "a"))
            )
    return answer