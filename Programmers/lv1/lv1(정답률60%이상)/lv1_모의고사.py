
# 내가 첫번째로 풀었던 풀이
#   n번 곱했기 때문에 시간복잡도에서 이득이 별로 없을 듯 하다 
def solution(answers):
    correct = [0,0,0]
    answer = []
    
    n = len(answers)
    num1 = [1,2,3,4,5] * n
    num2 = [2,1,2,3,2,4,2,5] * n
    num3 = [3,3,1,1,2,2,4,4,5,5] * n 
    
    for i in range(n):
        if answers[i] == num1[i]:
            correct[0] += 1
        if answers[i] == num2[i]:
            correct[1] += 1
        if answers[i] == num3[i]:
            correct[2] += 1
    
    for idx, ele in enumerate(correct):
        if ele == max(correct):
            answer.append(idx + 1)
    
    return answer
    

def solution2(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result