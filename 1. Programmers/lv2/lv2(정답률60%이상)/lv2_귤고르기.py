import sys
"""
    Counter 라이브러리 꼭 알아두자
    O(nlogn)의 시간복잡도를 가진다 
        Counter(iter).most_common() --> 이게 핵심 메소드 ㅎ
"""

# 첫번째 풀이 --> 풀긴 했는데 : 시간초과가 나왔다
def solution1(k, tangerine):
    cnt = 0
    
    size = list(set(tangerine))
    num = [0] * len(size)
    
    for i in range(len(size)):
        num[i] = tangerine.count(size[i])

    num.sort(reverse=True)
            
    for j in num:
        cnt += 1
        k -= j
        if k <= 0:
            break
        
    return cnt


# 시간 복잡도 고려해서 다시 풀어보자
from collections import Counter
def solution2(k, tangerine):
    cnt = 0
    answer = 0

    cntr = Counter(tangerine)
    
    for c in cntr.most_common():
        cnt += c[1]
        answer += 1
        if cnt >= k:
            return answer

# counter library를 사용하면 쉬운 코드였네

a = [1, 3, 2, 5, 4, 5, 2, 3]
counter = Counter(a)
print(counter)
print(counter.most_common())