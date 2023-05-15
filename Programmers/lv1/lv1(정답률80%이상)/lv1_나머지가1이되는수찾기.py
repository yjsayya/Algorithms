# 뭐 딱히 여기서 더 줄이는 방법이 있는지 모르겠네?!

def solution(n):

    answer = 0
    
    for i in range(1, n):       
        if n % i == 1:
            answer = i
            break
    
    return answer