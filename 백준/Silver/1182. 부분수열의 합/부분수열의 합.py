from sys import stdin


input = stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0


def func(k, res):
    if k == n:
        if res == s:
            global answer
            answer += 1
        return
    func(k + 1, res)
    func(k + 1, res + arr[k])


func(0, 0)
print(answer if s != 0 else answer - 1)
