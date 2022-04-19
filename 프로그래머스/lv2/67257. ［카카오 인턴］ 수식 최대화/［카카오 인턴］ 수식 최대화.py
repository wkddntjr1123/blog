from collections import deque
from itertools import permutations
import re
from sys import maxsize


def solution(expression):
    max_val = -maxsize
    for prior in permutations("*+-", 3):
        q = deque(re.findall("[0-9]+|[*+-]", expression))
        for op in prior:
            stack = []
            while q:
                if q[0] == op:
                    stack.append(str(eval(stack.pop() + q.popleft() + q.popleft())))
                    continue
                stack.append(q.popleft())
            q = deque(stack)
        max_val = max(max_val, abs(int(q[0])))
    return max_val