# 아이디어
    # -- 기준은 yellow로 잡으면 된다 
    # solution(24,24)를 푼다고 했을 때 ; 
    # upDown * 2 + side가 Brown 개수와 같을 때; 를 찾으면 된다 
    


# 첫번째 풀이
    # --> 한번에 풀어버렸다!!
def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            upDown = (yellow//i) + 2
            side = i * 2 

            if upDown * 2 + side == brown:
                answer = [upDown, i+2]
                break
    
    return answer

print(solution(24,24))