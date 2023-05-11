# set을 활용하여 중복을 제거함 --> 시간 복잡도가 얼마나 되는지는 잘 모르겠음
# 이렇게 3가지 list를 이용하여 풀었다
    # array = [1,2,3,3,3,4]
    # arr = [1,2,3,4]
    # listCnt = [1,1,3,1]

# 첫번째로 푼 풀이
def solution(array):
    listCnt = []
    arr = list(set(array))

    for i in arr:
        listCnt.append(array.count(i))

    if listCnt.count(max(listCnt)) > 1:
        return -1
    else:
        return arr[listCnt.index(max(listCnt))]

# 가장 깔끔하게 푼 것 같은 풀이를 가져와서 약간 수정했다
# idea는 염두해볼 만한 것 같다
    # set(array)에 있는 걸 쭉 지우면서 마지막에 남아있는걸 return 하는 방식인데
    # for문을 계속 돌려야하니깐 시간 복잡도에서 이득이 있는지는 잘 모르겠다

def solution3(array):
    answer = -1
    while len(array) != 0:
        if len(array) == 1:
            answer = array[0]
            break
        for i, ele in enumerate(set(array)):
            array.remove(ele)

    return answer