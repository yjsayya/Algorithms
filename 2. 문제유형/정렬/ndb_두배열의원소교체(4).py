'''
    if문 같은 디테일 꼭 살리도록 하자 ㅋㅋ 
'''
import sys

n, k = map(int, sys.stdin.readline().split())
aArr = list(map(int, sys.stdin.readline().split()))
bArr = list(map(int, sys.stdin.readline().split()))

aArr.sort()
bArr.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        aArr[i] = bArr[i]
    else:
        break

print(sum(aArr))