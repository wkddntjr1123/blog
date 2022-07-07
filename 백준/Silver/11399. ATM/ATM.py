from sys import stdin

input = stdin.readline

input()
arr = list(map(int, input().split()))
arr.sort()
answer = 0
start = len(arr)
for num in arr:
    answer += num * start
    start -= 1
print(answer)