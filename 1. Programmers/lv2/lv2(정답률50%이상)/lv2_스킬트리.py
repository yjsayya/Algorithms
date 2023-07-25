''''''
"""
    << 구현 문제 >>
    - 예외처리 얼마나 잘하는지 물어보는 문제인 듯 하다 
    - 이 정도는 문제 없이 풀 수 있을 것 같은데
    - 정리를 좀 잘 해두면 더 좋ㅇ르 것 같다 ㅇㅋ ㅋㅋㅋ
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


# 다시 한번 정리를 해보았다
def solution2(skill, skill_trees):
    cnt = 0
    for skills in skill_trees:
        li = list(skill)
        check = True

        for i in skills:
            if i == li[0]:
                li.pop(0)
                if not li:
                    break
            elif i != li[0] and i in li:
                check = False
                break

        if check: cnt += 1

    return cnt

"""
    어떠한 예외가 있는가? 
    - 일단 [skill_list]가 없으면 : 나가고 --> True
    - list에 없는 거는 그냥 pass 
    - 만약 li[0]이면 pop()하고 진행
    - li[0]이 아닌데 list안에 있으면 --> False
    
"""

# 다른 사람 풀이 - 이게 훨씬 깔끔한 정리라고 할 수 있다 ㅎㅎ
def solution3(skill, skill_trees):
    cnt = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            cnt += 1

    return cnt

# 아빠와 딸에서 나왔습니다. 이게 맞는지는 잘 모르계씾만 ㅇ쩄든 아주 이런 토프레 아주 훌륭하고 저는 정말 만족스러워서
# 코믹을 맡으면 되는거잔하용

data = [2,4,5,1,3]
test = 0

for i in data:
    if i > 10:
        test = 1
    break

if not test:
    print('10보다 큰 수 없음')

for i in data:
    if i > 10:
        break
else:
    print('10보다 큰 수 없음')

# 이거 두개가 같은 코드라고 한다 ㅇㅋ