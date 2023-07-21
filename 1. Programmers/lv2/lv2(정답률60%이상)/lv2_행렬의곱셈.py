''' 행렬의 곱셈 '''
"""
    구현 문제인 듯 하다 
    3중 for문으로 나름 잘 구현하긴 했는데 쉽진 않았다 
    
    
    << 푸는 방법 >>
    1. 3중 For문으로 그냥 단순하게 구현하기
    2. numpy 라이브러리 사용하기
    3. 
"""

# 내가 푼 1번 유형
def solution(arr1, arr2):
    answer = []

    # 1. arr2를 계산하기 편하게 정리
    newArr2 = []
    for i in range(len(arr2[0])):
        li = []
        for j in range(len(arr2)):
            li.append(arr2[j][i])
        newArr2.append(li)

    # newArr2를 정리하는 방법 이렇게 간단하게도 할 수 있따
    # ============================
    b = [[1,4,7], [2,5,8], [3,6,9]]
    zipped_b = list(zip(*b))
    print(zipped_b)
    # 출력 : [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    # 리스트 내 튜플로 반환을 해준다!!
    # ============================
    print(newArr2)

    # 2. 행렬 계산하기
    for a1 in arr1:
        li = []

        for a2 in newArr2:
            tot = 0
            for i in range(len(newArr2[0])):
                tot += a1[i] * a2[i]
            li.append(tot)

        answer.append(li)

    return answer

# 다른 사람이 푼 1번 유형 방법 - 이게 3중 For문으로는 가장 직관적인 듯
def productMatrix(A, B):
    answer = []

    for i in range(len(A)):
        arr = []
        for j in range(len(B[0])):
            tmp = 0
            for k in range(len(A[0])):
                tmp += A[i][k] * B[k][j]
            arr.append(tmp)
        answer.append(arr)

    return answer


# numpy는 따로 다운로드 받아서 사용해야함
import numpy as np
def productMatrix1(A,B):

    x = np.array(A)
    y = np.array(B)
    answer = x*y

    return answer.tolist()

# 이런 방법도 있다고 함
def productMatrix2(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]