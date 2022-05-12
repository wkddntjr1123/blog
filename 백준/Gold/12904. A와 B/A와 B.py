from sys import stdin


input = stdin.readline

s = input().rstrip()
t = list(input().rstrip())


def dfs(t, s):
    if len(t) == len(s):
        return True if "".join(t) == s else False
    if t[-1] == "A" and t[-1] == "B":
        return dfs(t[:-1], s) or dfs(t[:-1][::-1], s)
    elif t[-1] == "A":
        return dfs(t[:-1], s)
    elif t[-1] == "B":
        return dfs(t[:-1][::-1], s)
    else:
        return False


print(int(dfs(t, s)))
