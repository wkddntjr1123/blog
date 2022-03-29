from collections import defaultdict


def is_valid(u):
    stack = []
    for char in u:
        if char == "(":
            stack.append(char)
        else:
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return len(stack) == 0


def split(w):
    cnt = defaultdict(int)
    for i in range(len(w)):
        cnt[w[i]] += 1
        if cnt["("] == cnt[")"]:
            break
    return w[: i + 1], w[i + 1 :]


def rev(w):
    res = ""
    for char in w:
        if char == "(":
            res += ")"
        else:
            res += "("
    return res


def recur(w):
    # 1 : 입력이 빈 문자면 "" 반환
    if not w:
        return ""
    # 2 : 균형잡힌 문자열 w를 (최소균형잡힌문자열u + v)로 분리. w가 이미 최소라면 v는 빈 문자열이 된다.
    u, v = split(w)
    # 3-1 : u가 올바른 문자열이라면 v에 대해서 다시 1단계부터 수행
    if is_valid(u):
        return u + recur(v)
    # 3-2 : u가 올바른 문자열이 아니라면 "(" + v에대한 1단계재귀 + ")" + u[1:-1]의 각 괄호룰 reverse
    else:
        return "(" + recur(v) + ")" + rev(u[1:-1])


def solution(p):
    return recur(p)