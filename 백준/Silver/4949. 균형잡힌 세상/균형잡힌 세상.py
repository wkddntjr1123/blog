from sys import stdin

input = stdin.readline


def validation(s):
    stack = []
    table = {"]": "[", ")": "("}
    for char in s:
        if char in ["[", "("]:
            stack.append(char)
        elif char in table:
            if not stack:
                return False
            if stack[-1] != table[char]:
                return False
            stack.pop()
    return not stack


while True:
    s = input().rstrip()
    if s == ".":
        break
    print("yes" if validation(s) else "no")
