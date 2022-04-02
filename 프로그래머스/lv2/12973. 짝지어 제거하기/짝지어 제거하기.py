def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if not stack:
            stack.append(s[i])
            continue
        if stack[-1] == s[i]:
            stack.pop()
            continue
        else:
            stack.append(s[i])
    return 0 if stack else 1