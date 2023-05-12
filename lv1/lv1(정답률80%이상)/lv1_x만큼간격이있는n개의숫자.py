
# range()의 3번째 파라미터에는 0이 들어가면 안된다!!

def solution(x, n):
    
    if x > 0:
        return [i for i in range(x,n*x+1,x)]
    elif x < 0:
        return [i for i in range(x,n*x-1,x)]
    else:
        return [0] * n


def solution1(x,n):
    return [i * x + x for i in range(n)]

def solution2(x,n):
    return [i for i in range(x, x*(n+1), x)]

# 이런 방법도 있구나 ...