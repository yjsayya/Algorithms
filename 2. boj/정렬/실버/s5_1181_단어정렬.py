# 실버 5
'''
    사전 순으로 정렬하는 방법 
        - 정렬하고
        - 길이 순으로 다시 한번 정렬
    여기서는 중복 제거를 set을 통해서 했다
'''

n = int(input())
li = set(input() for _ in range(n)) # 중복제거 해주고

li = sorted(li)
li = sorted(li, key= len)

for i in li:
    print(i)