# 규칙을 찾아내면 어렵지 않게 풀 수 있는 문제 
# 이런 문제는 그래도 - 소마에서도 1번 문제 이런 느낌이었는데
# 규칙을 찾아내는 것이 핵심!!


def solution(a, b, n):
    answer = 0
    
    while n >= a:
        answer += (n//a)*b
        n = (n//a)*b  + n%a
        
    return answer



solution = lambda a, b, n: max(n - b, 0) // (a - b) * b
# 나중에 한번 다시 보자 
# 뭔지는 모르겠지만 ㅋㅋ