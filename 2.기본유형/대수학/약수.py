'''
* 약수(divisors) 구하기
    시간 복잡도 : O(√n)
    아이디어 : 반복문을 통해 1부터 n의 제곱근까지 순회하며, 
        n을 i로 나누어 떨어지는 경우 divisors 리스트에 추가하면서 
        n // i 값도 divisors 리스트에 추가합니다. 
        (n // i 값이 i와 같은 경우는 i가 제곱근이기 때문입니다.) 
'''

# 약수 리스트 반환
def getDivisors(n):
    divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if n // i != i:
                divs.append(n // i)
        i += 1
    divs.sort()
    return divs

# 약수 총합 반환
def getSumOfDivisors(n):
    sum = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            sum += i
            if n // i != i:
                sum += n //i
        i += 1
    return sum 

# 약수 개수 반환
def getNumOfDivisors(n):
    cnt = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            if n // i != i:
                cnt += 1
        i += 1
    return cnt

print(getDivisors(12))
print(getSumOfDivisors(12))
print(getNumOfDivisors(12))