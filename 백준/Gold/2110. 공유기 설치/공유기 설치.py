from sys import stdin


input = lambda: stdin.readline().rstrip()
n, m = map(int, input().split())

pos = [int(input()) for _ in range(n)]
pos.sort()

start = 1
end = pos[-1] - pos[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    prev = pos[0]
    count = 1

    for i in range(1, len(pos)):
        if pos[i] >= prev + mid:
            count += 1
            prev = pos[i]

    if count >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)