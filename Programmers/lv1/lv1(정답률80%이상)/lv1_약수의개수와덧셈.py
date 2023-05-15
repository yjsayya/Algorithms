'''
    * 아이디어 - 제곱수의 약수는 홀수개
'''

# 이게 시간복잡도 압도적으로 좋음 ㅅㅂ
def solution1(left, right):
    
    answer = 0

    for i in range(left,right+1):
        if int(i**0.5)==i**0.5: answer -= i
        else: answer += i

    return answer


# 이게 내가 푼 것 
def divi(n):
    cnt = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            if n // i != i:
                cnt += 1
        i += 1
    return cnt

def solution2(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if divi(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer