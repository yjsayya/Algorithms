# 시간 복잡도를 어떻게 하면 더 줄일 수 있을까? 


def solution(n):
    
    li = list(str(n))
    li.sort(reverse = True)
    
    return int("".join(li))