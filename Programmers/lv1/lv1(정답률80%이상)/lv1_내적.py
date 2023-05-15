# solution1이 solution2보다 속도가 빠르다
# 아무래도 list를 쓰는게 그렇게 빠른 것 같지는 않다

def solution1(a, b):
    
    answer = 0
    
    for i in range(len(a)):
        answer += a[i] * b[i]
    
    return answer

def solution2(a,b):
    return sum([x*y for x, y in zip(a,b)])