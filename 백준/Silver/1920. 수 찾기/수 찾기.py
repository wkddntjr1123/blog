from sys import stdin

input = stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))


def bin_search(arr, target, st, en):
    while st <= en:
        mid = (st + en) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    return -1


for target in arr2:
    print(0) if bin_search(arr1, target, 0, n - 1) == -1 else print(1)
