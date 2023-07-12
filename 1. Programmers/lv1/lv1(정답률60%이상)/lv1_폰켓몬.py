
def solution(nums):
    
    n = len(nums) / 2
    num = set(nums)
    
    if len(num) <= n:
        return len(num)
    else:
        return n
        
# set도 hash로 되어있긴 하지 ...


# 이 풀이 개 쩔었다 ...
def solution2(ls):
    return min(len(ls)/2, len(set(ls)))