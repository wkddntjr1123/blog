from sys import stdin


input = stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

# n^2
two_sum_set = set()
for i in range(n):
    for j in range(n):
        two_sum_set.add(arr[i] + arr[j])


max_result = 0
# n^2
for i in range(n):
    for j in range(i + 1, n):
        if arr[j] - arr[i] in two_sum_set:  # O(1)
            max_result = max(max_result, arr[j])
print(max_result)