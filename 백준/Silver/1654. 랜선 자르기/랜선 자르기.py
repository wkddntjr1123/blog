from sys import stdin

input = stdin.readline
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

# 최대 길이 라인
max_line_len = max(lines)


def need_more_line(mid):
    res = 0
    for line in lines:
        res += line // mid
    if res < n:  # 랜선 더 필요
        return True
    else:  # 랜선이 오히려 많거나 현재 딱 맞으면
        return False


def find_max_len(left, right):
    mid = (left + right) // 2
    # 최대길이 도달
    if left == mid:
        return mid
    if need_more_line(mid):
        return find_max_len(left, mid)
    else:
        return find_max_len(mid, right)
# 시작부터 최대길이로 정답이 나오는 경우 예외처리
print(max_line_len) if not need_more_line(max_line_len) else print(find_max_len(left=1, right=max_line_len))