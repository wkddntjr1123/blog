from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
# pok_names

pok_dict = dict()
num_arr = [False for _ in range(n + 1)]
for i in range(n):
    name = input().rstrip("\n")
    num_arr[i + 1] = name
    pok_dict[name] = i + 1
question = [input().rstrip("\n") for _ in range(m)]

for q in question:
    if q.isalpha():
        print(pok_dict[q])
    else:
        print(num_arr[int(q)])