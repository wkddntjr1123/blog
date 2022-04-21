def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    while B :
        if A[-1] >= B[-1] :
            B.pop()
        else :
            A.pop()
            B.pop()
            answer += 1
    return answer