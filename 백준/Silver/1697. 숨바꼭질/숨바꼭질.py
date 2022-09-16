from collections import deque

n, m = map(int, input().split())

def process():
    dist = [False for _ in range(100002)]
    q = deque()
    q.append(n)
    dist[n] = 0
    while q:
        x = q.popleft()
        if x == m:
            return dist[x]
        for num in (x - 1, x + 1, x * 2):
            if num < 0 or num > 100000:
                continue
            if not dist[num]:
                dist[num] = dist[x] + 1
                q.append(num)

print(process())