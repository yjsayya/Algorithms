
'''
이거 한번 확인하고 가자
[대문자 소문자 전환]
    str.upper()
    str.lower()
    str.title()
    str.capitalize()
    str.swapcase()
'''

def solution(s):

    s_list = s.split(" ")
    
    for i in range(len(s_list)):
        s_list[i] = s_list[i].capitalize()        
    
    return " ".join(s_list)