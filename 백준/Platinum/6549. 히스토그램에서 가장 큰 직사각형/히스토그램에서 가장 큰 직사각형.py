from sys import maxsize, stdin


input = lambda: stdin.readline().rstrip()
VAL, CNT = 0, 1
while True:
    arr = input()
    if arr == "0":
        break
    arr = list(map(int, arr.split()[1:]))
    stack = []  # 오름차순 유지
    answer = -maxsize
    for num in arr:
        if not stack or stack[-1][VAL] < num:  # case1 : 스택 비었거나, 더 큰 수 들어오는 경우
            stack.append((num, 1))
        elif stack[-1][VAL] == num:  # case2 : 같은 수 들어오는 경우
            stack.append((num, stack.pop()[CNT] + 1))
        else:  # case3 : 더 작은 수 들어오는 경우
            width = 0
            while stack and stack[-1][VAL] >= num:  # 현재 들어오는 수보다 작은 수가 나올 때 까지 pop하면서 넓이 계산
                h, cnt = stack.pop()
                width += cnt
                answer = max(answer, width * h)
            stack.append((num, width + 1))
    width = 0
    while stack:  # 최종적으로 stack이 남아있다면 오름차순으로 남아있는 상태이므로 넓이 계산
        h, cnt = stack.pop()
        width += cnt
        answer = max(answer, width * h)
    print(answer)