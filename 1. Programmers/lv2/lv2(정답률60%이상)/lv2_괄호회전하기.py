
'''
완전 탐색으로 풀었다 
    - s의 길이가 1,000이하라고 하길래 완전탐색으로 풀어도 되겠다고 생각을 했다
    - 시간복잡도가 좋진 않지만 풀어냈다 
'''

def check(s):
    stack = []
    
    for i in s:
        if i == '[' or i == '{' or i =='(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                if i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                if i == ')' and stack[-1] == '(':
                    stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    
    cnt = 0
    for _ in range(len(s)-1):
        if check(s):
            cnt += 1
        s = s[1:] + s[0]
    
    return cnt