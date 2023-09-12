# 10001번째 소수 구하기

# 소수 판별 메서드
def isPrime(n):
    if n < 2: # 0과 1은 소수가 아님
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


li = [0,0] # pNum, cnt
num = 1
while li[1] < 10001:
    if isPrime(num):
        li[0] = num
        li[1] += 1
        num += 1
    else:
        num += 1

print(li[0])