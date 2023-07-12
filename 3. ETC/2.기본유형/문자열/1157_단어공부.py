# 단순 문자열 구현 문제
# abc = list(set(str)) --> 중복 제거 이렇게 하면 좀 편한 듯?!


word = input().upper()
abc = list(set(word))
answer = [0] * len(abc)

for i in range(len(abc)):
    answer[i] = word.count(abc[i])

if answer.count(max(answer)) > 1:
    print("?")
else:
    print(abc[answer.index(max(answer))])
