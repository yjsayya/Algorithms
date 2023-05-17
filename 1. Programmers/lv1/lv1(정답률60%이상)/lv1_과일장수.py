
'''
첫번째 풀이 - 풀이는 맞는 것 같은데, 시간초과가 떠버렸다
두번째 풀이 - slicing 하는데 시간이 많이 걸릴거니깐
        그냥 읽어오는게 나을 거라고 생각한다
'''

def solution1(k, m, score):
    
    price = 0
    score.sort()
    
    while len(score) >= m:
        box = score[-m:]
        price += min(box)*m
        score = score[:-m]
    
return price


# 상태 1~k점
# 한 상자의 가격 --> p*m
#     - 사과 m개
#     - 가장 낮은 점수 : p
# 가장 이득을 많이 보려면 
#     - m * p * 상자 개수


def solution2(k, m, score):
    
    price = 0
    score.sort(reverse=True)
    
    idx = m
    for i in range(len(score)//m):
        price += min(score[idx-m:idx]) * m
        idx += m
    
    return price
