# 단순 문자열 구현 문제

# 첫번째로 푼 풀이
    # --> 예외만 잘 생각하면 어렵지 않은 문제였다
    # 예외1 - stack 젤 뒤에 있는 요소와 다른데 앞에도 아예 없으면 추가
    # 예외2 - stact 젤 뒤에 있는 요소와 다른데 앞에 있으면 그대로 끝

n = int(input())
words = [" "] * n
for _ in range(n):
    words[_] = input()

cnt = 0
for i in words:
    check = True
    stack = []
    for j in i:
        if len(stack) == 0:
            stack.append(j)
        else:
            if j != stack[-1] and j not in stack:
                stack.append(j)
            elif j != stack[-1] and j in stack:
                check = False
                break
    if check:
        cnt += 1

print(cnt)



# 계산할게 적어서 --> 시간 복잡도 안 따지고 그냥 단순하게 구현 했는데
# 다른 사람들은 어떻게 풀었는지 궁금하니깐 찾아보자

