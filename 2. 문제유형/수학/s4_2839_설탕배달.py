
'''
    이 정도는 이제 문제 없이 풀 수 있지 ㅎㅎ 
    idea - 모든 경우의 수를 구하고 - 그 중 최솟값을 반환하면 된다 
    ** 아마 list가 아니라 set으로 해보니깐 조금 더 빨랐다
'''

# list로 풀었음
n = int(input())

cnt = []
for i in range(n//5+1):
    kg = n - 5*i
    if kg % 3 == 0:
        cnt.append(i+kg//3)
    
if len(cnt) == 0:
    print(-1)
else:
    print(min(cnt))


# 똑같은 풀이인데 set으로 풀어봤음
n = int(input())

cnt = set()
for i in range(n//5+1):
    kg = n - 5*i
    if kg % 3 == 0:
        cnt.add(i+kg//3)
    
if len(cnt) == 0:
    print(-1)
else:
    print(min(cnt))