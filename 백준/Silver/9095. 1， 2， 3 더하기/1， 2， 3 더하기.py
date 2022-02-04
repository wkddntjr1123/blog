table = [False for _ in range(11)]

def calc_sum(n):
    table[1] = 1
    table[2] = 2
    table[3] = 4
    if n < 4:
        return
    for i in range(4, n + 1):
        table[i] = table[i - 1] + table[i - 2] + table[i - 3]

n = int(input())
targets = []
max_target = 0
for _ in range(n):
    target = int(input())
    targets.append(target)
    max_target = max(target, max_target)

calc_sum(max_target)
for target in targets:
    print(table[target])