# import sys
# li = list(sys.stdin.readline().split())
# n = int(li[0])
# x = int(li[1])

# k = list(map(int,sys.stdin.readline().split()))
# answer = []
# for i in k:
#     if i < x:
#         answer.append(i)
    
# for j in answer:
#     print(str(j), end=' ')





# 프로그래머스 영어 끝말잇기
def solution(n, words):
    answer = [0, 0]
    dict = set()
    idx = 0

    wsize = len(words)

    pword = ''
    while idx < wsize:
        word = words[idx]

        if (len(pword) > 1 and word[0] != pword[-1]) or word in dict:
            return [(idx%n)+1, int(idx/n)+1]
            
        dict.add(word)
        idx += 1
        pword = word

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))