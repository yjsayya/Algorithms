'''
실수로 break문을 깜빡했네
1번 코드를 깔끔하게 정리하면 2번 코드가 나온다

# 가장 먼저 탈락하는 사람의 번호, 자신의 몇번째 차레에 탈락하는지
# 1. 단어를 중복해서 틀리는 경우
# 2. 끝말잇기를 잘못한 경우
# 3. 틀린 사람이 없는 경우
'''

def solution1(n,words):
    
    num = 0
    # 1. 틀린 단어의 인덱스 번호 구하기
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            num = i
            break
        elif words[i] in words[:i]:
            num = i
            break
    # 2. 인덱스 번호 바탕으로 답 구하기
    if num == 0:
        return [0,0]
    else:
        return [num%n + 1 ,(num//n) + 1]
    


def solution2(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]


# 다시 풀어본 풀이
def solution3(n, words):
    lstLttr = words[0][0]

    for idx, word in enumerate(words):
        if word[0] != lstLttr or word in words[:idx]:
            return [(idx % n) + 1, int(idx / n) + 1]

        lstLttr = word[-1]

    return [0, 0]


# 시간 복잡도를 살짝 더 고려해서 set()을 이용해서 한번 풀어보았다
def solution4(n, words):
    wordVessel = set()
    lstLttr = words[0][0]

    for idx, word in enumerate(words):

        checkDup = len(wordVessel)
        wordVessel.add(word)

        if word[0] != lstLttr or len(wordVessel) == checkDup:
            return [(idx % n) + 1, int(idx / n) + 1]

        lstLttr = word[-1]

    return [0, 0]