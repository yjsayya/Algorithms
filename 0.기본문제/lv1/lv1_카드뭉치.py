# 1st 풀이
def solution(cards1, cards2, goal):

    for i in range(len(goal)):
        if len(cards) != 0 and goal[0] == cards1[0]:
            goal.pop(0)
            cards1.pop(0)
        elif len(cards2) != 0 and goal[0] == cards2[0]:
            goal.pop(0)
            cards2.pop(0)
        else:
            break
    
    if len(goal) != 0:
        return "No"
    else:
        return "Yes"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

# 테스트 케이스 통과 못하는게 있음 
# ** if문을 쓸 때; len(cards) != 0 길이 조건을 무조건 먼저 붙여줘야 통과할 수가 있다 !!!
# 이런 반례 찾기 항상 연습 ㄱㄱ

# 다른 사람 풀이
def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    card1_idx, card2_idx = 0, 0
    
    for word in goal:
        if len(cards1) > card1_idx and word == cards1[card1_idx]:
            card1_idx += 1
        elif len(cards2) > card2_idx and word == cards2[card2_idx]:
            card2_idx += 1
        else:
            answer = "No"
            break
    
    return answer