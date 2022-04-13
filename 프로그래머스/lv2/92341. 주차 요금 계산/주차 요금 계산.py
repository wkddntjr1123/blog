from collections import defaultdict
from datetime import datetime
from math import ceil


def calc_time(prev, next):
    gap = datetime.strptime(next, "%H:%M") - datetime.strptime(prev, "%H:%M")
    return int((gap.days * 24 * 60) + (gap.seconds / 60))


def solution(fees, records):
    # 기본시간, 기본요금, 단위시간, 단위요금
    standard_time, default_cost, time_slot, slot_cost = map(int, fees)
    table = defaultdict(list)
    for record in records:
        [time, number, state] = record.split()
        if state == "IN":
            table[number].append(time)
        else:
            prev_time = table[number].pop()
            table[number].append(calc_time(prev_time, time))

    for key in table:
        if type(table[key][-1]) == str:
            table[key].append(calc_time(table[key].pop(), "23:59"))
        sum_minute = sum(table[key])
        if sum_minute <= standard_time:
            table[key] = default_cost
        else:
            table[key] = ceil((sum_minute - standard_time) / time_slot) * slot_cost + default_cost
    keys = sorted(table.keys())
    answer = [table[key] for key in keys]
    return answer