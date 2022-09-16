def process(s: str) -> int:
    stick = 0
    result = 0
    for i in range(len(s)):
        # 막대+1
        if s[i] == "(":
            stick += 1
        else:
            stick -= 1
            # 레이저
            if s[i - 1] == "(":
                result += stick
            # 막대-1
            elif s[i - 1] == ")":
                result += 1
    return result
    
s = input()
print(process(s))