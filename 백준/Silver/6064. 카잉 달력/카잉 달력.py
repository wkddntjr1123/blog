from math import gcd
from sys import stdin

input = stdin.readline

test_num = int(input())


def process(m, n, target_x, target_y):
    end = m * n // gcd(m, n)
    if m == target_x and n == target_y:
        return end
    if target_x == m:
        target_x = 0
    if target_y == n:
        target_y = 0
    avail_x = []
    i = 0
    while True:
        if m * i + target_x > end:
            break
        avail_x.append(m * i + target_x)
        i += 1
    for val in avail_x:
        if val % n == target_y:
            return val
    return -1


for _ in range(test_num):
    print(process(*map(int, input().split())))
