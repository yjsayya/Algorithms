def solution(number, k):

    answer = ''

    while k > 0:
        num = number[:k]
        if len(num) == 0:
            break
        answer += max(num)

        number = number[num.find(max(num))+1:]
        k -= num.find(max(num))

    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
