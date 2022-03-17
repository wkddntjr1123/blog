m = 123456
isPrime = [False, False] + [True] * (m * 2 - 1)

for i in range(2, int((m * 2) ** 0.5) + 1):
    if isPrime[i]:
        for j in range(2 * i, m * 2 + 1, i):
            isPrime[j] = False

while True:
    num = int(input())
    if num == 0:
        break
    small = num
    num *= 2
    count = 0
    for i in range(small + 1, num + 1):
        if isPrime[i]:
            count += 1
    print(count)