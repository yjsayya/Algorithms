
# <문제 설명>
# 정수로 이루어진 배열 numbers가 있습니다. 
# 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
# 정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 
# 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.


# 내가 처음에 푼 풀이 
    # --> 잘풀긴 했는데 시간 초과남 
    # --> 시간복잡도 O(n^2)함
def solution(numbers):  
    answer = []
    n = len(numbers)
    
    for _ in range(len(numbers)):
        num = numbers.pop(0)
        for j in numbers:
            if num < j:
                answer.append(j)
                break
        if len(answer) + len(numbers) != n:
            answer.append(-1)
            
    return answer


# 이렇게 그냥 무차별 대입으로 풀면 에러가 난다 
    # --> 시간 복잡도 무조건 고려해줘야

# 시간복잡도 

# stack으로 풀어볼까? 
def solution2(numbers):
    answer = [-1]*(len(numbers))
    stack = []
    for i, val in enumerate(numbers):
        while stack and numbers[stack[-1]] < val:
            answer[stack.pop()] = val
        stack.append(i)
    return answer

# ㅅㅂ 어려운데 
# 일단 기술적인거 가져가자
    # --> enumerate(잇터레이터) index와 element 값을 동시에 가져올 수 있다!
    # --> while (list):
        # - list가 비어있으면 false;
        # - list가 채워져있으면 true;

