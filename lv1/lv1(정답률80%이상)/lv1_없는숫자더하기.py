
# 

def solution(numbers):
    num_list = [1,2,3,4,5,6,7,8,9,0]
    
    for i in numbers:
        if i in num_list:
            num_list.remove(i)
    
    return sum(num_list)


# 이거지 
def solution1(numbers):
    
    return 45 - sum(numbers)