# try-catch문이 별로 시간복잡도가 좋은것 같지는 않다 

def solution(arr):
    stack = []

    for i in arr:
        try:
            stack.append(i)
            if i == stack[-2]:
                stack.pop()
        except:
            pass

    return stack

def solution(arr):
    
    stack = [arr[0]]
    
    for i in range(1,len(arr)):
        if stack[-1] != arr[i]:
            stack.append(arr[i])
    
    return stack

# 이렇게 한줄로 적는 사람도 있다 
def no_continuous(s):
    return [s[i] for i in range(len(s)) if s[i] != s[i+1:i+2]]