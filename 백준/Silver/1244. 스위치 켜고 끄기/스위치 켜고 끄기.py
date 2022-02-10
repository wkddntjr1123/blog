from sys import stdin


input = stdin.readline

n = int(input())
switch = list(map(int, input().split()))
m = int(input())


def toggle_male(num, switch):
    for i in range(num, n, num + 1):
        switch[i] = int(not switch[i])


def toggle_female(num, switch):
    switch[num] = int(not switch[num])
    l, r = num - 1, num + 1
    while 0 <= l and r < n and switch[l] == switch[r]:
        switch[l] = int(not switch[l])
        switch[r] = int(not switch[r])
        l -= 1
        r += 1


for _ in range(m):
    sex, num = map(int, input().split())
    num -= 1
    if sex == 1:
        toggle_male(num, switch)
    else:
        toggle_female(num, switch)

for i in range(len(switch)):
    print(switch[i], end=" ")
    if (i + 1) % 20 == 0:
        print()