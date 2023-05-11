# 일단 풀긴 했는데 더 깔끔하게 풀 수 있을 듯
def solution(n):
    waterMelon = '수박' * (n//2)
    if n % 2 != 0:
        waterMelon += '수'

    return waterMelon

# str * int 이게 된다는 거 꼭 기억하도록 하자 