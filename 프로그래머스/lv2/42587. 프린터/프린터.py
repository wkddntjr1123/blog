from collections import deque


def solution(p, loc):
    answer = 0
    max_p = deque(sorted(p, reverse=True))
    p = deque(enumerate(p))  # (location,priors)

    cnt = 1
    while p:
        cur_loc, cur_prior = p.popleft()
        if cur_prior == max_p[0]:
            if cur_loc == loc:
                return cnt
            else:
                max_p.popleft()
                cnt += 1
        else:
            p.append((cur_loc, cur_prior))
    return answer