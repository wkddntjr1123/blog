from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)

input = stdin.readline

DAY, VALUE = 0, 1
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]


def isAble(curIdx):
    return curIdx + arr[curIdx][DAY] <= n


def dfs(arr, curIdx, total):
    if curIdx >= n:
        global answer
        answer = max(answer, total)
        return
    if isAble(curIdx):
        dfs(arr, curIdx + arr[curIdx][DAY], total + arr[curIdx][VALUE])
    dfs(arr, curIdx + 1, total)


answer = 0
for i in range(n):
    dfs(arr, i, 0)
print(answer)
