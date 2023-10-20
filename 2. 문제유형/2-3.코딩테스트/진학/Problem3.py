
def solution(orders):
    # 1. dict으로 {유저:주문 메뉴} 구하기
    dic = dict()
    for order in orders:
        arr = order.split(" ")
        name = arr[0]
        se = set(arr[1:])

        if name in dic:
            dic[name] = dic[name].union(se)
        else:
            dic[name] = se
    # 2. 주문한 음식 수가 많은 순으로 정렬하기
    li = sorted(dic.keys(), key= lambda x : (-len(dic[x]) ,x))
    # 3. 정렬하기
    ans = []
    maxi = len(dic[li[0]])
    for name in li:
        if len(dic[name]) == maxi:
            ans.append(name)
        else:
            break

    return ans