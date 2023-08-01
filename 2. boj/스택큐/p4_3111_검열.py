''''''
"""
    프로그래머스 스택/큐 문제 다 풀고 자신있게 도전해본 플래티넘 문제
    
    어떤 부분에서 예외가 
"""

# 첫번째 풀이 -- 잘 푼 거 같은데
#   어디서 예외가 있는지 모르겠다
word = input()
txt = input()

while txt.find(word) != -1:
    # 1. 첫번째 word 제거
    txt = txt.replace(word, '')

    if txt.find(word) == -1:
        break

    # 2. 마지막에 word가 딱 붙어있는 경우 제거
    if txt[-len(word):] == word:
        txt = txt[:-len(word)]
        continue

    # 3. 마지막 word 제거
    wordNum = txt.count(word)
    li = txt.split(word)
    newtxt = ''
    for i in li:
        newtxt += i
        if wordNum != 0:
            wordNum -= 1
            newtxt += word

print(txt)