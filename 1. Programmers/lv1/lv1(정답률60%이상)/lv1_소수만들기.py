'''
소수 만들기 알고리즘은 적어둔것을 참조하자
'''

def isPrime(n):
    if n < 2: # 0과 1은 소수가 아님
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

from itertools import combinations as comb
def solution(nums):
    cnt = 0
    for i in comb(nums, 3):
        if isPrime(sum(i)):
            cnt += 1
            
    return cnt


# Chat Gpt가 풀어줌
from itertools import combinations
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution2(nums):
    count = 0
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            count += 1
    return count