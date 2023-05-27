'''
    제한사항
    - N(1 ≤ N ≤ 1,000,000)
'''

n = int(input())
li = [int(input()) for _ in range(n)]

li.sort()

for i in li:
    print(i)