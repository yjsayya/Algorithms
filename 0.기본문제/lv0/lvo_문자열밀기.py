def solution(A, B):
    check = False
    a_list = list(A)
    cnt = 0
    
    for i in range(len(a_list)):
        if "".join(a_list) == B:
            check = True
            break
        
        a_list.insert(0, a_list.pop())
        cnt += 1
    
    if check == True:
        return cnt
    else:
        return -1


for i in range(1,11):
    print(i)
# 걍 list로 풀었음
# 원래는 str로 풀어야하는데 