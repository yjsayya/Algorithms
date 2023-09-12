
'''
'''

import sys
# 0. t 입력 받기
t = int(sys.stdin.readline())
result = []

for i in range(t):
    # 1. 입력받기
    func = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    pArr = sys.stdin.readline().rstrip()

    # 2. p배열 - 리스트로 쓸 수 있게 정리하기
    if n != 0:
        pArr = pArr[1:-1]
        pArr = list(map(int,pArr.split(',')))
    else:
        pArr = []

    # 3. 매커니즘 진행시켜 
    try:
        for i in func:
            if i == 'R':
                pArr.reverse()
            elif i == 'D':
                pArr.pop(0)
        result.append(pArr)
    except:
        result.append('error')

# 4. 출력하기
for k in result:
    print(k)