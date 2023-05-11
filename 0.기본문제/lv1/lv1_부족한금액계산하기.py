# 간단한 등차수열의 합 문제 
# 등차수열 공식 알면 쉽게 풀 수 있다 ㅇㅇ 

def solution(price, money, count):
    
    answer = price * (count+1) * count / 2 - money
    
    if answer < 0:
        return 0
    else:
        return price * (count+1) * count / 2 - money