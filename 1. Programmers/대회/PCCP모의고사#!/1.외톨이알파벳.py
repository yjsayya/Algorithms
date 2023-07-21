''''''
"""
    dic을 이용해서 잘 풀어냈다 굿굿 
    
"""

def solution(input_string):
    abc = []

    for i in input_string:
        if not abc:
            abc.append(i)
        else:
            if abc[-1].find(i) == 0:
                abc[-1] += i
            else:
                abc.append(i)
    # {알파뱃개수, 덩어리 갯수}
    dic = dict()
    for i in abc:
        if i[0] in dic:
            dic[i[0]][0] += len(i)
            dic[i[0]][1] += 1
        else:
            dic[i[0]] = [len(i), 1]
    ans = []
    for i in dic:
        if dic[i][0] >= 2 and dic[i][1] >= 2:
            ans.append(i)

    return "".join(sorted(ans)) if ans else "N"