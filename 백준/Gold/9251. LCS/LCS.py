from sys import stdin

input = stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
table = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i][j - 1], table[i - 1][j])

print(max(map(max, table)))