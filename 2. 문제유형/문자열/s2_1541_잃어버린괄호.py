
'''
    아이디어 
    - 마이너스 기호를 만날 때 다음 마이너스까지 더하면 되네
    ** 아이디어가 중요한 문제 
'''

# arr = input().split('-')

# s = 0
# for i in arr[0].split('+'):
#     s += int(i)

# for j in arr[1:]:
#     for k in j.split('+'):
#         s -= int(k)

# print(s)




# 10+20-20+40+30-20+30-90
# -220

arr = input().split('-')

answer = 0
for i in arr[0].split('+'):
    answer += int(i)

for j in arr[1:]:
    for k in j.split('+'):
        answer -= int(k)

print(answer)