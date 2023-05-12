# 리스트 자체가 시간복잡도가 굉장히 불리한듯 하다 

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


# 이렇게 python 내장함수 ord(), chr()로 풀어도 괜찮다!!!
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)