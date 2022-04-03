def valid(s):
    table = {"]": "[", "}": "{", ")": "("}
    stack = []
    for char in s:
        if char in table:
            if not stack or table[char] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


def solution(s):
    answer = 0
    for i in range(len(s)):
        if valid(s[i:] + s[:i]):
            answer += 1
    return answer