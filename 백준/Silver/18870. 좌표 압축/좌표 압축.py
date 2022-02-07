from sys import stdin


input = stdin.readline
n = int(input())
origin_arr = list(map(int, input().split()))
sorted_set = sorted(set(origin_arr))
res_dict = dict()
for i in range(len(sorted_set)):
    res_dict[sorted_set[i]] = i
for num in origin_arr:
    print(res_dict[num], end=" ")