def solution(n):
    
    waterMelon = '수박' * (n//2)
    
    if n % 2 != 0:
        waterMelon += '수'

    return waterMelon


def solution1(n):
    waterMelon = '수박' * (n//2)
    return waterMelon if n % 2 == 0 else waterMelon + '수'

# 다른 사람 풀이인데 좋은 것 같아서 가져왔다 
def water_melon(n):
    str = "수박"*(n//2+1)
    return str[:n]