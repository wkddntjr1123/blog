from sys import stdin


input = lambda: stdin.readline().rstrip()


def valid(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return not bool(stack)


for _ in range(int(input())):
    s = input()
    print("YES" if valid(s) else "NO")