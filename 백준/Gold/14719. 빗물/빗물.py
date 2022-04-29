from sys import stdin


input = stdin.readline

input()
arr = list(map(int, input().split()))

l, r = 0, len(arr) - 1
l_max, r_max = arr[0], arr[-1]
res = 0
while l < r:
    if l_max < r_max:
        l += 1
        val = min(l_max, r_max) - arr[l]
        l_max = max(l_max, arr[l])
    else:
        r -= 1
        val = min(l_max, r_max) - arr[r]
        r_max = max(r_max, arr[r])
    if val > 0:
        res += val
print(res)
