''''''
"""
   투포인터로 푸는 문제였다
   완벽하게 이해했다 시부레 ...
"""

# 첫번째 풀이 - 시간 초과 + 틀렸다
# 그리디로 풀면 안된다 !!
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

# 투포인터_문자열 풀이1
def solution2(people, limit):

    people.sort()

    ans = 0
    left, right = 0, len(people)-1
    while left <= right:
        ans += 1
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1

    return ans

"""
<< 투포인터_문자열 알고리즘(Two Pointer Algorithmn) >>
    - 정렬된 배열에서
    - 두개의 포인터를 사용하여 
    - 특정 조건을 만족하는 요소를 찾는 데 사용되는 알고리즘
    
    ** 배열이 이미 정렬이 되어있어야 한다 
"""