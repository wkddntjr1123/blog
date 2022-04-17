from math import ceil


def solution(progresses, speeds):
    res = []  # item : [day, count]
    for process, speed in zip(progresses, speeds):
        day = ceil((100 - process) / speed)
        if not res or res[-1][0] < day:
            res.append([day, 1])
        else:
            res[-1][1] += 1
    return [item[1] for item in res]