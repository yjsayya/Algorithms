# str.isdigit() 굉장히 유용한 함수인 것 같음 --> 꼭알아두자

# 내가 처음 푼 풀이
def solution(my_string):
    stack = []
    answer = 0

    if my_string.isdigit():
        return int(my_string)
    else:
        for i in my_string:
            if i.isdigit():
                stack.append(i)
            else:
                if len(stack) == 0:
                    continue
                else:
                    answer += int("".join(stack))
                    stack.clear()
        if len(stack) != 0:
            answer += int("".join(stack))

        return answer

# 예외처리
    # 1. 전부 숫자인 경우
    # 2. 전부 숫자가 아닌 경우 - return 0
    # 3. 숫자로 끝나는 경우 --> 마지막에 다시 answer에 넣어줘야한다
    # 4.

# 정규식을 이용해서 풀 수도 있음
import re
def solution1(my_string):
    num = map(int, re.findall(r"[0-9]+", my_string))
    return sum(num)


# 정규식 없이 가장 깔끔하게 푼 것
def solution3(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

# 위에 있는 걸 풀어서 써봤다 --> 이게 가장 best인 것 같다
def solution4(my_string):
    answer = ''
    for i in my_string:
        if i.isdigit():
            answer += ''.join(i)
        else:
            answer += ' '

    return sum(map(int, answer.split()))
