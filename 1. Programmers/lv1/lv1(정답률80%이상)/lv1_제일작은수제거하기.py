def solution(arr):
    
    arr.remove(min(arr))
    
    if len(arr) == 0:
        return [-1]
    else:
        return arr


def solution2(arr):
    arr.remove(min(arr))
    return arr if len(arr) != 0 else [-1]


# 이렇게 한 줄로 줄이는 방법도 있다 !!