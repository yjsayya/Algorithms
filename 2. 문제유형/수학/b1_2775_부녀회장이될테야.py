'''
    제한사항 (1 ≤ k, n ≤ 14)
    
    idea 
    - 제한사항이 워낙 작아서 1층부터 14층까지 몇명 사는지 전부 구한 다음에
    - 간단하게 뽑아냈다 

'''

# 1. 1층부터 14층까지 거주하는 사람 수 전부 구하기
apart = dict()

apart[0] = [i for i in range(1,15)]
for i in range(1, 15):
    apart[i] = [sum(apart[i-1][:j+1]) for j in range(14)]

# 2. t 입력 받기
t = int(input())

# 3. k,n 입력 받기 
answer = []
for _ in range(t):
    k = int(input())
    n = int(input())

    answer.append(apart[k][n-1])

# 4. 출력하기
for j in answer:
    print(j)