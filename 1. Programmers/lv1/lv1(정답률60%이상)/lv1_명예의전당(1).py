
'''
    일단 첫번째 푼 풀이를 보면 - 한번 할때마다 정렬을 계속 해줘야하기 때문에
    시간복잡도가 별로 좋진 않겠지만
    제한 사항이 별로 크지 않았기 때문에 이렇게 작성을 했고 
    문제 없이 통과하였다 
'''


def solution(k, score):
    answer = []
    
    for idx,ele in enumerate(score):
        if idx < k:
            answer.append(min(score[:idx+1]))
        else:
            answer.append(sorted(score[:idx+1], reverse=True)[k-1])
            
    return answer

'''
필요 없으면 빼버리면 되는구나 .. 이걸 생각못했네 
시간복잡도가 훨씬 좋아졌다
'''

def solution(k, score):
    rank = []
    answer = []
    
    for idx,ele in enumerate(score):
        if idx < k:
            rank.append(ele)
            answer.append(min(rank))
        else:
            if min(rank) < ele:
                rank.remove(min(rank))
                rank.append(ele)
            answer.append(min(rank))
            
    return answer