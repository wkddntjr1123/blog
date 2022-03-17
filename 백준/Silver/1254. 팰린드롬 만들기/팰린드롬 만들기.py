from sys import stdin


input = stdin.readline

s = input().rstrip()

idx = len(s) - 1
for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        idx = i
        break
print(len(s) + i)