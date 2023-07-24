''''''
"""
    내가 처음 생각해낸 아이디어 
        1. 자릿수 x를 먼저 구한다
        2. x자릿수 n번째인지 구한다 (n을 손봐야한다)
        3. 해당 자릿수 li에서 li[n]을 구한다 
    --> 느낌이 이따구로 구하면 안될 것 같다 : 시간복잡도가 ㅎㅌㅊ이다 
    
     
"""

# 자릿수 x 구하기
def checkX(n):
    x = 1
    while n >= (3**(x+1)) // 2:
        x += 1
    return x

def solution(n):
     x = checkX(n)
     n -= (3**x-3) // 2


# 다른 사람 풀이 시부레
def solution2(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n%3)
            n //= 3
        else:
            answer += '4'
            n = n//3 -1

    return answer[::-1]


