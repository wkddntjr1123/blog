from functools import cmp_to_key
import re
from sys import stdin

input = stdin.readline

n = int(input())


def comp(s1, s2):
    num_mask = re.compile("[0-9]+|[a-zA-Z]")
    token1 = [item.group() for item in num_mask.finditer(s1)]
    token2 = [item.group() for item in num_mask.finditer(s2)]
    diff_idx = -1
    for i in range(min(len(token1), len(token2))):
        if token1[i] != token2[i]:
            diff_idx = i
            break
    # case0 : 둘이 동일하거나 포함관계인 경우 => 짧은 문자열 우선
    if diff_idx == -1:
        return -1 if len(token1) < len(token2) else 1
    # case1 : 둘다 알파벳
    if token1[diff_idx].isalpha() and token2[diff_idx].isalpha():
        if token1[diff_idx].lower() == token2[diff_idx].lower():  # 같은 알파벳 => 대문자가 우선
            return -1 if token1[diff_idx].isupper() else 1
        else:  # 다른 알파벳 => 통상적 순서
            return -1 if token1[diff_idx].lower() < token2[diff_idx].lower() else 1
    # case2 : 둘 다 숫자
    elif token1[diff_idx].isnumeric() and token2[diff_idx].isnumeric():
        num1, num2 = int(token1[diff_idx]), int(token2[diff_idx])
        if num1 < num2:  # 십진수로 작은 숫자가 우선
            return -1
        elif num1 > num2:
            return 1
        else:  # 같은 숫자면 0개수가 적은 게 우선
            return -1 if len(token1[diff_idx]) <= len(token2[diff_idx]) else 1
    # case3 : 하나만 숫자 => 숫자가 우선
    else:
        return -1 if token1[diff_idx].isnumeric() else 1


arr = []
for _ in range(n):
    arr.append(input().rstrip())

arr.sort(key=cmp_to_key(comp))
print(*arr, sep="\n")