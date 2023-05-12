'''
    arr이 무한에 가까워질수록 
    solution2 시간복잡도가 좀 더 커질 수 있다고 한다 
    리스트 내 for문 작동원리 다시 한번 확인해볼 필요가 있다 
'''

def solution1(arr, divisor):

    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        
    return sorted(answer) if len(answer) != 0 else [-1]


    # return sorted([n for n in arr if n%divisor == 0]) or [-1]
    # 이렇게 한 줄로도 처리가 가능 

def solution2(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]


