
# 1. 필요 없는 걸 먼저 abc에서 제거
    # --> str.replace() 사용
        # 문자열 = 문자열.replace(i, "") - replace() 함수의 return값 잘 확인하자   
    # --> set으로 지우는 방법도 있다!!
        # 이건 다시 연습 필요
# 2. index 만큼 뒤로 넘기요
    # --> 그냥 넘기는건 별로 안 어렵지? 
    # --> z 뒤로 넘어가는 경우 : abc[    (abc.index(s) + index) % len(abc)    ]
    # ** 이걸 꼭 알아두자 넘어가는 경우 그 abc로 나눈 나머지가 뒤로 몇번을 넘어가야하는지도 결정하게 되니깐!

def solutionMine(s, skip, index):
    answer1 = []
    
    abc = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in skip:
        if i in abc:
            abc = abc.replace(i, '')
            
    for j in s:
        if abc.index(j)+index > abc.index('z'):
            answer1.append(abc[index -(len(abc) - abc.index(j))])
        else:
            answer1.append(abc[abc.index(j) + index])
        
    
    return "".join(answer1)


# 다른 사람 풀이 ... ㅅㅂ
def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz" # 알파벳
    
    # 1. 필요 없는 것 삭제
    for ch in skip:
        if ch in alpha:
            alpha = alpha.replace(ch, "")
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)] # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change
    
    return answer



from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result
        

