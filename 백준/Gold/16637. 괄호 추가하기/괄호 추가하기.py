import re
from sys import maxsize, stdin

input = stdin.readline

n = int(input())
s = input().rstrip()
answer = -maxsize


def dfs(s):
    if len(re.findall(r"[0-9]+", s)) <= 2:
        avail = eval(s)
        global answer
        answer = max(answer, avail)
        return
    num_idx = []
    for item in re.finditer(r"[0-9]+", s):
        num_idx.append(item.span())
    st_a, end_a = num_idx[0]
    st_b, end_b = num_idx[1]
    st_c, end_c = num_idx[2]
    val = eval(s[:end_b])
    dfs(str(val) + s[end_b:])
    val = eval(s[st_b:end_c])
    val = eval(s[:st_b] + str(val))
    dfs(str(val) + s[end_c:])


dfs(s)
print(answer)