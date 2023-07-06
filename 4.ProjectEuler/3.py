# 600_851_475_143의 가장 큰 소인수 구하기

se = set()
num = 600_851_475_143
i = 2

while num >= i:
    if num % i == 0:
        se.add(i)
        while num % i == 0:
            num //= i
    i += 1

print(max(se))

'''
왜 잔디가 안 심어지지? 
'''