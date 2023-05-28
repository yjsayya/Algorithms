'''
    제한사항
    - 1 <= n <= 1,000
    - 1 <= 추의 무게 <= 1,000,000
'''

n = int(input())
li = sorted(list(map(int, input().split())))

answer = 0
for i in li:
    if i <= answer + 1:
        answer += i
    else:
        break

print(answer+1)