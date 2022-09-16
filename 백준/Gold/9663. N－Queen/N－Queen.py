from sys import stdin


input = stdin.readline

n = int(input())

visitedCol = [False for _ in range(n)]
visitedSlash = [False for _ in range(2 * n)]
visitedBackSlash = [False for _ in range(2 * n)]

answer = 0

def func(i):
    if i == n:
        global answer
        answer += 1
        return
    for j in range(n):
        if visitedCol[j] or visitedSlash[i - j + n] or visitedBackSlash[i + j]:
            continue
        visitedCol[j] = True
        visitedSlash[i - j + n] = True
        visitedBackSlash[i + j] = True
        func(i + 1)
        visitedCol[j] = False
        visitedSlash[i - j + n] = False
        visitedBackSlash[i + j] = False


func(0)
print(answer)