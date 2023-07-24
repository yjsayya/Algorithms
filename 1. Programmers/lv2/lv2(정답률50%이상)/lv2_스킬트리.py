''''''
"""
    예외처리 얼마나 잘하는지 물어보는 문제인 듯 하다 
    --> 이런 건 빠르게 잘 풀면 될 듯?! 
    이 정도는 문제 없이 풀 수 있을 것 같은데
    정리를 좀 잘 해두면 더 좋ㅇ르 것 같다 ㅇㅋ ㅋㅋㅋ
    
    
"""
# 큰 무리 없이 잘 풀었다
def solution(skill, skill_trees):

    cnt = 0

    for i in skill_trees:
        li = list(skill)
        check = True
        for j in i:
            if not li:
                break

            if j == li[0]:
                li.pop(0)
            elif j != li[0] and j in li:
                check = False
                break
        if check:
            cnt += 1

    return cnt