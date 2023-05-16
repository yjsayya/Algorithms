'''
이 정도는 그냥 넘어가도 되겠지? 
'''

def solution(s):
    li = list(map(int, s.split()))
    return f"{min(li)} {max(li)}"