
# 이렇게 푸는 사람도 있다 
# '에라토스테네스의 체'를 이용하는 것이 현재 가장 시간복잡도가 빠른 알고리즘 인 듯
# 시간 복잡도 : O(nlog(log n))

'''
n 이하 소수의 개수
    - 시간 복잡도 : O(nlog(log n))
    - '에라토스테네스의 체'를 이용 (이게 가장 빠른 방법인 듯)
'''
def getNumberOfPrime(n):
    # n 이하의 모든 수가 있는 집합을 만들고
    numList = set(range(2,n+1))
    # 2부터 '에라토스테네스의 체'를 적용
    for i in range(2,n+1):
        if i in numList:
            num -= set(range(2*i, n+1, i))

    return len(num)

'''
n이 소수인지 아닌지 판별
    - 시간 복잡도 : O(√n)
'''
def isPrime(n):
    if n < 2: # 0과 1은 소수가 아님
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

