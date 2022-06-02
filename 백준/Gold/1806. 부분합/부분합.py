from sys import maxsize, stdin


input = stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = right = 0
min_len = maxsize
temp_sum = 0
while True:
    if temp_sum < s:
        if right == n:
            break
        temp_sum += arr[right]
        right += 1
    else:
        min_len = min(min_len, right - left)
        temp_sum -= arr[left]
        left += 1
        if left == n:
            break
print(min_len) if min_len != maxsize else print(0)