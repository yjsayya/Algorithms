

'''
    제한사항
    - (1 <= n.l <= 1,000)
    - (1 <= 물이 새는 위치 <= 1,000)

    뭔가 구현이 어려웠다 
    아이디어 - 시작 끝 사이에 없으면 되는거지 
'''
import sys

n,l = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

li.sort()

cnt = 1
start = li[0]
end = li[0] + l

for i in range(n):
    if start <= li[i] < end:
        continue
    else:
        start = li[i]
        end = li[i] + l
        cnt += 1
        
print(cnt)