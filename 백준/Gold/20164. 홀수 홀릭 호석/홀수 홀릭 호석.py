from sys import maxsize, stdin


input = stdin.readline

num = input().rstrip()


def count_odd(num):
    cnt = 0
    for char in num:
        if int(char) % 2 == 1:
            cnt += 1
    return cnt


min_answer = maxsize
max_answer = 0


def func(num, cnt):
    cnt += count_odd(num)
    if len(num) == 1:
        global min_answer, max_answer
        min_answer = min(min_answer, cnt)
        max_answer = max(max_answer, cnt)
        return
    elif len(num) == 2:
        func(str(int(num[0]) + int(num[1])), cnt)
    else:
        for i in range(len(num) - 2):
            for j in range(i + 1, len(num) - 1):
                func(str(int(num[: i + 1]) + int(num[i + 1 : j + 1]) + int(num[j + 1 :])), cnt)


func(num, 0)
print(min_answer, max_answer)
