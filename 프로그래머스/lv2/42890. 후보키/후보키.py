from itertools import combinations

def solution(relation):
    answer = 0
    rows, cols = len(relation), len(relation[0])
    result_set = set()
    for n in range(1, cols + 1):  # 1개부터 ~ cols개까지 : 작은 순으로 찾기
        for possible_cols in combinations(range(cols), n):  # n개 컬럼을 뽑아서 검사
            # 최소성 검사 : 작은 순으로 검사 해왔으므로 possible_cols가 result_set안에 특정 원소를 완전히 포함하면 fail
            valid = True
            for res in result_set:
                if set(res).issubset(set(possible_cols)):
                    valid = False
                    break
            if not valid:
                continue
            check_set = set()
            for row in range(rows):  # 모든 row의 조합을 check_set에 담음
                check_set.add(tuple(relation[row][col] for col in possible_cols))  # 한 row에서의 조합
            if len(check_set) == rows:  # 만족
                answer += 1
                result_set.add(possible_cols)
    return answer