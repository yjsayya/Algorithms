'''
    ???!!!!!
    while True: 가급적이면 쓰지 말자!!!
    첫번째 코드는 시간초과가 났는데
    두번째 코드는 시간초과가 나지 않았다
    while문을 벗어나는 break문을 while옆에다가 써줬냐 마지막에 써줬냐의 차이 뿐이었는데 ...
'''

def solution(n,a,b):
    
    cnt = 0

    while True:
        
        if a % 2 == 0: a //= 2
        else: a = a//2 + 1
            
        if b % 2 == 0: b //= 2
        else: b = b//2 + 1
        
        cnt += 1
        
        if max(a,b) % 2 == 0 and abs(a-b) == 1:
            break

    return cnt + 1



def solution(n,a,b):
    
    cnt = 0

    while max(a,b) % 2 != 0 or abs(a-b) != 1:
        # a처리
        if a % 2 == 0: a //= 2
        else: a = a//2 + 1
        # b처리
        if b % 2 == 0: b //= 2
        else: b = b//2 + 1
        
        cnt += 1

    return cnt + 1