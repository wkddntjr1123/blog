s = input()
p = input()


def get_pi(pattern):
    pi = [0 for _ in range(len(pattern))]  # 초기화는 pattern의 길이만큼 0
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:  # j를 다시 일치하는 문자까지 앞으로
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(s, pattern):
    pi = get_pi(pattern)  # pi 배열 생성
    result = []
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                result.append(i - len(pattern) + 2)
                return result
            else:
                j += 1
    return None


if kmp(s, p):
    print(1)
else:
    print(0)
