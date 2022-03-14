test_case = int(input())
m = 10000
isPrime = [False, False] + [True] * (m - 1)
for i in range(2, int(m**0.5) + 1):
    if isPrime[i]:
        for j in range(2 * i, m + 1, i):
            isPrime[j] = False


def getGoldPartition(num):
    global isPrime
    center = num // 2
    # n/2가 소수인 경우
    if isPrime[center]:
        print(center, center)
        return
    # n/2가 소수가 아닌 경우
    else:
        for i in range(center - 1, 1, -1):  # 왼쪽으로 1씩 이동
            if isPrime[i]:  # 왼쪽에서 소수 발견하면
                for j in range(center + 1, n + 1):  # 오른쪽으로 한칸씩 이동
                    if isPrime[j]:  # 오른쪽에서 소수 발견하면
                        sum = i + j
                        if sum == n:  # 골드바흐 파티션인 경우
                            print(i, j)
                            return
                        elif sum > n:
                            break


for _ in range(test_case):
    n = int(input())
    getGoldPartition(n)