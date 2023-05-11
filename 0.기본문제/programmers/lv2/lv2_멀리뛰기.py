# math 라이브러리 기억해두자
import math
n,r = 3,1
nCr = math.comb(n,r)
nPr = math.perm(n,r)


# 첫번째 풀이 --> 내가 직접 규칙 찾아서 조합으로 풀어냈다
import math

def solution(n):
    answer = 0

    for i in range(n // 2 + 1):
        answer += math.comb(n - i, i)

    return answer % 1234567

# 다른 사람 풀이 --> 피보나치 수열로 풀리네 시부레
def jumpCase(num):
    a, b = 1, 2
    for i in range(2,num):
        a, b = b, a+b
    return b

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(4))