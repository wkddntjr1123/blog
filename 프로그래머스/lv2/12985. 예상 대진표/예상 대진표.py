import math
def solution(n,a,b):
    def half(x):
        return math.floor(x+0.5)
    def dfs(n,a,b,res) :    
        if n == 2 :
            return 1
        if a <= n//2 and b<=n//2 :
            return dfs(n//2,half(a),half(b),res+1)
        elif a>n//2 and b>n//2 :
            return dfs(n//2,half(a-n//2),half(b-n//2),res+1)
        else :
            cnt = 0
            while n != 1:
                n//=2
                cnt += 1
            return cnt
    return dfs(n,a,b,0)