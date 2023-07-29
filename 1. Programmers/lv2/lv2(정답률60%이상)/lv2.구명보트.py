''''''
"""
   투포인터로 푸는 문제였다
   - 근데 그냥  
"""

# 첫번째 풀이 - 시간 초과 + 틀렸다
# 근데 시간초과는 그렇다쳐도 시부레 왜 틀린건지 모르겠네

def solution(people,limit):
    people.sort(reverse=True)
    cnt = 0
    while people:
        if len(people) < 2:
            cnt += 1
            people.pop(0)
        elif people[0] + people[1] > limit:
            people.pop(0)
            cnt += 1
        else:
            cnt += 1
            people.pop(0)
            people.pop(0)

    return cnt



# 투포인터 풀이1
def solution2(people, limit):

    answer = 0
    people.sort()
    
    start = 0 
    end = len(people) - 1
    
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    
    return answer


# 투포인터 풀이2
def solution3(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

print(solution3([70, 50, 80, 50], 100))


"""
<< 투포인터 알고리즘(Two Pointer Algorithmn) >>
    - 정렬된 배열에서
    - 두개의 포인터를 사용하여 
    - 특정 조건을 만족하는 요소를 찾는 데 사용되는 알고리즘
    
    ** 배열이 이미 정렬이 되어있어야 한다 
"""