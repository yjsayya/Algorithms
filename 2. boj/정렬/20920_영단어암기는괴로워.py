# 실버 3
'''
    ** 우선 순위 기준 설정 공부에 도움을 줄 수 있는 문제 
    ** 사전 순으로 정리
    - 알파벳 순
    - 길이도 고려!!

    제한사항
    - (1 <= n <= 100,000)
    - (1 <= m <= 10)
'''

n,m = map(int, input().split())
dic = dict()
for _ in range(n):
    word = input()
    if len(word) >= m:
        if word in dic:
            dic[word][0] += 1
        else:
            dic[word] = [1, len(word), word]

li = sorted(dic.items(), key= lambda x : (-x[1][0], -x[1][1], x[1][2]))

print(li)

for i in li:
    print(i[0], end="\n")