
'''

# 이게 지그재그로 이루어져 있는 수열 
# -> 1/1
#    1/2 2/1 <-
# -> 1/3 2/2 3/1
#    1/4 2/3 3/2 4/1 <-
# -> 1/5 2/4 3/3 4/3 5/2 6/1

'''

x = int(input())

# 1. 몇번째 수열인지 먼저 구하자
idx = 0
for i in range(1,x+1):
    if x <= i*(i+1)//2:
        idx = i
        break

# # 2. 구체적인 수열을 구하자
li = [i for i in range(idx*(idx-1)//2+1, idx*(idx+1)//2 +1)]

seq = li.index(x)
if len(li) % 2 == 0:
    분자 = seq + 1
    분모 = len(li) - seq
else:
    분자 = len(li) - seq 
    분모 = seq + 1

print(str(분자) + '/' + str(분모))

