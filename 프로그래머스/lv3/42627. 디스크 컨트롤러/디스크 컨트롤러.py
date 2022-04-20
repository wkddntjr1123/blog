from collections import deque
from heapq import heappop, heappush


def solution(jobs):
    answer = 0
    time = 0
    length = len(jobs)
    jobs = deque(sorted(jobs, key=lambda x: (x[0], x[1])))  # 시작시간 순 정렬, 시작 시간이 같다면 짧은 순 정렬
    heap = []  # 시작 가능한 녀석들 소요시간 기준으로 힙에 삽입
    while True:
        while jobs and jobs[0][0] <= time:  # 시작 가능한 모든 녀석들 heap에 넣는다
            heappush(heap, jobs.popleft()[::-1])
        if not heap:  # 시작 가능한게 없다면 가장 빠른 시작인 녀석 하나를 뺀다
            heappush(heap, jobs.popleft()[::-1])
            continue
        duration, start = heappop(heap)
        time = max(time, start) + duration
        answer += time - start
        if not jobs and not heap:
            break
    return answer // length