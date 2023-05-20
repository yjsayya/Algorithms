'''
    이중 for문으로 풀긴 했는데, 시간복잡도가 그리 좋아보이진 않는다
    --> range() 숫자 범위 잘 따져서 해야한다

    여기선 이중 for문으로 푸는게 맞는 듯하다
    두번째 풀이에서는 Counter 라이브러리를 썼는데 오히려 시간복잡도가 더 좋지 않았다.
'''

def solution1(want, number, discount):
    
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


from collections import Counter
def solution2(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer