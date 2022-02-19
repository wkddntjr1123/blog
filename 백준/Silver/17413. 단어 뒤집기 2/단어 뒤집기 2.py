from sys import stdin

input = stdin.readline
s = list(input().rstrip())

i = 0
while i < len(s):
    if s[i] == "<":
        while s[i] != ">":
            i += 1
        i += 1
    elif s[i] == " ":
        i += 1
    else:
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        s[start:i] = s[start:i][::-1]

print("".join(s))