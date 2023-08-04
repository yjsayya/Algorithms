''''''
"""
    ** 아이디어 - 내림차순으로 정렬하면
        ele = 인용 횟수가 되고
        idx+1 = 논문 갯수가 되니깐
        ele == idx+1이 된 곳이 answer가 되고
        
        만약 
        
    예외까지 잡는게 굉장히 어려웠다 ㅅㅂ
"""

# 첫번째 풀이 - 뭐가 문제인지 테스트 케이스 9 한개를 통과 못했음
def solution(citations):
    # h-index 구하기
    n = len(citations)
    citations = sorted(citations, reverse=True)

    for idx, ele in enumerate(citations):
        if ele == idx + 1:
            return ele
        elif ele < idx + 1:
            return idx

# 예외 결국은 찾아냈다 - citations[-1] > n 이걸 추가로 예외처리 해줬더니 해결했다
def solution2(citations):
    n = len(citations)
    citations = sorted(citations, reverse=True)

    if citations[-1] > n:
        return n
    else:
        for idx, ele in enumerate(citations):
            if ele == idx + 1:
                return ele
            elif ele < idx + 1:
                return idx