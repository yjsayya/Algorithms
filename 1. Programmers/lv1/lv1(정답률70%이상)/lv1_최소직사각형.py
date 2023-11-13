""""""
"""
    1. 일단 배열 내 최대값 구하기 
    2. 배열 중 작은 수만 따로 모아두고 이 중 가장 큰 수 구하기 
    3. (1) * (2)가 정답
"""

# 다시 풀었는데 규칙을 찾았다
def solution3(sizes):
    # 1. 배열 내 최댓값 구하기
    max1 = max([max(a,b) for a,b in sizes])
    # 2. 가로 세로 중 작은 수만 따로 모은 것 중 최댓값 구하기
    max2 = max([min(i,j) for i,j in sizes])
    # (1) * (2)가 정답
    return max1 * max2

# 이제 이런 리스트 컴프리헨션도 익숙해졌다
def solution4(sizes):
    return max([max(a,b) for a,b in sizes]) * max([min(i,j) for i,j in sizes])

def solution5(sizes):
    li1,li2 = [], []
    for i, j in sizes:
        li1.append(max(i, j))
        li2.append(min(i, j))
    return max(li1) * max(li2)

# 이거 내가 푼 풀이
def solution1(sizes):
    
    garo = sorted(sizes, key=lambda x : x[0], reverse=True)
    sero = sorted(sizes, key=lambda x : x[1], reverse=True)
    
    g = garo[0][0] # 가로 최대
    s = sero[0][1] # 세로 최대
    
    li = []
    
    if g <= s:
        for i in garo: #0이 가로 1이 세로
            if i[0] >= i[1]:
                li.append(i[1])
            else:
                li.append(i[0])
        
        return s * max(li)
    
    elif g > s:
        for j in sero:
            if j[0] <= j[1]:
                li.append(j[0])
            else:
                li.append(j[1])
    
        return g * max(li) 



# python은 이게 되네 ㄹㅇ 개 쩌는 언어야 ...
def solution2(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col


