'''
    피보나치수열 알아두자
'''

def solution(n):
    
    a0, a1 = 0, 1
    an = 0
    
    for _ in range(n-1):
        an = a0+a1
        a0 = a1
        a1 = an
    
    return an % 1234567



# python은 '''a, b = b, a+b''' 이따구로 해도 괜찮다는거 꼭 알아두자
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a