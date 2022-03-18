from collections import Counter
from sys import stdin


input = stdin.readline

s = input().rstrip()

table = Counter(s)
front = ""
mid = ""
# 홀수 count가 2개 이상이면 실패
cnt = 0
for k in sorted(table.keys()):
    if table[k] % 2 == 1:
        cnt += 1
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()
        front += k * (table[k] // 2)
        mid = k
    else:
        front += k * (table[k] // 2)
end = front[::-1]
print(front + mid + end)