s = input()
s = s.split("::")


def restore(sub_str):
    return ":".join(list(map(lambda x: x.rjust(4, "0"), sub_str.split(":"))))


if len(s) == 1:
    print(restore(s[0]))
else:
    sub_str1, sub_str2 = s
    if not sub_str1 and not sub_str2:
        res = "0000:0000:0000:0000:0000:0000:0000:0000"
    elif not sub_str2:
        res = restore(sub_str1)
        while len(res) != 39:
            res += ":0000"
    elif not sub_str1:
        res = restore(sub_str2)
        while len(res) != 39:
            res = "0000:" + res
    else:
        front = restore(sub_str1) + ":"
        back = ":" + restore(sub_str2)
        mid = "0000"
        while len(front) + len(back) + len(mid) != 39:
            mid += ":0000"
        res = front + mid + back
    print(res)