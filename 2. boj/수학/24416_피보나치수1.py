
# n = int(input())

# 재귀함수를 이용한 피보나치수열 계산 
def fib(n):
    cnt += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(10))
print(cnt)
