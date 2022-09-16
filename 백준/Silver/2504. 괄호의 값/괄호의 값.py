def process(s: str) -> int:
    stack = []
    table = {")": "(", "]": "["}
    # 첫문자가 잘못된 경우 return 0
    if (not s) or (s[0] in table):
        return 0
    result = 0
    for i in range(len(s)):
        # 여는 괄호면 stack에 추가
        if s[i] in ("(", "["):
            stack.append(s[i])
        # 닫는 괄호면
        else:
            # "())))))))"같은 오른쪽 괄호가 더 많은 잘못된 케이스 입력 예외처리
            if not stack:
                return 0
            last = stack.pop()
            # 괄호 짝이 잘못된 경우 return 0 : 스택에서 꺼낸 아이템과 s[i]가 다르면 괄호에 문제가 있다는 의미
            if table[s[i]] != last:
                return 0
            # 괄호 짝이 맞는데 이전 문자가 아닌 경우 = (x), [x] 인 경우
            if s[i - 1] != table[s[i]]:
                continue
            # 괄호 짝이 맞고 이전 문자도 동일한 경우 = (), [] 인 경우
            else:
                # ()면 2, []면 3
                num = 2 if s[i] == ")" else 3
                # 스택에 있는 "("는 x2, "["는 x3
                result += num * (2 ** stack.count("(")) * (3 ** stack.count("["))
    # 최종적으로 스택에 값이 없어야 정상
    return result if not stack else 0

s = input()
print(process(s))