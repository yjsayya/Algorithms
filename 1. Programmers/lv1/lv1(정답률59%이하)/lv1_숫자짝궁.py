
'''
이제 슬슬 시간복잡도를 고려해야하는 문제가 나오기 시작했다

    첫번째 풀이도 - 알고리즘은 문제 없지만 시간초과가 뜬다
'''

# 첫번째 풀이
    # 테스트 11 12 13 14 시간초과로 통과하지 못했다
def solution(X, Y):
    
    liy = list(Y)
    answer = []
    
    for i in X:
        if i in liy:
            answer.append(i)
            liy.remove(i)
    
    if len(answer) == 0:
        return "-1"
    elif len(answer) == answer.count('0'):
        return "0"
    else:
        return ''.join(sorted(answer, reverse=True))


# 두번째 풀이
    # 9부터 시작하면 정렬하는 것도 안 해줘도 된다!!
def solution(X, Y):
    
    answer = []
    num = '9876543210'
    
    for i in num:
        answer.extend([i] * min(X.count(i), Y.count(i)))
    
    if len(answer) == 0:
        return "-1"
    elif len(answer) == answer.count("0"):
        return "0"
    else:
        return ''.join(answer)