
'''
첫번째 풀이 시간초과가 났다 시부레
'''


def solution(s):
    
    if len(s) == 1:
        return 0
    
    
    for i in s:
        if s.count(i) % 2 != 0:
            return 0
        else:
            while i+i in s:
                s = s.replace(i+i, '')
    
    if len(s) == 0:
        return 1
    else: 
        return 0