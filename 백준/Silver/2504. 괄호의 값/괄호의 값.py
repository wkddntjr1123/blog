from sys import stdin

input = stdin.readline

s = input().rstrip()


def cal_s(s):
    stack = []
    match = {")": "(", "]": "["}
    result = 0
    if s[0] in (")", "]"):
        return 0
    for i in range(len(s)):
        if s[i] in ("(", "["):
            stack.append(s[i])
        else:
            if not stack or stack.pop() != match[s[i]]:
                return 0
            elif s[i - 1] in (")", "]"):
                continue
            else:
                num_2, num_3 = 0, 0
                for char in stack:
                    if char == "(":
                        num_2 += 1
                    else:
                        num_3 += 1
                if s[i] == ")":
                    result += 2 * (2**num_2) * (3**num_3)
                else:
                    result += 3 * (2**num_2) * (3**num_3)
    return result if not stack else 0


print(cal_s(s))