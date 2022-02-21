from sys import stdin


input = stdin.readline

n = int(input())
schedule = [0] * 367
for _ in range(n):
    s, t = map(int, input().split())
    for i in range(s, t + 1):
        schedule[i] += 1

seq = col = res = 0
for i in range(1, 367):
    if schedule[i] != 0:
        seq += 1
        col = max(col, schedule[i])
    else:
        res += seq * col
        seq = 0
        col = 0
print(res)
