def solution(name):
    answer = 0
    for char in name:
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)
    move = len(name) - 1
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        move = min((2 * i + len(name) - next), (2 * (len(name) - next) + i), move)
    return answer + move