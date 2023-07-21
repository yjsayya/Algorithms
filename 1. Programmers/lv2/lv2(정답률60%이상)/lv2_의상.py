''' '''
"""
    - 전형적인 Hash 문제
    아이디어 - 모든 의상의 개수를 곱한후 -1하기
    
    dic에 대한 공부 최대한 많이 하자
"""

# 아주 어렵지 않게 잘 풀었따
def solution(clothes):
    clothes_dic = dict()
    for i in clothes:
        if i[1] in clothes_dic:
            clothes_dic[i[1]].append(i[0])
        else:
            clothes_dic[i[1]] = [i[0]]

    answer = 1
    for clothes in clothes_dic.keys():
        answer *= len(clothes_dic[clothes]) + 1

    return answer - 1