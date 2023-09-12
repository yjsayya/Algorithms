''''''
"""
    << stack을 이용한 구현문제 >> 
    - while문, for문 돌릴때 IndexError 꼭 조심하도록 하자
    - stack이 비어있을 떄 while문 break

"""

# 여러번 풀었지만 -- 이게 가장 깔끔하게 푼 풀이인 듯 하다
n = int(input())
numList = [int(input()) for _ in range(n)]

stack = []
ans = []

for i in range(1,n+1):
    stack.append(i)
    ans.append('+')
    while stack and stack[-1] == numList[0]:
        stack.pop()
        ans.append('-')
        numList.pop(0)

if stack:
    print("NO")
else:
    for i in ans:
        print(i)