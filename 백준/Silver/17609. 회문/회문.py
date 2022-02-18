from sys import stdin

input = stdin.readline

def check(s, l, r, first) -> bool:
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if first:
                if check(s, l + 1, r, False) or check(s, l, r - 1, False):
                    return True
                else:
                    return False
            else:
                return False
    return True

n = int(input())

for _ in range(n):
    s = input().rstrip()
    if s == s[::-1]:
        print(0)
    elif check(s, 0, len(s) - 1, True):
        print(1)
    else:
        print(2)
