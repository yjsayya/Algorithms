# 전반적으로 stack/queue문제는 시간복잡도를 고려하지 않고 푸는 문제가 많이 나오는 듯 하다


# 첫번째로 푼 풀이 
    # --> 이제 stack/queue문제는 어렵지 않게 풀 수 있을 것 같다 
def solution(prices):
    answer = [0] * len(prices)
    for idx, ele in enumerate(prices):
        
        check = False
        
        for k in range(idx+1, len(prices)):
            if ele > prices[k]:
                check = True
                answer[idx] = k - idx
                break
                
        if check == False:
            answer[idx] = len(prices) - idx - 1
            
    return answer

print(solution([1, 2, 3, 2, 3]))