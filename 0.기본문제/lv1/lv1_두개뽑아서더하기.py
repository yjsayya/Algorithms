import itertools as i

def solution(numbers):
    answer = []
    
    a = i.permutations(numbers,2)
    print(list(a))
    
    # for i in list(a):
    #     print(type(i))

    return answer


solution([2,1,3,4,1])