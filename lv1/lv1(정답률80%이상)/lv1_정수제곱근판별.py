# int(2.1) --> 2가 나오는 형변환을 이용하는 문제

def solution(n):
    
    if int(n ** 0.5) ** 2 == n:
        return (int(n ** 0.5)+1)**2
    else:
        return -제