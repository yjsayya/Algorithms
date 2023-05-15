'''
    이중 for문 밖에 없나?
    dic을 잘 쓰면 되는 문제 ㅇㅋ
'''

def solution(name, yearning, photo):
    answer = []
    score = {}
    
    for mem, num in zip(name, yearning):
        score[mem] = num
    
    for i in photo:
        total = 0
        for j in i:
            if j in score:
                total += score[j]
        answer.append(total)
    
    return answer