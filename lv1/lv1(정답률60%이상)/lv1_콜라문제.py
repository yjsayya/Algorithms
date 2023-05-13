# 규칙 잘 찾아야하는 문제 
# --> 이제 이 정도 나오면 어렵지 않게 풀 수 있을 것 같은데 
# --> 수학 문제에 더 가깝지 않나? 

def solution(a,b,n):
    
    cnt = 0
    
    while n >= a:
        cnt += n//a*b
        n = n//a*b + n%a
    
    return cnt

