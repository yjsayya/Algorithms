
'''
3번째 람다 풀이가 가장 시간복잡도가 좋긴 하다 
'''

def solution(s):
    answer = []
    
    for i in s.split(' '):
        word = ''
        for j in range(len(i)):
            if j % 2 == 0:
                word += i[j].upper()
            else:
                word += i[j].lower()
        
        answer.append(word)
                
    return " ".join(answer)



def solution(s):
    
    answer = ''
    
    for i in s.split(' '):
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
                
    return answer[:-1]


# 이건 또 람다 쓰는게 젤 빠르네 ...
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))