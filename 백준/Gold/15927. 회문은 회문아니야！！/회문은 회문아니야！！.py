s = input()
if len(s) in (0, 1):
    print(-1)
    exit()
if s != s[::-1]:
    print(len(s))
else:
    s = s[:-1]
    if s != s[::-1]:
        print(len(s))
    else:
        print(-1)
