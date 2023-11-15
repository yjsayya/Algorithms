""""""
"""
첫번째 풀이 - 풀이는 맞는 것 같은데, 시간초과가 떠버렸다
두번째 풀이 - slicing 하는데 시간이 많이 걸릴거니깐
        그냥 읽어오는게 나을 거라고 생각한다

** slicing은 시간복잡도에서 손해를 많이 본다는 것!!
--> 이걸 꼭 알아두자
"""
def solution1(k, m, score):
    
    price = 0
    score.sort()
    
    while len(score) >= m:
        box = score[-m:]
        price += min(box)*m
        score = score[:-m]
    
    return price


def solution2(k, m, score):
    
    price = 0
    score.sort(reverse=True)
    
    idx = m
    for i in range(len(score)//m):
        price += min(score[idx-m:idx]) * m
        idx += m
    
    return price


# 인덱스로 푸는게 젤 좋은 듯
def solution4(k,m,score):
    score.sort()
    ans = 0
    for idx in range(len(score)-m,-1,-m):
        ans += score[idx] * m

    return ans