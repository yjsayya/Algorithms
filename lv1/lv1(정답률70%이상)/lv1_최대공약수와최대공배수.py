def gcdlcm(a, b):
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer


def solution1(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]


# 이게 내가 푼 풀이 -- 유클리드 호제법을 이용해야 최소공배수 최대공약수를 빠르게 구할 수 있다 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(n, m):
    answer = []
    
    if n == m:
        return [n,m]
    elif n%m==0 or m%n==0:
        if n > m:
            return [m,n]
        else:
            return [n,m]
    else:
        return [gcd(n,m), lcm(n,m)]