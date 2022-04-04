def to_k(n, k):
    res = ""
    while n != 0:
        res = str(n % k) + res
        n //= k
    return res


def is_prime(num):
    if num in (0, 1):
        return False
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    nums = []
    for s in to_k(n, k).split("0"):
        if s:
            nums.append(int(s))
    for num in nums:
        if is_prime(num):
            answer += 1
    return answer