'''
원래는 String으로 이진수를 바꾼 후 String에 변환을 할까 했는데
어차피 컴퓨터는 2진수에 최적화가 되어있으므로 대입되는 숫자가 좀 커도
    - 시간복잡도 크게 생각하지 않고 그냥 1씩 더해서 이진수로 변환 후 따지는 형식으로 갔다
    - 무차별 대입으로 풀었단 의미 ㅇㅇ
    - 그래도 효율성테스트 0.01ms 넘어가는 것 없었다 ㅇㅋ
'''


def solution(n):
    answer = 0
    binaryN = bin(n)
    a = n + 1 
    while True:
        binaryA = bin(a)
        if bin(n).count('1') == binaryA.count('1'):
            answer = a
            break
        
        a += 1
        
    return answer



# 같은 원리이긴 했는데 - 이 방법이 조금 더 깔끔했던 것 같다
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n