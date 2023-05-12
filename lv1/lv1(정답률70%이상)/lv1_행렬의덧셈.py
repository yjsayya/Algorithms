# 행렬의 덧셈은 numpy 라이브러리로도 풀 수 있다 

def solution1(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]

    return arr1


def solution2(arr1, arr2):
    
    answer = []
    
    for i in range(len(arr1)):
        li = []
        for j in range(len(arr1[i])):
            li.append(arr1[i][j] + arr2[i][j])
        answer.append(li)
    return answer
    

# solution1이 아무래도 조금 더 빠르다