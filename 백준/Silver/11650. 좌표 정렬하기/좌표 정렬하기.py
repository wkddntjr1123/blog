from sys import stdin


input = lambda: stdin.readline().rstrip()
arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda pos: (pos[0], pos[1]))
for pos in arr:
    print(pos[0], pos[1])