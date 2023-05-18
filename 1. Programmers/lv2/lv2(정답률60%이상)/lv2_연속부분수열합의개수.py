'''
    제한사항
        3 ≤ elements의 길이 ≤ 1,000
        1 ≤ elements의 원소 ≤ 1,000
    별로 크지 않아서 시간 복잡도 크게 고려하지 않고 첫번째 풀이를 작성하였다
    근데 구려도 너무 구려서 수정이 필요했다 
'''



# 첫번째 풀이
    # 풀긴 했는데 시간복잡도가 아주 구리다 
    # 좀 더 개선이 필요하다 
    # idea : 뒤에 붙여서 반복하면 되는거지 
def solution1(elements):
    
    n = len(elements)
    elements.extend(elements[:-1])
    ele = set()
    
    for i in range(1,n+1):
        for j in range(n):
            ele.add(sum(elements[j:j+i]))
    
    return len(ele)


# 다른 사람 풀이 가져왔다 ㅋㅋ 
    # 이렇게도 풀 수 있다 
def solution2(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)

