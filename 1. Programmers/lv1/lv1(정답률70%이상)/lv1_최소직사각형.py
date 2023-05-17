'''
    이중 배열일 때 ; python은
    for i, j in [[1,2], [1,3]]:
        이렇게 되면 i,j 둘다 꺼낼 수 있다 ... ㄷㄷ; 
        개쩐다 ....


    완전탐색이라고는 하지만 -- 완전 탐색으로 안 풀었음 
    결국 규칙이 있음 ㅋㅋ 
'''

# 이거 내가 푼 풀이
def solution(sizes):
    
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
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col


