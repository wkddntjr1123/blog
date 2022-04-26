def solution(n, times):
    answer = 0
    left = 1
    right = n//len(times)*max(times)
    def bi(times,left,right) :
        if left >= right :
            return left
        mid_time = (left+right)//2
        res = 0
        for time in times :
            res += mid_time // time
        if res < n :
            return bi(times,mid_time+1,right)
        else :
            return bi(times,left,mid_time)
    
    return bi(times,left,right)