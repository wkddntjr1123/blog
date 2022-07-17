from sys import stdin


def to_postfix(arr):
    i = 0
    while i < len(arr):
        if arr[i] in ("*", "/"):
            res = arr[i - 1] + arr[i + 1] + arr[i]
            for _ in range(2):
                arr.pop(i - 1)
            arr[i - 1] = res
            i -= 1
        i += 1
    i = 0
    while i < len(arr):
        if arr[i] in ("+", "-"):
            res = arr[i - 1] + arr[i + 1] + arr[i]
            for _ in range(2):
                arr.pop(i - 1)
            arr[i - 1] = res
            i -= 1
        i += 1
    return arr[0]


input = lambda: stdin.readline().rstrip()

infix = input()

# 1. 괄호 먼저 모두 처리
stack = [infix[0]]
for i in range(1, len(infix)):
    if infix[i] != ")":
        stack.append(infix[i])
    else:  # 닫는 괄호면
        sub = []
        char = stack.pop()
        while char != "(":
            sub.append(char)
            char = stack.pop()
        sub.reverse()
        stack.append(to_postfix(sub))
# 2. 괄호 없는 최종 문자열 처리
print(to_postfix(stack))