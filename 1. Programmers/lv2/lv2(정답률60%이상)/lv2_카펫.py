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

# 두번째 푼 풀이
def solution2(brown, yellow):
    if yellow == 1:
        return [3,3]

    for i in range(1, yellow // 2 + 1):
        if yellow % i == 0:
            y_garo = max(i, yellow / i)
            y_sero = min(i, yellow / i)

            if (y_garo + 2) * 2 + y_sero * 2 == brown:
                return [y_garo + 2, y_sero + 2]