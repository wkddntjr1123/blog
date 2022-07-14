from sys import stdin


input = lambda: stdin.readline().rstrip()

arr = [input().split() for _ in range(int(input()))]
arr.sort(key=lambda item: int(item[0]))
for item in arr:
    print(*item)