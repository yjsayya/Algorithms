def solution(polynomial):
    li = polynomial.split(" + ")
    answer = ""
    x = 0
    ins = 0
    # 1. 이걸로 x와 ins 뽑아내고
    for i in li:
        if i[-1] != 'x':
            ins += int(i)
        else:
            if i == 'x':
                x += 1
            else:
                x += int(i[:-1])
    # 2. 모든 경우의 수 이걸로 쳌
    if ins == 0:
        if x == 0:
            answer = '0'
        elif x == 1:
            answer = 'x'
        else:
            answer = str(x) + 'x'
    else:
        if x == 0:
            answer = str(ins)
        elif x == 1:
            answer = 'x + ' + str(ins) 
        else:
            answer = str(x) + 'x + ' + str(ins)
    
    return answer