''''''
"""
    dic을 이용해서 잘 풀어냈다 굿굿 
    
"""

def solution(input_string):
    abc = []

    for i in input_string:
        if not abc:
            abc.append(i)
        else:
            if abc[-1].find(i) == 0:
                abc[-1] += i
            else:
                abc.append(i)
    # {알파뱃개수, 덩어리 갯수}
    dic = dict()
    for i in abc:
        if i[0] in dic:
            dic[i[0]][0] += len(i)
            dic[i[0]][1] += 1
        else:
            dic[i[0]] = [len(i), 1]
    ans = []
    for i in dic:
        if dic[i][0] >= 2 and dic[i][1] >= 2:
            ans.append(i)

    return "".join(sorted(ans)) if ans else "N"



# 두번째로 푼 풀이
#   이것도 잘 풀어냈다 ㅋㅋㅋ ㅇㅋ
def solution2(input_string):

    # 1. dic 만들기
    dic = dict()
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for i in abc:
        dic[i] = []
    # 2. 알파벳 박아넣기
    # 첫번째꺼 넣어주기
    dic[input_string[0]].append(input_string[0])
    # 두번째부터 진행
    for j in range(1,len(input_string)):
        leftLttr = input_string[j-1]
        lttr = input_string[j]
        if dic[lttr] and leftLttr == lttr:
            dic[lttr][-1] += lttr
        else:
            dic[lttr].append(lttr)
    # 3. 정답 구하기
    ans = ''
    for k in dic:
        if len(dic[k]) >= 2:
            ans += k

    return "N" if ans=='' else ans