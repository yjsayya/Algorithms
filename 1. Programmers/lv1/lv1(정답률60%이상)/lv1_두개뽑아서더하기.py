'''
2보다 1이 더 빠르다
    if i not in answer --> 이걸 연산하는 과정 ㄸ문인 것 같다
'''


from itertools import combinations as cb
def solution1(numbers):
    answer = []
    
    for i in cb(numbers, 2):
        answer.append(sum(i))
    
    answer = sorted(list(set(answer)))
    
    return answer



from itertools import combinations as cb
def solution2(numbers):
    answer = []

    for i in cb(numbers, 2):
        if i not in answer:
            answer.append(sum(i))
    
    return sorted(answer)