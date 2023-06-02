
'''
    아이디어 - 역추적해보면 쉽게 풀 수 있는 문제였다 
'''

s = input()
t = input()

n = len(t) - len(s)

for _ in range(n):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        a = list(t)[:-1]
        a.reverse()
        t = "".join(a)

if s == t: print(1)
else: print(0)