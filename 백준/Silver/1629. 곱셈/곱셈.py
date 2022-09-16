a, b, c = map(int, input().split())

# a의 b승
def ab_mod_c(a, b, c):
    if b == 1:
        return a % c
    value = ab_mod_c(a, b // 2, c)
    # b가 짝수
    if b % 2 == 0:
        return (value**2) % c
    # b가 홀수
    else:
        return (value**2 * a) % c

print(ab_mod_c(a, b, c))