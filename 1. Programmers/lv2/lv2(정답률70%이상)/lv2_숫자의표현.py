'''
    등차수열의 공식을 통해서 구하는 방법도 있다
    아이디어 : 자기보다 작은 홀수로 나누어 떨어지는 값의 갯수가 이문제 답의 갯수와 같다
'''

def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        num = 0
        for j in range(i, n+1):
            num += j
            if num == n:
                answer += 1
                break
            if num>n:
                break
    return answer



# 등차수열 공식을 통해서 푼 문제
def expressions(num):
    return len([i for i in range(1,num+1,2) if num % i is 0])

def hi(num):
    li = []
    for i in range(1, num+1, 2):
        if num % i is 0:
            li.append(i)

    return len(li)



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