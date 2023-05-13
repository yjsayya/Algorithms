
def solution(s):
    answer = []
    li = []
    
    for i in s:
        if i not in li:
            answer.append(-1)
            li.insert(0,i)
        else:
            answer.append(li.index(i) + 1)
            li.insert(0,i)
            
    return answer