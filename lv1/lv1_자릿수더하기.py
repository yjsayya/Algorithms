
'''
** 리스트 내 for문을 돌릴 경우 시간복잡도에서 이득을 볼 수 있다
    시간복잡도가 중요할 경우 리스트 내 for문 사용하는 것이 좋다 
    오 이건 몰랐네
'''

def solution(n):
    return sum([int(i) for i in str(n)])


def solution1(n):
    
    answer = 0
    for i in str(n):
        answer += int(i)
    
    return answer


print(solution(123))
print(solution(1234))
print(solution(12345))

