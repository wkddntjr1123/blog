from sys import stdin

input = stdin.readline

n = int(input())
meets = [tuple(map(int, input().split())) for _ in range(n)]

meets.sort(key=lambda item: (item[1], item[0]))

end_time = 0
cnt = 0
for meet in meets:
    if meet[0] < end_time:
        continue
    end_time = meet[1]
    cnt += 1
print(cnt)