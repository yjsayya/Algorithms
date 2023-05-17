'''
결국은 규칙을 찾는게 굉장히 중요했던 문제
그 공식을 잘 찾았다면 - 구현은 어렵지 않았다 
아이디어 : 둘래의 길이를 계산하는 것 
'''

def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            upDown = (yellow//i) + 2
            side = i * 2 

            if upDown * 2 + side == brown:
                return [upDown, i+2]