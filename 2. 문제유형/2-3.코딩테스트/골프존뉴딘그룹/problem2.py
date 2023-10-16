""""""
"""
    구현 문제였다 
    -- 좀 복잡하긴 했지만 잘 풀어낸 것 같다
"""
def solution(products, purchased):
    # 1. 구매 물품 -- dict 자료형으로 만들기
    dic = dict()
    for string in products:
        li = list(string.split())
        dic[li.pop(0)] = li

    # 2. 고객 구매 제품의 특성 dict 자료형으로 찾고 정렬하기
    dic2 = dict()
    for key in purchased:
        for i in dic[key]:
            if i in dic2:
                dic2[i] += 1
            else:
                dic2[i] = 1
        del dic[key]

    # 3. 추천 제품 찾기
    se = set(dic.keys())
    for i,_ in sorted(dic2.items(), key=lambda x: (-x[1], x[0])):
        new_se = set(se)
        for key in new_se:
            if i not in dic[key]:
                se.remove(key)
                new_se.add(key)
        if len(se) == 1:
            break
        if not se:
            se = new_se

    return se.pop()
