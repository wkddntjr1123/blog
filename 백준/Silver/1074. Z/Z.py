n, r, c = map(int, input().split())


def process(n, r, c) -> None:
    if n == 0:
        return 0
    order_value = 0
    width = 2**n
    reduced = width // 2
    top = True if r < reduced else False
    left = True if c < reduced else False
    # 1사분면
    if left and top:
        return order_value + process(n - 1, r, c)
    # 2사분면
    if not left and top:
        return order_value + reduced**2 + process(n - 1, r, c - reduced)
    # 3사분면
    if left and not top:
        return order_value + (reduced**2) * 2 + process(n - 1, r - reduced, c)
    # 4사분면
    if not left and not top:
        return order_value + (reduced**2) * 3 + process(n - 1, r - reduced, c - reduced)

print(process(n, r, c))