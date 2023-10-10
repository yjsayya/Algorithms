""""""
"""
    1. 인생이 만만하지 않지
    - 그냥 list 써서 풀면  당연히 시간 초과
"""


import sys

k, l = map(int,sys.stdin.readline().split())

dic = dict()
for i in range(l):
    dic[sys.stdin.readline().rstrip()] = i

sorted_dic = sorted(dic.items(), key=lambda x : x[1])

for i in range(k):
    if i < len(sorted_dic):
        print(sorted_dic[i][0])
    else:
        break

# idx = 0
# while idx+1 <= k:
#     print(li[idx])
#     idx += 1