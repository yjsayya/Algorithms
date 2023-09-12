# String이 주제이기만 한 알고리즘 문제

# stack으로 푸는 문제였다
# 내가 첫번째 푼 문제
n = int(input())
answer = ''
for i in range(n):
    str1 = input()
    stack = []
    for j in str1:
        if len(stack) == 0:
            if j == '(':
                stack.append(j)
            elif j == ')':
                stack.append(j)
                break
        else:
            if j == '(':
                stack.append(j)
            elif j == ')':
                stack.pop()

    if len(stack) == 0:
        answer += 'YES\n'
    else:
        answer += 'NO\n'

print(answer)
