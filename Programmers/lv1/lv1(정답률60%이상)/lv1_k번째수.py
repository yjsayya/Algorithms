
def solution(array, commands):
    
    answer = []
    
    for i in commands:
        arr = array[i[0]-1:i[1]]
        arr.sort()
        answer.append(arr[i[2]-1])
    
    return answer




# sorted() 써도 될 듯?!
# 다중 배열일 때; 이런식으로 사용 가능!!
def solution(array,commands):
    
    answer = []
    
    for i,j,k in commands:
        arr = sorted(array[i-1:j])
        answer.append(arr[k-1])
    
    return answer