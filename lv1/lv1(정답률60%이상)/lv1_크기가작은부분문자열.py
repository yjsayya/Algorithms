def solution(t, p):
    num = []
    cnt = 0
    try:
        for i in range(0,len(t)-len(p)+1):
            num.append(int(t[i:i+len(p)]))
    except IndexError:
        pass
    
    for j in num:
        if j <= int(p):
            cnt += 1

    return cnt