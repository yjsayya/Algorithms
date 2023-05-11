


# 첫번째 풀이 --> 풀긴 했는데 : 시간초과가 나왔다
def solution(k, tangerine):
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

def solution(k, tangerine):
    cnt = 0
    answer = 0

    counter = Counter(tangerine)
    
    for c in counter.most_common():
        cnt += c[1]
        answer += 1
        if cnt >= k:
            return answer

# counter library를 사용하면 쉬운 코드였네