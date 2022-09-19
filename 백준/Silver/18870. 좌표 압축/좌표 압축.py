from sys import stdin

input = stdin.readline


def biLeft(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if target <= arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


n = int(input())
arr = list(map(int, input().split()))
sortedArr = sorted(set(arr))


for num in arr:
    print(biLeft(sortedArr, num), end=" ")
