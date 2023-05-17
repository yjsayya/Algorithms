'''
    int() 함수의 작동 방식
        각 자리를 더하고 10을 곱하지만 2진수 형태로 저장되기 때문에 자릿수에 또 한번 비례한다
        시간복잡도 : O(자릿수 * * 2)
    
    따라서 두번째 방법으로 푸는 것이 훨씬 시간 복잡도에서 이득을 볼 수 있다
'''

def solution(s):
    return int(s)


def solution1(s):
    answer = 0
    
    for i in s:
        if i == '1':
            answer = answer * 10 + 1
        elif i == '2':
            answer = answer * 10 + 2
        elif i == '3':
            answer = answer * 10 + 3
        elif i == '4':
            answer = answer * 10 + 4
        elif i == '5':
            answer = answer * 10 + 5
        elif i == '6':
            answer = answer * 10 + 6
        elif i == '7':
            answer = answer * 10 + 7
        elif i == '8':
            answer = answer * 10 + 8
        elif i == '9':
            answer = answer * 10 + 9
        elif i == '0':
            answer = answer * 10 + 0
        
    if s[0] == '-':
        return -answer
    else:
        return answer