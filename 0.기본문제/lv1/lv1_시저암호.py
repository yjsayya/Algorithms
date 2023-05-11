# lv2_둘만의암호 문제와 같은 유형 --> 그 덕에 쉽게 풀어낼 수 있어쑈다 
    # --> abc[(abc.index(i) + n) % len(abc)] 
    # 이거 꼭 잘 기억하도록 하자 ㅇㅋ 

def solution(s, n):
    answer = ''
    
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in s:
        if i in abc:
            answer += abc[(abc.index(i) + n) % len(abc)]
        elif i in ABC:
            answer += ABC[(ABC.index(i) + n) % len(abc)]
        else:
            answer += " "
            
    return answer