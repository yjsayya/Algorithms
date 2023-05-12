# 약수(divisors) 구하기

# 약수 리스트 반환
def get_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors

print(get_divisors(12))
print(get_divisors(36))