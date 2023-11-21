''''''
"""
    << 구현 문제 >>
    - 예외처리 얼마나 잘하는지 물어보는 문제인 듯 하다 
    - 이 정도는 문제 없이 풀 수 있을 것 같은데
    - 정리를 좀 잘 해두면 더 좋ㅇ르 것 같다 ㅇㅋ ㅋㅋㅋ
    
    정규식으로 푸는 방법
    이중 for문으로 푸는 방법
    
    (w.f) str.index() vs str.find() 잘 쵘하기
"""

# 이게 가장 깔끔한 풀이
def solution(skill, skill_trees):
    cnt = 0
    for ABC in skill_trees:
        temp = ABC
        # 1. 필요 없는 스킬은 replace()로 제거해버리기
        for abc in ABC:
            if abc not in skill:
                temp = temp.replace(abc, "")
        # 2. skill.find()가 0인 것만 카운트
        if skill.find(temp) == 0:
            cnt += 1

    return cnt



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