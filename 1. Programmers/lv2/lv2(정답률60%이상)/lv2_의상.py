'''
    구현 문제인 듯 하다
    --> 시간복잡도도 별로 걸리지 않게 제한된 수가 많지 않다
    --> 구현을 얼마나 잘하는지 물어보는 문제인 듯 
'''

# 첫번째 풀이 --> 개 ㅈㄹ을 해서 삼중 for문으로 풀었는데
    # 테스트 케이스 1번만 시간 초과가 되었다.
from itertools import combinations as comb
def solution(clothes):
    
    dic = dict()
    cnt = 0
    li = []
    
    for i,j in clothes:
        if j in dic:
            dic[j] += 1
            continue
        dic[j] = 1
    
    for k in dic.values():
        li.append(k)    
    
    for l in range(1,len(li)+1):
        tot = 0
        for m in comb(li,l):
            mul = 1
            for n in m:
                mul *= n
            tot += mul
        cnt += tot
            
    return cnt