# 전체 알파벳 수는 최대 15 * 5 = 75이기 때문에 --> 시간 복잡도는 고려하지 않아도 되는 문제

# 첫번째 풀이
    # 아주 개 ㅈㄹ을 하면서 풀었네
    # 문제 좀 제발 꼼꼼히 읽도록 하자
words = [""] * 5
words_len = []
answer = ""

for i in range(5):
    words[i] = input()

for j in range(len(words)):
    words_len.append(len(words[j]))

m = max(words_len)
for k in range(len(words)):
    if len(words[k]) < m:
        while len(words[k]) < m:
            words[k] += ' '

for j in range(m):
    for k in range(len(words)):
        answer += words[k][j]

while ' ' in answer:
    answer = answer.replace(' ', '')

print(answer)

# 다른 사람 풀이 가져와 봤다
text = []
for i in range(5):
    text.append(input())

for j in range(max(len(e) for e in text)):
    for k in range(5):
        if j < len(text[k]):
            print(text[k][j], end=' ')


text = []
for i in range(5):
    text.append(input())
