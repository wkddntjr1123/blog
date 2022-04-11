from bisect import bisect_left


def solution(citations):
    answer = 0
    citations.sort()
    for i in range(1, len(citations) + 1):
        if len(citations) - bisect_left(citations, i) >= i:
            answer = i
    return answer