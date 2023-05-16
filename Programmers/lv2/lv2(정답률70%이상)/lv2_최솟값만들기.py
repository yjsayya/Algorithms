
'''
이 정도도 빠르게 넘어가도록 하자 
sort() vs sorted() 꼭 알아두도록 하자 
'''

def solution(A,B):
    answer = 0
    
    for a,b in zip(sorted(A), sorted(B, reverse=True)):
        answer += a*b

    return answer