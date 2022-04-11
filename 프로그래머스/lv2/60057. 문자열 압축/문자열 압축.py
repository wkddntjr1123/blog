def solution(s):
    answer = len(s)
    for size in range(1, len(s) // 2 + 1):
        i, cnt, length = 0, 0, len(s)
        for i in range(0, len(s), size):
            if s[i : i + size] == s[i + size : i + size + size]:
                cnt += 1
            elif cnt > 0:
                length = length - (cnt * size) + len(str(cnt + 1))
                cnt = 0
        answer = min(answer, length)
    return answer