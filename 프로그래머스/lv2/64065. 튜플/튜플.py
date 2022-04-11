from collections import Counter


def input_to_list(s):
    arr = []
    for item in s[1:-1].split("},"):
        item = item.replace("{", "")
        if item[-1] == "}":
            item = item[:-1]
        arr.append(set(map(int, item.split(","))))
    arr.sort(key=len)
    return arr


def solution(s):
    arr = input_to_list(s)
    c = Counter()
    for item in arr:
        for num in item:
            c[num] += 1

    return [item[0] for item in c.most_common()]