'''
 뭐 별로 어렵지 않았지? 넘어가자 
'''


def solution(t,p):
    
    n, m = len(p), len(t)
    cnt = 0
    
    for i in range(n-1, m):
        if int(t[i-n+1:i+1]) <= int(p):
            cnt += 1

    return cnt