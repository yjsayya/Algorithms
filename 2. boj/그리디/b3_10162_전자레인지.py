
'''
    ** 대표적인 그리디 문제
    -- a,b,c가 배수 관계이기 때문에 탐색 알고리즘으로 풀 수 있다!!
    -- 배수 관계가 아니라면 탐색 알고리즘 사용하면 안된다

    a 버튼 --> 5min --> 300sec
    b 버튼 --> 1min --> 60sec
    c 버튼 --> 10sec
'''

t = int(input())

cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
while t != 0:
    if t >= 300:
        t -= 300
        cnt1 += 1
    elif t >= 60:
        t -= 60
        cnt2 += 1
    elif t >= 10:
        t -= 10
        cnt3 += 1
    else:
        cnt = -1
        break
if cnt == -1:
    print(cnt)
else:
    print(cnt1, end=' ')
    print(cnt2, end=' ')
    print(cnt3, end=' ')