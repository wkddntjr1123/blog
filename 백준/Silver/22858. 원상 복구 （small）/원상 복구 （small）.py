np, nk = map(int, input().split())
s = [-1] + list(map(int, input().split()))
d = [-1] + list(map(int, input().split()))
p = [0 for _ in range(len(s))]
for i in range(nk):
    for i in range(len(s)):
        p[d[i]] = s[i]
    s = p[:]
    p = [0 for _ in range(len(s))]

print(*s[1:])
