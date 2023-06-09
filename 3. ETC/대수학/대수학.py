
'''

1. 소수(prime_number)
2. 약수, 배수, 최소공약수, 최소공배수
3. 피보나치 수열
4. 경우의 수 구하기 - 순열, 조합
5. 

'''


# =[ 소수(Prime Number) ]======================================================
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
            numList -= set(range(2*i, n+1, i))

    return len(numList)

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

# =[ 약수(divisors) ]======================================================
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



# =[ 최대공약수, 최소공배수 ]======================================================
'''
    유클리드 호제법을 이용해서 접근하는 것이 가장 빠른 방법이라고 한다.
    둘다 - 시간복잡도 : O(logN)

    << 유클리드 호제법 >>
    - 입력된 두 수를 a와 b라고 합니다.
    - a % b를 계산합니다. 이 값이 0이라면, b가 a와 b의 최대공약수입니다.
    - a % b의 값이 0이 아니라면, a를 b로, b를 a % b로 대체합니다.
    - 2번으로 돌아가서 다시 계산합니다.

    --> 재귀함수로 구하는 것이 일반적이다.
'''


# 최대공약수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수
def lcm(a, b):
    return a * b // gcd(a,b)



# =[ 피보나치수열 ]======================================================



# =[ 순열,조합 ]======================================================
'''
<<python으로 순열과 조합 구현하기>>

# python 라이브러리 이용하기

from itertools import combinations, permutations

1. 순열(Permutations, nPr)
    permutation(iteral, r)
    // param1 - iteral
    // param2 - 고를 개수(r)
    // return - tuple()

    nums = [1,2,3,4]
    list(permutations(nums,2))

2. 조합(Combinations, nCr)
    combination(iteral, r)
    // param1 - iteral
    // param2 - 고를 개수(r)
    // return - tuple()

    ** list()함수와 같이 쓰면 된다

    tuple()로 반환한다
    ex)
        num = [1,2,3,4]
        cases = list(combinations(num, 4)
        print(cases)    # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# 순열(nPr), 조합(nCr)
1. 재귀함수를 이용하여 순열 구현하기
    * idea -
list = [1,2,3,4,5]
used = [0] * len(list)

def per(arr,n):
    if n == len(list):
        print(arr)
        return
    for i in range(len(list)):
        if not used[i]:
            used[i] = 1
            arr.append(input_list[i])
            perm(arr, n+1)
            arr.pop()
            used[i] = 0
'''