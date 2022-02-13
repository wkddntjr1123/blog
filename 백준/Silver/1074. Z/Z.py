from sys import stdin

input = stdin.readline

n, r, c = map(int, input().split())

result = 0

def Z(k, x, y):
    global r, c, result
    if k == -1:
        print(result)
        exit()
    if not (x <= r < (x + 2**k)) or not (y <= c < (y + 2**k)):
        result += (2**k) ** 2
        return
    center = (2**k) // 2
    Z(k - 1, x, y)
    Z(k - 1, x, y + center)
    Z(k - 1, x + center, y)
    Z(k - 1, x + center, y + center)

Z(n, 0, 0)