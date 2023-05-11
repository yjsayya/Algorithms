

# 내가 처음 푼 풀이인데 
    # --> 시간 초과 나버렸네 // 시간복잡도 : O(n^2)
def find_ys(num):
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
            cnt += 1
    
    return cnt


def solution(n):
    answer = 0
    
    for i in range(2,n+1):
        if find_ys(i) == 2:
            answer += 1
    
    return answer