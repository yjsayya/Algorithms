


# 첫번쨰 푼 풀이
    # --> 시간 복잡도를 고려하지 않아서 좀 구린 듯

def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    for i in range(len(participant) -1):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    
    if answer == '':
        return participant[-1]
    else:
        return answer


# hash로 풀어봤음
    # 근데 이게 효율성 테스트에서 오히려 시간 초과 났음 

def solution1(participant, completion):
    dic = {}
    
    for i in participant:
        dic[i] = participant.count(i)
    
    for j in completion:
        dic[j] = dic.get(j) - 1
        if dic[j] ==0:
            del dic[j]
    
    return list(dic)[0]
