num = int(input())

count5 = num // 5
if count5 * 5 == num:
    print(count5)
else:
    while True:
        if (num - count5 * 5) % 3 == 0:
            print(count5 + ((num - count5 * 5) // 3))
            break
        if count5 <= 0:
            print(-1)
            break
        count5 -= 1