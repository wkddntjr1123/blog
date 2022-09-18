from sys import stdin

input = stdin.readline

n, m, l = map(int, input().split())
arr = [0] + (list(map(int, input().split()))) + [l]
arr.sort()


def getDividedCount(arr, divValue):
    count = 0
    for i in range(1, n + 2):
        count += (arr[i] - arr[i - 1] - 1) // divValue
    return count


for x in range(1, 1001):
    if getDividedCount(arr, x) <= m:
        print(x)
        exit()
