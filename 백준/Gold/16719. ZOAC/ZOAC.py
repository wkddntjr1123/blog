from sys import maxsize, stdin


input = stdin.readline

s = input().rstrip()
index_table = {v: i for i, v in enumerate(s)}
visited = [False for _ in range(len(s))]


def right_index(index):
    min_char, min_idx = "z", -1
    for i in range(index + 1, len(s)):
        if not visited[i] and s[i] < min_char:
            min_idx = i
            min_char = s[i]
    return min_idx


res = ["" for _ in range(len(s))]


def func(index):
    while True:
        r_min_idx = right_index(index)  # 우측 중 가장 빠른 사전 인덱스
        if r_min_idx == -1:
            break
        res[r_min_idx] = s[r_min_idx]
        visited[r_min_idx] = True
        print("".join(res))
        func(r_min_idx)


func(-1)