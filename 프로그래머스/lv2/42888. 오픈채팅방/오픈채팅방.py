def solution(record):
    answer = []
    namespace = dict()
    for log in record:
        log = log.split()
        if log[0] == "Enter" or log[0] == "Change":
            namespace[log[1]] = log[2]
    for log in record:
        log = log.split()
        if log[0] == "Enter":
            answer.append(f"{namespace[log[1]]}님이 들어왔습니다.")
        elif log[0] == "Leave":
            answer.append(f"{namespace[log[1]]}님이 나갔습니다.")
    return answer