from math import ceil


def solution(n, stations, w):
    # 앞
    none_area_len = stations[0] - w - 1
    front = ceil(none_area_len / (2 * w + 1))
    # 뒤
    none_area_len = n - (stations[-1] + w)
    back = ceil(none_area_len / (2 * w + 1))
    # 사이사이
    sisi = 0
    if len(stations) > 1:
        for i in range(len(stations) - 1):
            none_area_len = (stations[i + 1] - w - 1) - (stations[i] + w + 1) + 1
            sisi += ceil(none_area_len / (2 * w + 1))
    return front + back + sisi