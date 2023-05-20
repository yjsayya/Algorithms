def solution(want, number, discount):
    
    cnt = 0
    pro = dict()
    
    for i,j in zip(want, number):
        pro[i] = j
    
    for i in range(10, len(discount)+1):
        check = True
        for j in pro:
            if discount[i-10:i].count(j) < pro[j]:
                check = False
                break
        if check:
            cnt += 1
    return cnt


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))