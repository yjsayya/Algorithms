"""
    스택 문제였는데
    while문, for문 돌릴때 IndexError 꼭 조심하도록 하자
    특정 리스트가 비어있을 떄 while문 탈출할수 있도록 해야한다

"""

n = int(input())
numList = [int(input()) for _ in range(n)]
stack = []
ans = []

for i in range(1,n+1):
    stack.append(i)
    ans.append('+')

    if len(stack) != 0:
        while numList[0] == stack[-1]:
            stack.pop()
            numList.pop(0)
            ans.append('-')

            if len(numList) == 0 or len(stack) == 0:
                break

if numList:
    print("NO")
else:
    for k in ans:
        print(k, end='\n')