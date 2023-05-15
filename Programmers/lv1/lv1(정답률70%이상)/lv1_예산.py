# 이건 문제가 좀 이상한거 같은데? - 테스트 케이스가 좀 잘못된 듯 하다..?!

def solution(d, budget):
    
    d.sort()
    answer = 0
    
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
    
    return answer


#[2,2,2,2,2] budget = 9인 것처럼 아예 해결을 할 수 없는 케이스는 없는건가? 