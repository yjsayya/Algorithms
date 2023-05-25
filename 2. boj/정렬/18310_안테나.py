# 실버 3 - 2019 소마 기출문제
'''

'''

# 첫번째 풀이 -- 이따구로 완전탐색으로 풀면 시간초과 남 ㅇㅇ ㅋㅋㅋㅋ
# import sys

# n = int(input())
# li = list(map(int,sys.stdin.readline().split()))
# li.sort()
# answer = []

# for i in li:
#     total = 0
#     for idx in range(0, len(li)):
#         total += abs(i - li[idx])
#     answer.append(total)

# print(li[answer.index(min(answer))]로

# 두번째 풀이 
import sys

n = int(input())
li = sorted(list(map(int,sys.stdin.readline().split())))

answer = 0

avg = sum(li) / n
print(avg)
for i in li:
    if i > avg:
        answer = i 
        break

print(answer)