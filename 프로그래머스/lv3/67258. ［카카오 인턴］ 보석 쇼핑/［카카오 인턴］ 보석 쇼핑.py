from collections import defaultdict


def solution(gems):
    answer = []
    MAX_GEM = len(set(gems))
    gemSort = set()
    gemCount = defaultdict(int)
    l, r = 0, 0
    maxAnswer = [0, 20000000]
    while l < len(gems):
        if l == r:
            gemCount[gems[r]] += 1
            gemSort.add(gems[r])
            r += 1
            continue
        if len(gemSort) == MAX_GEM:
            bl, br = maxAnswer
            if br - bl > r - l:
                maxAnswer = [l, r]
            gemCount[gems[l]] -= 1
            if gemCount[gems[l]] == 0:
                gemSort.remove(gems[l])
            l += 1
        else:
            if r == len(gems):
                break
            gemCount[gems[r]] += 1
            gemSort.add(gems[r])
            r += 1
    return [maxAnswer[0] + 1, maxAnswer[1]]