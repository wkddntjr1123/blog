from sys import stdin

input = stdin.readline

n = int(input())

visited_col = [False] * n
visited_slash = set()
visited_r_slash = set()
res = 0

def dfs(k):
    if k == n:
        global res
        res += 1
        return
    for col in range(n):
        if (
            not visited_col[col]
            and (col - k) not in visited_slash
            and (k + col) not in visited_r_slash
        ):
            visited_col[col] = True
            visited_slash.add(col - k)
            visited_r_slash.add(k + col)
            dfs(k + 1)
            visited_col[col] = False
            visited_slash.remove(col - k)
            visited_r_slash.remove(k + col)

dfs(0)
print(res)