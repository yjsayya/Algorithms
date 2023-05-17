# 대표적인 그리디 문제인 것 같다
    #idea - 최소 행동횟수를 구하려면 당연히 복제 마법이 최대한 많아야한다

n = int(input())
cnt = 1
cat = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while cat < n:
        cat *= 2
        cnt += 1

    print(cnt)



