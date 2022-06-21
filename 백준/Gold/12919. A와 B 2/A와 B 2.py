from sys import stdin


input = stdin.readline

s = input().rstrip()
t = list(input().rstrip())


# 거꾸로 가야함. t에서 A를 제거하거나 t를 뒤집은 거에서 B를 제거하거나
# 이렇게 해가면서 s와 일치되면 True


def dfs(t, s):
    if len(t) == len(s):
        return True if "".join(t) == s else False
    if t[-1] == "A" and t[0] == "B":
        return dfs(t[:-1], s) or dfs(t[::-1][:-1], s)
    elif t[-1] == "A":
        return dfs(t[:-1], s)
    elif t[0] == "B":
        return dfs(t[::-1][:-1], s)
    else:
        return False


print(int(dfs(t, s)))
