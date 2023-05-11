

n = int(input())

an = 0
an1 = 1  

answer = 0

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(3, n+2):
        answer = an + an1 
        an = an1
        an1 = answer

    print(answer)
