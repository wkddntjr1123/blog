from sys import stdin, setrecursionlimit

setrecursionlimit(999999999)


input = stdin.readline

n = int(input())
lc = [-1 for _ in range(n + 1)]
rc = [-1 for _ in range(n + 1)]
for _ in range(n):
    v, left, right = map(int, input().split())
    lc[v] = left
    rc[v] = right


end_node = 1
while rc[end_node] != -1:
    end_node = rc[end_node]

res = []


def func(v):
    res.append(v)
    if lc[v] != -1:
        func(lc[v])
        res.append(v)
    if rc[v] != -1:
        func(rc[v])
        res.append(v)


func(1)

r_idx = len(res) - 1
for i in range(len(res) - 1, -1, -1):
    if res[i] == end_node:
        r_idx = i
        break
print(r_idx)
