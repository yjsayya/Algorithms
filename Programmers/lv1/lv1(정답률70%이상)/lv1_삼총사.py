
'''
대충 3가지 방법으로 풀어낼 수 있는 듯하다
    1. combinations 라이브러리를 이용하거나
    2. DFS를 이용하거나
    3. 삼중 for문 이용하는 방법인데 

    - 난 1번으로 풀었고
    - 3번은 시간복잡도가 엉망인것 같고
    - 2번은 기억할 필요가 있는 듯 하다 

    근데 여기서는 1번의 시간복잡도가 가장 빨랐다 ㅋㅋㅋ
'''


# combinations 라이브러리 이용
from itertools import combinations as cb
def solution(number):
    cnt = 0
    
    for i in list(cb(number, 3)):
        if sum(i) == 0:
            cnt += 1
        
    return cnt


# DFS 이용 
def solution(number):
    tot = 0
    def dfs(i, cnt, sum_num):
        nonlocal tot

        if cnt == 3 and not sum_num:
            tot += 1
            return

        if i == len(number):
            return

        if cnt < 3:
            dfs(i+1, cnt+1, sum_num + number[i])
            dfs(i+1, cnt, sum_num)

    dfs(0,0,0)        

    return tot