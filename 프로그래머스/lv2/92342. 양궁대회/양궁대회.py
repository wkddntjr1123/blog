from collections import Counter
from itertools import combinations_with_replacement


def comp(data, avail):
    data_val = avail_val = 0
    for i in range(11):
        if avail[i] > data[i]:
            avail_val += i
        else:
            if data[i] == 0:
                continue
            else:
                data_val += i
    return avail_val - data_val


def create_arr(avail):
    res = []
    for i in range(11):
        if avail[i]:
            res.append(avail[i])
        else:
            res.append(0)
    return res


def comp_two_arr(arr1, arr2):
    for i in range(11):
        if arr1[i] == arr2[i]:
            continue
        elif arr1[i] > arr2[i]:
            return arr1
        else:
            return arr2


def solution(n, info):
    info = info[::-1]
    data = Counter()
    for i in range(11):
        if info[i] != 0:
            data[i] = info[i]
    most_gap = -1
    answer = [-1]
    for item in combinations_with_replacement(range(11), n):  # n개 화살쏴서 맞춘 과녁의 수
        avail = Counter(item)
        gap = comp(data, avail)
        if gap <= 0:
            continue
        else:
            temp = create_arr(avail)
            if gap > most_gap:
                most_gap = gap
                answer = temp
            else:
                answer = comp_two_arr(temp, answer)
    return answer[::-1]