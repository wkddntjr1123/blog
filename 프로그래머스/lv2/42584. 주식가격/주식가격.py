def solution(prices):
    stack = []
    answer = [False for _ in range(len(prices))]
    for i in range(0, len(prices)):
        while stack and stack[-1][1] > prices[i]:
            item = stack.pop()
            answer[item[0]] = i - item[0]
        stack.append((i, prices[i]))
    while stack:
        item = stack.pop()
        answer[item[0]] = len(prices) - item[0] - 1
    return answer