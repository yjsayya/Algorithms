

def solution(absolutes, signs):
    answer = 0
    
    for i,j in zip(absolutes, signs):
        if j: answer += i
        else: answer -= i
    
    return answer


print(solution([4,7,12],[true,false,true]))