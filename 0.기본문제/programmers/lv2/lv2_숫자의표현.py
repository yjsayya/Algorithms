# 첫번째 푼 풀이
    #--> 효율성 테스트는 하나도 통과하지 못했다 
    # 무차별 대입으로 풀었다
def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        sum = 0
        for j in range(i,n+1):
            sum += j
            if sum == n:
                answer += 1
                break
    
    return answer



# 시간 복잡도를 고려해서 두번째로 푼 풀다
def solution1(n):
    answer = 1

    for i in range(1,n+1):
        sum = 0
        for j in range(i,n//2+1):
            sum += j
            if sum == n:
                break
            if sum > n:
                break


# 다른 사람 풀이 --> 공식을 이용해서 풀이
def solution2(n):
    answer = 0
    a = []
    for i in range(1, n+1 ,2):
        if n % i == 0:
            a.append(i)
    
    return len(a)

print(solution2(15))

# n-1 + n + n+1 = 3n
# n-2 + n-1 + n + n+1 + n+2 = 5n
# 결국  n의 약수 중 홀수가 몇개 있냐는 문제