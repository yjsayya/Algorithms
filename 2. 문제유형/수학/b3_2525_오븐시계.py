
'''
    이 부분이 핵심이라고 할 수 있다 
    아이디어 - 특정 부분을 '순환'해야할 때 ; 
        - 순환 해야하는 해당 크기만큼 나눈 나머지 값
        - 시간은 0부터 23까지 있으니깐 24로 나눈 나머지 값
        ex) hr = (a + cnt) % 24
'''

a,b = map(int,input().split())
c = int(input())

if b+c < 60:
    print(str(a) + ' ' + str(b+c))
elif b+c >= 60:
    # min
    min = b+c
    cnt = 0
    while min >= 60:
        min -= 60
        cnt += 1
    # hr
    hr = (a + cnt) % 24

    print(str(hr) + " " + str(min))