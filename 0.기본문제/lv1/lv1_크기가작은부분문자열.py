
# 내가 처음 푼 것 
def solution(t, p):
    num = []
    cnt = 0
    try:
        for i in range(0,len(t) - len(p) + 1):
            num.append(int(t[i:i+len(p)]))
    except IndexError:
        pass
    
    for j in num:
        if j <= int(p):
            cnt += 1

    return cnt


# 프로그래머스 1번 답
def solution1(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer


# 일단 for문을 한번만 썼다는 점에서 훨씬 좋은 풀이
# *** indexing[0:3] --> 이건 인덱스 넘어가도 IndexError 안난다!!!!!
# 이게 되게 중요하니깐 꼭 알아두도록 하자 !!!


