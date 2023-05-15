
'''
    아이디어 --> insert를 통해서 젤 앞에다가 집어 넣으면 상관 없지 ㅎㅎ 
    그러면 index() 써도 별 고민 없이 해결할 수 있다 
'''

def solution(s):
    answer = []
    stack = []
    
    for i in s:
        if i not in stack:
            answer.append(-1)
            stack.insert(0,i)
        else:
            answer.append(stack.index(i) + 1)
            stack.insert(0,i)
            
    return answer


def solution(s):
    
    stack = []
    answer = []
    
    for i in s:
        if stack.count(i) == 0:
            answer.append(-1)
        elif stack.count(i) == 1:
            answer.append(len(stack) - stack.index(i))
        else:
            answer.append(len(stack) - list(filter(lambda x: stack[x] == i, range(len(stack))))[-1])
        
        stack.append(i)
            
    return answer