# reversed() 내장함수 이거 꼭 알아두자
# python은 정말 없는 함수가 없는 것 같다

def solution(n):
    answer = []
    
    for i in str(n):
        answer.append(int(i))
    
    answer.reverse()
    return answer


def solution1(n):
    return [ int(i) for i in reversed(str(n))]

print(solution1(12345))