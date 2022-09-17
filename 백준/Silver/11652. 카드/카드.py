from sys import stdin


input = stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

max_count = 0
max_num = None
count = 0
for i in range(n):
    if i == n - 1:
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max_num = nums[i]
        break
    if nums[i] == nums[i + 1]:
        count += 1
    else:
        count += 1
        if count > max_count:
            max_count = count
            max_num = nums[i]
        count = 0
print(max_num)
