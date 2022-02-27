times = 0
order = []


def move(n, start, to):
    global times
    times += 1
    order.append(f"{start} {to}")


def hanoi(n, start, to, via):
    if n == 1:
        move(n, start, to)
    else:
        hanoi(n - 1, start, via, to)
        move(n, start, to)
        hanoi(n - 1, via, to, start)


n = int(input())
hanoi(n, 1, 3, 2)
print(times)
print(*order, sep="\n")